ï»¿# Astra Effort ê¢â¬â guia em portuguêÂªs

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

[![Astra Effort: nêÂ­veis de esforêÂ§o na prêÂ¡tica](capa/capa.png)](https://linnoff88-dev.github.io/

**[Abrir o guia de uso](https://linnoff88-dev.github.io/ êÂ· **[Ler o guia completo](https://linnoff88-dev.github.io/ êÂ· **[Baixar o PDF em portuguêÂªs](Astra-Effort-Guia-pt-BR.pdf)**

EdiêÂ§êÂ£o em portuguêÂªs do **GPT-6 Astra Effort Super Guide**, de Mark Kashef / Early AI Dopters: sete primeiras tentativas documentadas, dez prompts reutilizêÂ¡veis, quadros editêÂ¡veis e um mêÂ©todo para comparar nêÂ­veis de esforêÂ§o no seu trabalho.

O projeto reêÂºne a traduêÂ§êÂ£o do kit e materiais complementares enviados pelo usuêÂ¡rio. Os resultados sêÂ£o do experimento original de 7 de setembro de 2026, com pesquisa encerrada em 8 de setembro. A traduêÂ§êÂ£o nêÂ£o executa novamente os testes nem revalida preêÂ§os ou funcionalidades.

## Comece aqui

1. Leia [START-HERE.md](START-HERE.md) e o [guia completo em portuguêÂªs](SUPER-GUIDE.md).
2. Escolha um dos [dez prompts](PROMPTS.md) e adapte os campos êÂ  sua tarefa.
3. Compare os [resultados em portuguêÂªs ê¢â¬â CSV](evidence/results.pt-BR.csv) ou [JSON](evidence/results.pt-BR.json).
4. Consulte as [verificaêÂ§êÂµes do produtor](evidence/PRODUCER-CHECKS.md) antes de tirar conclusêÂµes.
5. Registre um teste prêÂ³prio usando [experiment/YOUR-RUN-LOG.csv](experiment/YOUR-RUN-LOG.csv).

Medium foi a preferêÂªncia inicial do autor **para esta tarefa de pesquisa e construêÂ§êÂ£o**. Tempos sêÂ£o observaêÂ§êÂµes individuais; tokens processados incluem entrada em cache e **nêÂ£o representam custo financeiro**. Ultra foi a condiêÂ§êÂ£o com delegaêÂ§êÂ£o habilitada.

**Ver tambêÂ©m:** [EsforêÂ§o na prêÂ¡tica](https://linnoff88-dev.github.io/ no repositêÂ³rio `modelos`. A pêÂ¡gina cruza estes dados com um teste do Claude Opus 5.5 por nêÂ­vel de esforêÂ§o. êâ° uma referêÂªncia externa e nêÂ£o altera esta traduêÂ§êÂ£o.

## Biblioteca

| Caminho | ConteêÂºdo e idioma |
| --- | --- |
| [guia/](guia/) | PêÂ¡gina pêÂºblica e cinco pêÂ¡ginas de leitura em portuguêÂªs |
| [SUPER-GUIDE.md](SUPER-GUIDE.md) | Guia completo traduzido |
| [Astra-Effort-Guia-pt-BR.pdf](Astra-Effort-Guia-pt-BR.pdf) | PDF da traduêÂ§êÂ£o |
| [PROMPTS.md](PROMPTS.md) e [prompts/](prompts/) | Dez modelos de prompt em portuguêÂªs |
| [SOURCE-NOTES.md](SOURCE-NOTES.md) | Oito complementos com fontes, traduzidos |
| [experiment/](experiment/) | Enunciado e condiêÂ§êÂµes traduzidos; quadro e cabeêÂ§alhos originais |
| [evidence/](evidence/) | ExplicaêÂ§êÂµes em portuguêÂªs, dados bilêÂ­ngues e capturas originais |
| [canvases/](canvases/) | Sete planos originais editêÂ¡veis em Excalidraw, em inglêÂªs |
| [docs/](docs/) | Planilha XLSX, resumo, transcriêÂ§êÂ£o traduzida, referêÂªncia visual e glossêÂ¡rio |
| [original-en/](original-en/) | Kit descompactado e transcriêÂ§êÂ£o originais em inglêÂªs |
| [files/](files/) | PDF e ZIP originais em inglêÂªs |
| [source/](source/) | ApresentaêÂ§êÂ£o, metadados e procedêÂªncia da importaêÂ§êÂ£o |

## PortuguêÂªs e inglêÂªs

Textos de estudo, explicaêÂ§êÂµes e prompts estêÂ£o em portuguêÂªs. Comandos, nomes prêÂ³prios, identificadores como `reasoning.effort`, chaves JSON/CSV e nomes de configuraêÂ§êÂµes como `low`, `medium` e `xhigh` permanecem em inglêÂªs. PDF original, capturas, quadros e dados brutos foram preservados para auditoria.

O [glossêÂ¡rio da traduêÂ§êÂ£o](docs/TRADUCAO.md) explica as escolhas e os campos dos dados. Os resumos, planilha e referêÂªncia visual enviados pelo usuêÂ¡rio trazem aproximaêÂ§êÂµes e interpretaêÂ§êÂµes prêÂ³prias; para comparar, use os nêÂºmeros exatos e limites do guia original traduzido.

## Uso local

NêÂ£o hêÂ¡ dependêÂªncias para ler o material nem para servir os arquivos jêÂ¡ gerados:

```bash
git clone https://github.com/linnoff88-dev/astra-effort.git
cd astra-effort
python3 -m http.server 8000
```

Abra `http://localhost:8000/guia/`. Para editar os quadros, abra os arquivos `.excalidraw` no Excalidraw.

Para regenerar as pêÂ¡ginas de leitura apêÂ³s editar os documentos:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_docs.py
```

O PDF em portuguêÂªs foi gerado a partir de `guia/leitura.html` com Chromium, em A4; a pêÂ¡gina tambêÂ©m tem estilos de impressêÂ£o para exportar pelo navegador. O HTML da landing êÂ© mantido diretamente em `guia/index.html`. O GitHub Pages publica os arquivos estêÂ¡ticos por [.github/workflows/pages.yml](.github/workflows/pages.yml).

## Integridade e origem

```bash
python3 scripts/verify.py
```

Depois de alteraêÂ§êÂµes intencionais, atualize o manifesto e confira novamente:

```bash
python3 scripts/verify.py --write-manifest
python3 scripts/verify.py
```

- [Pasta original no GitHub](https://github.com/earlyaidopters/gumroad-resources/tree/ecfbc2cc3d212672404d346043e47e492fb30198/resources/gpt-6-astra-effort-super-guide).
- Commit de origem: `ecfbc2cc3d212672404d346043e47e492fb30198`.
- ImportaêÂ§êÂ£o e traduêÂ§êÂ£o: 10 de setembro de 2026.
- [source/provenance.json](source/provenance.json): registro dos 45 arquivos importados, com hashes anteriores êÂ  traduêÂ§êÂ£o.
- [original-en/MANIFEST.json](original-en/MANIFEST.json): manifesto original do kit.
- [MANIFEST.json](MANIFEST.json): manifesto da ediêÂ§êÂ£o atual.

Os documentos em `source/` sêÂ£o cêÂ³pias da apresentaêÂ§êÂ£o original; seus links relativos refletem a estrutura de origem. Use o êÂ­ndice acima para navegar nesta ediêÂ§êÂ£o. A autoria e os direitos dos materiais originais permanecem com seus respectivos titulares.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>