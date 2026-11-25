ï»¿# Astra Effort ê¢â¬â guêÂ­a en portuguêÂ©s

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

[![Astra Effort: niveles de esfuerzo en la prêÂ¡ctica](capa/capa.png)](https://linnoff88-dev.github.io/

**[Abrir la guêÂ­a de uso](https://linnoff88-dev.github.io/ êÂ· **[Leer la guêÂ­a completa](https://linnoff88-dev.github.io/ êÂ· **[Descargar el PDF en portuguêÂ©s](Astra-Effort-Guia-pt-BR.pdf)**

EdiciêÂ³n en portuguêÂ©s de **GPT-6 Astra Effort Super Guide**, de Mark Kashef / Early AI Dopters: siete primeros intentos documentados, diez prompts reutilizables, cuadros editables y un mêÂ©todo para comparar niveles de esfuerzo en tu trabajo.

El proyecto reêÂºne la traducciêÂ³n del kit y materiales complementarios enviados por el usuario. Los resultados corresponden al experimento original del 7 de septiembre de 2026, cuya investigaciêÂ³n concluyêÂ³ el 8 de septiembre. La traducciêÂ³n no vuelve a ejecutar las pruebas ni revalida precios o funcionalidades.

## Empieza aquêÂ­

1. Lee [START-HERE.md](START-HERE.md) y la [guêÂ­a completa en portuguêÂ©s](SUPER-GUIDE.md).
2. Elige uno de los [diez prompts](PROMPTS.md) y adapta los campos a tu tarea.
3. Compara los [resultados en portuguêÂ©s ê¢â¬â CSV](evidence/results.pt-BR.csv) o [JSON](evidence/results.pt-BR.json).
4. Consulta las [verificaciones del productor](evidence/PRODUCER-CHECKS.md) antes de sacar conclusiones.
5. Registra una prueba propia usando [experiment/YOUR-RUN-LOG.csv](experiment/YOUR-RUN-LOG.csv).

Medium fue la preferencia inicial del autor **para esta tarea de investigaciêÂ³n y desarrollo**. Los tiempos son observaciones individuales; los tokens procesados incluyen entradas en cachêÂ© y **no representan un costo financiero**. Ultra fue la condiciêÂ³n con delegaciêÂ³n habilitada.

**Consulta tambiêÂ©n:** [Esfuerzo en la prêÂ¡ctica](https://linnoff88-dev.github.io/ en el repositorio `modelos`. La pêÂ¡gina cruza estos datos con una prueba de Claude Opus 5.5 por nivel de esfuerzo. Es una referencia externa y no modifica esta traducciêÂ³n.

## Biblioteca

| Ruta | Contenido e idioma |
| --- | --- |
| [guia/](guia/) | PêÂ¡gina pêÂºblica y cinco pêÂ¡ginas de lectura en portuguêÂ©s |
| [SUPER-GUIDE.md](SUPER-GUIDE.md) | GuêÂ­a completa traducida |
| [Astra-Effort-Guia-pt-BR.pdf](Astra-Effort-Guia-pt-BR.pdf) | PDF de la traducciêÂ³n |
| [PROMPTS.md](PROMPTS.md) y [prompts/](prompts/) | Diez plantillas de prompts en portuguêÂ©s |
| [SOURCE-NOTES.md](SOURCE-NOTES.md) | Ocho complementos con fuentes, traducidos |
| [experiment/](experiment/) | Enunciado y condiciones traducidos; cuadro y encabezados originales |
| [evidence/](evidence/) | Explicaciones en portuguêÂ©s, datos bilingêÂ¼es y capturas originales |
| [canvases/](canvases/) | Siete planes originales editables en Excalidraw, en inglêÂ©s |
| [docs/](docs/) | Hoja de cêÂ¡lculo XLSX, resumen, transcripciêÂ³n traducida, referencia visual y glosario |
| [original-en/](original-en/) | Kit descomprimido y transcripciêÂ³n originales en inglêÂ©s |
| [files/](files/) | PDF y ZIP originales en inglêÂ©s |
| [source/](source/) | PresentaciêÂ³n, metadatos y procedencia de la importaciêÂ³n |

## PortuguêÂ©s e inglêÂ©s

Los textos de estudio, las explicaciones y los prompts estêÂ¡n en portuguêÂ©s. Los comandos, nombres propios, identificadores como `reasoning.effort`, claves JSON/CSV y nombres de configuraciones como `low`, `medium` y `xhigh` permanecen en inglêÂ©s. El PDF original, las capturas, los cuadros y los datos sin procesar se conservaron para auditorêÂ­a.

El [glosario de la traducciêÂ³n](docs/TRADUCAO.md) explica las decisiones y los campos de los datos. Los resêÂºmenes, la hoja de cêÂ¡lculo y la referencia visual enviados por el usuario incluyen aproximaciones e interpretaciones propias; para comparar, usa las cifras exactas y los lêÂ­mites de la guêÂ­a original traducida.

## Uso local

No se necesitan dependencias para leer el material ni para servir los archivos ya generados:

```bash
git clone https://github.com/linnoff88-dev/astra-effort.git
cd astra-effort
python3 -m http.server 8000
```

Abre `http://localhost:8000/guia/`. Para editar los cuadros, abre los archivos `.excalidraw` en Excalidraw.

Para volver a generar las pêÂ¡ginas de lectura despuêÂ©s de editar los documentos:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_docs.py
```

El PDF en portuguêÂ©s se generêÂ³ a partir de `guia/leitura.html` con Chromium, en A4; la pêÂ¡gina tambiêÂ©n incluye estilos de impresiêÂ³n para exportarla desde el navegador. El HTML de la pêÂ¡gina de inicio se mantiene directamente en `guia/index.html`. GitHub Pages publica los archivos estêÂ¡ticos mediante [.github/workflows/pages.yml](.github/workflows/pages.yml).

## Integridad y origen

```bash
python3 scripts/verify.py
```

DespuêÂ©s de hacer cambios intencionales, actualiza el manifiesto y vuelve a verificar:

```bash
python3 scripts/verify.py --write-manifest
python3 scripts/verify.py
```

- [Carpeta original en GitHub](https://github.com/earlyaidopters/gumroad-resources/tree/ecfbc2cc3d212672404d346043e47e492fb30198/resources/gpt-6-astra-effort-super-guide).
- Commit de origen: `ecfbc2cc3d212672404d346043e47e492fb30198`.
- ImportaciêÂ³n y traducciêÂ³n: 10 de septiembre de 2026.
- [source/provenance.json](source/provenance.json): registro de los 45 archivos importados, con hashes anteriores a la traducciêÂ³n.
- [original-en/MANIFEST.json](original-en/MANIFEST.json): manifiesto original del kit.
- [MANIFEST.json](MANIFEST.json): manifiesto de la ediciêÂ³n actual.

Los documentos en `source/` son copias de la presentaciêÂ³n original; sus enlaces relativos reflejan la estructura de origen. Usa el êÂ­ndice anterior para navegar por esta ediciêÂ³n. La autorêÂ­a y los derechos de los materiales originales siguen perteneciendo a sus respectivos titulares.
