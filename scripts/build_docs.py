#!/usr/bin/env python3
"""Gera as pêÂ¡ginas de leitura a partir das traduêÂ§êÂµes; requer Python-Markdown."""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, quote
import re
import markdown

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    'SUPER-GUIDE.md': ('leitura.html', 'Guia completo'),
    'PROMPTS.md': ('prompts.html', 'Dez prompts para usar'),
    'SOURCE-NOTES.md': ('fontes.html', 'Notas e fontes'),
    'evidence/PRODUCER-CHECKS.md': ('revisao.html', 'VerificaêÂ§êÂµes do produtor'),
    'docs/Texto colado(20260910-165842).txt': ('transcricao.html', 'TranscriêÂ§êÂ£o do vêÂ­deo'),
}
landing = (ROOT / 'guia/index.html').read_text()
style = re.search(r'<style>(.*?)</style>', landing, re.S).group(1)
script = re.search(r'<script>(.*?)</script>', landing, re.S).group(1)
nav = re.search(r'<a class="skip".*?</nav>', landing, re.S).group(0)
nav = nav.replace('href="#resultados"', 'href="./#resultados"').replace('href="#guia"', 'href="./#guia"').replace('href="#materiais"', 'href="./#materiais"')
reader_style = '''
.reader{max-width:78ch;padding:40px 22px 70px;margin:auto;overflow-wrap:anywhere}.reader h1{font-size:clamp(2rem,4vw,3rem);margin:28px 0}.reader h2{font-size:1.7rem;margin:2.6em 0 .7em;scroll-margin-top:100px}.reader h3{margin:1.8em 0 .6em}.reader p,.reader li{line-height:1.85}.reader a{text-decoration:underline;text-underline-offset:3px}.reader table{display:block;overflow:auto;font-size:.88rem}.reader pre{white-space:pre-wrap;line-height:1.7}.toc{background:var(--bg2);padding:20px 24px;border:1px solid var(--line);border-radius:12px}.toc ul{padding-left:20px}.reader .back{font-family:Sora;font-size:.9rem}.reader details{margin:28px 0}.reader summary{cursor:pointer;font-weight:600}.reader blockquote{margin-left:0;padding:4px 20px;border-left:1px solid var(--amb)}
@media print{nav,.skip,.back,.toc,footer,.reader>details{display:none}body,body.light{background:#fff!important;color:#111!important;font-size:10pt;color-scheme:light}.reader{max-width:none;padding:0}.reader h1{font-size:26pt}.reader h2{font-size:17pt;break-after:avoid}.reader h3{break-after:avoid}.reader pre{background:#f4f4f4!important;color:#111!important;border-color:#ddd;font-size:8pt;break-inside:auto}.reader a{color:#333}.reader table{display:table;font-size:8pt}.reader th,.reader td{white-space:normal;color:#111;border-color:#ddd;padding:7px;background:#fff}.reader tr{break-inside:avoid}a[href]:after{content:none}}
'''

def fix_links(body, source):
    def replace(match):
        url=match.group(1)
        parts=urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            return match.group(0)
        target=(ROOT / source).parent.joinpath(unquote(parts.path)).resolve()
        if not target.is_relative_to(ROOT):
            return match.group(0)
        relative=target.relative_to(ROOT).as_posix()
        dest=PAGES[relative][0] if relative in PAGES else '../'+quote(relative, safe='/')
        if parts.fragment:
            dest += '#'+parts.fragment
        return 'href="'+escape(dest,quote=True)+'"'
    return re.sub(r'href="([^"]+)"',replace,body)

for source,(filename,title) in PAGES.items():
    text=(ROOT/source).read_text()
    if source.endswith('.txt'):
        lines=text.splitlines()
        text='# '+lines[0]+'\n\n'+'\n\n'.join(lines[1:])
    parser=markdown.Markdown(extensions=['tables','fenced_code','toc'])
    content=fix_links(parser.convert(text),source)
    toc='<details><summary>Nesta pêÂ¡gina</summary>'+parser.toc+'</details>'
    doc=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)} ê¢â¬â Astra Effort</title><meta name="description" content="{escape(title)} do kit Astra Effort em portuguêÂªs."><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap"><style>{style}{reader_style}</style></head><body>{nav}<main id="conteudo" class="reader"><a class="back" href="./">ê¢â Â Biblioteca Astra Effort</a>{toc}{content}</main><footer><a href="./">Voltar êÂ  biblioteca</a> êÂ· <a href="https://ARCKHê AI">ARCKHê AI</a></footer><script>{script}</script></body></html>'''
    (ROOT/'guia'/filename).write_text(doc)
    print(filename)
