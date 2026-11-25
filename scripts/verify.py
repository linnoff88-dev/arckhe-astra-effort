#!/usr/bin/env python3
"""Confere originais, traduçêo dos dados, links HTML e manifesto local."""
import argparse
import csv
import hashlib
import json
import re
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '.venv', '__pycache__', 'node_modules', '.impeccable'}

def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and not EXCLUDED.intersection(p.relative_to(ROOT).parts)
                  and p != ROOT / 'MANIFEST.json')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs: self.links.append(attrs[key])

def verify():
    provenance=json.loads((ROOT/'source/provenance.json').read_text())
    for item in provenance['files']:
        old=item['path']
        path=ROOT/old if old.startswith(('source/','files/')) else ROOT/'original-en'/old
        assert path.stat().st_size == item['bytes'], f'Tamanho original: {old}'
        assert sha(path) == item['sha256'], f'Hash original: {old}'
    for item in json.loads((ROOT/'original-en/MANIFEST.json').read_text()):
        assert sha(ROOT/'original-en'/item['path']) == item['sha256'], item['path']
    for path in files():
        if path.suffix in ('.json','.excalidraw'):
            json.loads(path.read_text())
    with zipfile.ZipFile(ROOT/'files/Astra-Super-Guide.zip') as archive:
        assert archive.testzip() is None, 'ZIP inválido'
    for path in ROOT.glob('*.pdf'):
        assert path.read_bytes().startswith(b'%PDF-'), path
    english=json.loads((ROOT/'evidence/results.json').read_text())
    portuguese=json.loads((ROOT/'evidence/results.pt-BR.json').read_text())
    translated={'what','avatar','moat','proved','gap','takeaway'}
    assert len(english['runs']) == len(portuguese['runs']) == 7
    for before,after in zip(english['runs'],portuguese['runs']):
        assert before.keys() == after.keys()
        for key in before:
            if key not in translated: assert before[key] == after[key], key
        assert after['processed_tokens'] == after['input_tokens'] + after['output_tokens']
        assert 0 <= after['cached_input_tokens'] <= after['input_tokens']
    with (ROOT/'evidence/results.pt-BR.csv').open() as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==7
    for row,run in zip(rows,portuguese['runs']):
        for key,value in run.items(): assert row[key]==str(value), key
    blocks=re.findall(r'```text\n(.*?)\n```',(ROOT/'PROMPTS.md').read_text(),re.S)
    prompts=sorted((ROOT/'prompts').glob('*.txt'))
    assert len(blocks)==len(prompts)==10
    for block,path in zip(blocks,prompts): assert block.strip()==path.read_text().strip(),path
    original=(ROOT/'original-en/docs/transcricao-video.txt').read_text()
    translated_text=(ROOT/'docs/Texto colado(20260910-165842).txt').read_text()
    assert re.findall(r'\(\d{2}:\d{2}\)',original)==re.findall(r'\(\d{2}:\d{2}\)',translated_text), 'Timestamps da transcriçêo'
    pages={}
    for page in (ROOT/'guia').glob('*.html'):
        parser=Links();parser.feed(page.read_text());pages[page]=parser
        assert len(parser.ids)==len(set(parser.ids)), f'IDs duplicados: {page}'
        assert not re.search(r'\{\{[A-Z_]+\}\}',page.read_text()), f'Placeholder: {page}'
    for page,parser in pages.items():
        for link in parser.links:
            parts=urlsplit(link)
            if parts.scheme or parts.netloc: continue
            target=(page.parent/unquote(parts.path)).resolve() if parts.path else page
            if target.is_dir(): target=target/'index.html'
            assert target.exists(), f'Link ausente em {page.name}: {link}'
            if parts.fragment and target in pages:
                assert unquote(parts.fragment) in pages[target].ids, f'Âncora ausente: {link}'
    print(f'OK: {len(provenance["files"])} originais, 7 resultados bilíngues, 10 prompts, transcriçêo, ZIP e links de {len(pages)} páginas.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-manifest',action='store_true')
    args=parser.parse_args()
    verify()
    if args.write_manifest:
        manifest=[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files()]
        (ROOT/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        print(f'Manifesto atualizado: {len(manifest)} arquivos.')
    else:
        manifest=json.loads((ROOT/'MANIFEST.json').read_text())
        assert {x['path'] for x in manifest}=={p.relative_to(ROOT).as_posix() for p in files()}, 'Manifesto desatualizado: lista de arquivos'
        for item in manifest:
            p=ROOT/item['path']
            assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256'], f'Manifesto desatualizado: {item["path"]}'
        print(f'Manifesto conferido: {len(manifest)} arquivos.')

if __name__=='__main__':main()
