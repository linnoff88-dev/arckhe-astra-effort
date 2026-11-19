# Astra Effort — guía en portugués

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Astra Effort: niveles de esfuerzo en la práctica](capa/capa.png)](https://inematds.github.io/astra-effort/guia/es/)

**[Abrir la guía de uso](https://inematds.github.io/astra-effort/guia/es/)** · **[Leer la guía completa](https://inematds.github.io/astra-effort/guia/es/leitura.html)** · **[Descargar el PDF en portugués](Astra-Effort-Guia-pt-BR.pdf)**

Edición en portugués de **GPT-6 Astra Effort Super Guide**, de Mark Kashef / Early AI Dopters: siete primeros intentos documentados, diez prompts reutilizables, cuadros editables y un método para comparar niveles de esfuerzo en tu trabajo.

El proyecto reúne la traducción del kit y materiales complementarios enviados por el usuario. Los resultados corresponden al experimento original del 7 de septiembre de 2026, cuya investigación concluyó el 8 de septiembre. La traducción no vuelve a ejecutar las pruebas ni revalida precios o funcionalidades.

## Empieza aquí

1. Lee [START-HERE.md](START-HERE.md) y la [guía completa en portugués](SUPER-GUIDE.md).
2. Elige uno de los [diez prompts](PROMPTS.md) y adapta los campos a tu tarea.
3. Compara los [resultados en portugués — CSV](evidence/results.pt-BR.csv) o [JSON](evidence/results.pt-BR.json).
4. Consulta las [verificaciones del productor](evidence/PRODUCER-CHECKS.md) antes de sacar conclusiones.
5. Registra una prueba propia usando [experiment/YOUR-RUN-LOG.csv](experiment/YOUR-RUN-LOG.csv).

Medium fue la preferencia inicial del autor **para esta tarea de investigación y desarrollo**. Los tiempos son observaciones individuales; los tokens procesados incluyen entradas en caché y **no representan un costo financiero**. Ultra fue la condición con delegación habilitada.

**Consulta también:** [Esfuerzo en la práctica](https://inematds.github.io/modelos/guia/esforco/), en el repositorio `modelos`. La página cruza estos datos con una prueba de Claude Opus 5.5 por nivel de esfuerzo. Es una referencia externa y no modifica esta traducción.

## Biblioteca

| Ruta | Contenido e idioma |
| --- | --- |
| [guia/](guia/) | Página pública y cinco páginas de lectura en portugués |
| [SUPER-GUIDE.md](SUPER-GUIDE.md) | Guía completa traducida |
| [Astra-Effort-Guia-pt-BR.pdf](Astra-Effort-Guia-pt-BR.pdf) | PDF de la traducción |
| [PROMPTS.md](PROMPTS.md) y [prompts/](prompts/) | Diez plantillas de prompts en portugués |
| [SOURCE-NOTES.md](SOURCE-NOTES.md) | Ocho complementos con fuentes, traducidos |
| [experiment/](experiment/) | Enunciado y condiciones traducidos; cuadro y encabezados originales |
| [evidence/](evidence/) | Explicaciones en portugués, datos bilingües y capturas originales |
| [canvases/](canvases/) | Siete planes originales editables en Excalidraw, en inglés |
| [docs/](docs/) | Hoja de cálculo XLSX, resumen, transcripción traducida, referencia visual y glosario |
| [original-en/](original-en/) | Kit descomprimido y transcripción originales en inglés |
| [files/](files/) | PDF y ZIP originales en inglés |
| [source/](source/) | Presentación, metadatos y procedencia de la importación |

## Portugués e inglés

Los textos de estudio, las explicaciones y los prompts están en portugués. Los comandos, nombres propios, identificadores como `reasoning.effort`, claves JSON/CSV y nombres de configuraciones como `low`, `medium` y `xhigh` permanecen en inglés. El PDF original, las capturas, los cuadros y los datos sin procesar se conservaron para auditoría.

El [glosario de la traducción](docs/TRADUCAO.md) explica las decisiones y los campos de los datos. Los resúmenes, la hoja de cálculo y la referencia visual enviados por el usuario incluyen aproximaciones e interpretaciones propias; para comparar, usa las cifras exactas y los límites de la guía original traducida.

## Uso local

No se necesitan dependencias para leer el material ni para servir los archivos ya generados:

```bash
git clone https://github.com/inematds/astra-effort.git
cd astra-effort
python3 -m http.server 8000
```

Abre `http://localhost:8000/guia/`. Para editar los cuadros, abre los archivos `.excalidraw` en Excalidraw.

Para volver a generar las páginas de lectura después de editar los documentos:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_docs.py
```

El PDF en portugués se generó a partir de `guia/leitura.html` con Chromium, en A4; la página también incluye estilos de impresión para exportarla desde el navegador. El HTML de la página de inicio se mantiene directamente en `guia/index.html`. GitHub Pages publica los archivos estáticos mediante [.github/workflows/pages.yml](.github/workflows/pages.yml).

## Integridad y origen

```bash
python3 scripts/verify.py
```

Después de hacer cambios intencionales, actualiza el manifiesto y vuelve a verificar:

```bash
python3 scripts/verify.py --write-manifest
python3 scripts/verify.py
```

- [Carpeta original en GitHub](https://github.com/earlyaidopters/gumroad-resources/tree/ecfbc2cc3d212672404d346043e47e492fb30198/resources/gpt-6-astra-effort-super-guide).
- Commit de origen: `ecfbc2cc3d212672404d346043e47e492fb30198`.
- Importación y traducción: 10 de septiembre de 2026.
- [source/provenance.json](source/provenance.json): registro de los 45 archivos importados, con hashes anteriores a la traducción.
- [original-en/MANIFEST.json](original-en/MANIFEST.json): manifiesto original del kit.
- [MANIFEST.json](MANIFEST.json): manifiesto de la edición actual.

Los documentos en `source/` son copias de la presentación original; sus enlaces relativos reflejan la estructura de origen. Usa el índice anterior para navegar por esta edición. La autoría y los derechos de los materiales originales siguen perteneciendo a sus respectivos titulares.
