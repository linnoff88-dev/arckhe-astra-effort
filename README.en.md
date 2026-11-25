# Astra Effort â€” guide in Portuguese

**ðŸ‡§ðŸ‡· [Português](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [Espaê±ol](README.es.md)**

[![Astra Effort: levels of effort in practice](capa/capa.png)](https://linnoff88-dev.github.io/

**[Open the user guide](https://linnoff88-dev.github.io/ Â· **[Read the full guide](https://linnoff88-dev.github.io/ Â· **[Download the PDF in Portuguese](Astra-Effort-Guia-pt-BR.pdf)**

Portuguese edition of the **GPT-6 Astra Effort Super Guide**, by Mark Kashef / Early AI Dopters: seven documented first attempts, ten reusable prompts, editable canvases, and a method for comparing effort levels in your work.

The project brings together the kitâ€™s translation and supplementary materials provided by the user. The results are from the original experiment of September 7, 2026, with research concluded on September 8. The translation does not rerun the tests or revalidate prices or features.

## Start here

1. Read [START-HERE.md](START-HERE.md) and the [full guide in Portuguese](SUPER-GUIDE.md).
2. Choose one of the [ten prompts](PROMPTS.md) and adapt the fields to your task.
3. Compare the [results in Portuguese â€” CSV](evidence/results.pt-BR.csv) or [JSON](evidence/results.pt-BR.json).
4. Consult the [producer's checks](evidence/PRODUCER-CHECKS.md) before drawing conclusions.
5. Record your own test using [experiment/YOUR-RUN-LOG.csv](experiment/YOUR-RUN-LOG.csv).

Medium was the author's initial preference **for this research and build task**. Times are individual observations; processed tokens include cached input and **do not represent financial cost**. Ultra was the condition with delegation enabled.

**See also:** [Effort in practice](https://linnoff88-dev.github.io/ in the `modelos` repository. The page cross-references these data with a Claude Opus 5.5 test at each effort level. It is an external reference and does not change this translation.

## Library

| Path | Content and language |
| --- | --- |
| [guia/](guia/) | Public page and five reading pages in Portuguese |
| [SUPER-GUIDE.md](SUPER-GUIDE.md) | Full translated guide |
| [Astra-Effort-Guia-pt-BR.pdf](Astra-Effort-Guia-pt-BR.pdf) | Translation PDF |
| [PROMPTS.md](PROMPTS.md) and [prompts/](prompts/) | Ten prompt templates in Portuguese |
| [SOURCE-NOTES.md](SOURCE-NOTES.md) | Eight translated supplements with sources |
| [experiment/](experiment/) | Translated prompt and conditions; original canvas and headings |
| [evidence/](evidence/) | Explanations in Portuguese, bilingual data, and original screenshots |
| [canvases/](canvases/) | Seven original editable plans in Excalidraw, in English |
| [docs/](docs/) | XLSX spreadsheet, summary, translated transcript, visual reference, and glossary |
| [original-en/](original-en/) | Original unzipped kit and transcript in English |
| [files/](files/) | Original PDF and ZIP in English |
| [source/](source/) | Presentation, metadata, and import provenance |

## Portuguese and English

Study texts, explanations, and prompts are in Portuguese. Commands, proper names, identifiers such as `reasoning.effort`, JSON/CSV keys, and configuration names such as `low`, `medium`, and `xhigh` remain in English. The original PDF, screenshots, canvases, and raw data were preserved for auditing.

The [translation glossary](docs/TRADUCAO.md) explains the translation choices and data fields. The summaries, spreadsheet, and visual reference provided by the user include their own approximations and interpretations; for comparison, use the exact figures and limits in the translated original guide.

## Local use

There are no dependencies for reading the material or serving the generated files:

```bash
git clone https://github.com/linnoff88-dev/astra-effort.git
cd astra-effort
python3 -m http.server 8000
```

Open `http://localhost:8000/guia/`. To edit the canvases, open the `.excalidraw` files in Excalidraw.

To regenerate the reading pages after editing the documents:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_docs.py
```

The Portuguese PDF was generated from `guia/leitura.html` with Chromium, in A4; the page also has print styles for exporting from the browser. The landing HTML is maintained directly in `guia/index.html`. GitHub Pages publishes the static files through [.github/workflows/pages.yml](.github/workflows/pages.yml).

## Integrity and origin

```bash
python3 scripts/verify.py
```

After intentional changes, update the manifest and check again:

```bash
python3 scripts/verify.py --write-manifest
python3 scripts/verify.py
```

- [Original folder on GitHub](https://github.com/earlyaidopters/gumroad-resources/tree/ecfbc2cc3d212672404d346043e47e492fb30198/resources/gpt-6-astra-effort-super-guide).
- Source commit: `ecfbc2cc3d212672404d346043e47e492fb30198`.
- Import and translation: September 10, 2026.
- [source/provenance.json](source/provenance.json): record of the 45 imported files, with hashes from before translation.
- [original-en/MANIFEST.json](original-en/MANIFEST.json): original kit manifest.
- [MANIFEST.json](MANIFEST.json): current edition manifest.

The documents in `source/` are copies of the original presentation; their relative links reflect the source structure. Use the index above to navigate this edition. Authorship and rights for the original materials remain with their respective holders.
