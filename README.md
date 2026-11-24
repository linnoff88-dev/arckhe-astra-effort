# Astra Effort â€” guia em portuguÃªs

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

[![Astra Effort: nÃ­veis de esforÃ§o na prÃ¡tica](capa/capa.png)](https://linnoff88-dev.github.io/

**[Abrir o guia de uso](https://linnoff88-dev.github.io/ Â· **[Ler o guia completo](https://linnoff88-dev.github.io/ Â· **[Baixar o PDF em portuguÃªs](Astra-Effort-Guia-pt-BR.pdf)**

EdiÃ§Ã£o em portuguÃªs do **GPT-6 Astra Effort Super Guide**, de Mark Kashef / Early AI Dopters: sete primeiras tentativas documentadas, dez prompts reutilizÃ¡veis, quadros editÃ¡veis e um mÃ©todo para comparar nÃ­veis de esforÃ§o no seu trabalho.

O projeto reÃºne a traduÃ§Ã£o do kit e materiais complementares enviados pelo usuÃ¡rio. Os resultados sÃ£o do experimento original de 7 de setembro de 2026, com pesquisa encerrada em 8 de setembro. A traduÃ§Ã£o nÃ£o executa novamente os testes nem revalida preÃ§os ou funcionalidades.

## Comece aqui

1. Leia [START-HERE.md](START-HERE.md) e o [guia completo em portuguÃªs](SUPER-GUIDE.md).
2. Escolha um dos [dez prompts](PROMPTS.md) e adapte os campos Ã  sua tarefa.
3. Compare os [resultados em portuguÃªs â€” CSV](evidence/results.pt-BR.csv) ou [JSON](evidence/results.pt-BR.json).
4. Consulte as [verificaÃ§Ãµes do produtor](evidence/PRODUCER-CHECKS.md) antes de tirar conclusÃµes.
5. Registre um teste prÃ³prio usando [experiment/YOUR-RUN-LOG.csv](experiment/YOUR-RUN-LOG.csv).

Medium foi a preferÃªncia inicial do autor **para esta tarefa de pesquisa e construÃ§Ã£o**. Tempos sÃ£o observaÃ§Ãµes individuais; tokens processados incluem entrada em cache e **nÃ£o representam custo financeiro**. Ultra foi a condiÃ§Ã£o com delegaÃ§Ã£o habilitada.

**Ver tambÃ©m:** [EsforÃ§o na prÃ¡tica](https://linnoff88-dev.github.io/ no repositÃ³rio `modelos`. A pÃ¡gina cruza estes dados com um teste do Claude Opus 5.5 por nÃ­vel de esforÃ§o. Ã‰ uma referÃªncia externa e nÃ£o altera esta traduÃ§Ã£o.

## Biblioteca

| Caminho | ConteÃºdo e idioma |
| --- | --- |
| [guia/](guia/) | PÃ¡gina pÃºblica e cinco pÃ¡ginas de leitura em portuguÃªs |
| [SUPER-GUIDE.md](SUPER-GUIDE.md) | Guia completo traduzido |
| [Astra-Effort-Guia-pt-BR.pdf](Astra-Effort-Guia-pt-BR.pdf) | PDF da traduÃ§Ã£o |
| [PROMPTS.md](PROMPTS.md) e [prompts/](prompts/) | Dez modelos de prompt em portuguÃªs |
| [SOURCE-NOTES.md](SOURCE-NOTES.md) | Oito complementos com fontes, traduzidos |
| [experiment/](experiment/) | Enunciado e condiÃ§Ãµes traduzidos; quadro e cabeÃ§alhos originais |
| [evidence/](evidence/) | ExplicaÃ§Ãµes em portuguÃªs, dados bilÃ­ngues e capturas originais |
| [canvases/](canvases/) | Sete planos originais editÃ¡veis em Excalidraw, em inglÃªs |
| [docs/](docs/) | Planilha XLSX, resumo, transcriÃ§Ã£o traduzida, referÃªncia visual e glossÃ¡rio |
| [original-en/](original-en/) | Kit descompactado e transcriÃ§Ã£o originais em inglÃªs |
| [files/](files/) | PDF e ZIP originais em inglÃªs |
| [source/](source/) | ApresentaÃ§Ã£o, metadados e procedÃªncia da importaÃ§Ã£o |

## PortuguÃªs e inglÃªs

Textos de estudo, explicaÃ§Ãµes e prompts estÃ£o em portuguÃªs. Comandos, nomes prÃ³prios, identificadores como `reasoning.effort`, chaves JSON/CSV e nomes de configuraÃ§Ãµes como `low`, `medium` e `xhigh` permanecem em inglÃªs. PDF original, capturas, quadros e dados brutos foram preservados para auditoria.

O [glossÃ¡rio da traduÃ§Ã£o](docs/TRADUCAO.md) explica as escolhas e os campos dos dados. Os resumos, planilha e referÃªncia visual enviados pelo usuÃ¡rio trazem aproximaÃ§Ãµes e interpretaÃ§Ãµes prÃ³prias; para comparar, use os nÃºmeros exatos e limites do guia original traduzido.

## Uso local

NÃ£o hÃ¡ dependÃªncias para ler o material nem para servir os arquivos jÃ¡ gerados:

```bash
git clone https://github.com/linnoff88-dev/astra-effort.git
cd astra-effort
python3 -m http.server 8000
```

Abra `http://localhost:8000/guia/`. Para editar os quadros, abra os arquivos `.excalidraw` no Excalidraw.

Para regenerar as pÃ¡ginas de leitura apÃ³s editar os documentos:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_docs.py
```

O PDF em portuguÃªs foi gerado a partir de `guia/leitura.html` com Chromium, em A4; a pÃ¡gina tambÃ©m tem estilos de impressÃ£o para exportar pelo navegador. O HTML da landing Ã© mantido diretamente em `guia/index.html`. O GitHub Pages publica os arquivos estÃ¡ticos por [.github/workflows/pages.yml](.github/workflows/pages.yml).

## Integridade e origem

```bash
python3 scripts/verify.py
```

Depois de alteraÃ§Ãµes intencionais, atualize o manifesto e confira novamente:

```bash
python3 scripts/verify.py --write-manifest
python3 scripts/verify.py
```

- [Pasta original no GitHub](https://github.com/earlyaidopters/gumroad-resources/tree/ecfbc2cc3d212672404d346043e47e492fb30198/resources/gpt-6-astra-effort-super-guide).
- Commit de origem: `ecfbc2cc3d212672404d346043e47e492fb30198`.
- ImportaÃ§Ã£o e traduÃ§Ã£o: 10 de setembro de 2026.
- [source/provenance.json](source/provenance.json): registro dos 45 arquivos importados, com hashes anteriores Ã  traduÃ§Ã£o.
- [original-en/MANIFEST.json](original-en/MANIFEST.json): manifesto original do kit.
- [MANIFEST.json](MANIFEST.json): manifesto da ediÃ§Ã£o atual.

Os documentos em `source/` sÃ£o cÃ³pias da apresentaÃ§Ã£o original; seus links relativos refletem a estrutura de origem. Use o Ã­ndice acima para navegar nesta ediÃ§Ã£o. A autoria e os direitos dos materiais originais permanecem com seus respectivos titulares.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>