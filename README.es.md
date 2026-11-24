# Astra Effort â€” guÃ­a en portuguÃ©s

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

[![Astra Effort: niveles de esfuerzo en la prÃ¡ctica](capa/capa.png)](https://linnoff88-dev.github.io/

**[Abrir la guÃ­a de uso](https://linnoff88-dev.github.io/ Â· **[Leer la guÃ­a completa](https://linnoff88-dev.github.io/ Â· **[Descargar el PDF en portuguÃ©s](Astra-Effort-Guia-pt-BR.pdf)**

EdiciÃ³n en portuguÃ©s de **GPT-6 Astra Effort Super Guide**, de Mark Kashef / Early AI Dopters: siete primeros intentos documentados, diez prompts reutilizables, cuadros editables y un mÃ©todo para comparar niveles de esfuerzo en tu trabajo.

El proyecto reÃºne la traducciÃ³n del kit y materiales complementarios enviados por el usuario. Los resultados corresponden al experimento original del 7 de septiembre de 2026, cuya investigaciÃ³n concluyÃ³ el 8 de septiembre. La traducciÃ³n no vuelve a ejecutar las pruebas ni revalida precios o funcionalidades.

## Empieza aquÃ­

1. Lee [START-HERE.md](START-HERE.md) y la [guÃ­a completa en portuguÃ©s](SUPER-GUIDE.md).
2. Elige uno de los [diez prompts](PROMPTS.md) y adapta los campos a tu tarea.
3. Compara los [resultados en portuguÃ©s â€” CSV](evidence/results.pt-BR.csv) o [JSON](evidence/results.pt-BR.json).
4. Consulta las [verificaciones del productor](evidence/PRODUCER-CHECKS.md) antes de sacar conclusiones.
5. Registra una prueba propia usando [experiment/YOUR-RUN-LOG.csv](experiment/YOUR-RUN-LOG.csv).

Medium fue la preferencia inicial del autor **para esta tarea de investigaciÃ³n y desarrollo**. Los tiempos son observaciones individuales; los tokens procesados incluyen entradas en cachÃ© y **no representan un costo financiero**. Ultra fue la condiciÃ³n con delegaciÃ³n habilitada.

**Consulta tambiÃ©n:** [Esfuerzo en la prÃ¡ctica](https://linnoff88-dev.github.io/ en el repositorio `modelos`. La pÃ¡gina cruza estos datos con una prueba de Claude Opus 5.5 por nivel de esfuerzo. Es una referencia externa y no modifica esta traducciÃ³n.

## Biblioteca

| Ruta | Contenido e idioma |
| --- | --- |
| [guia/](guia/) | PÃ¡gina pÃºblica y cinco pÃ¡ginas de lectura en portuguÃ©s |
| [SUPER-GUIDE.md](SUPER-GUIDE.md) | GuÃ­a completa traducida |
| [Astra-Effort-Guia-pt-BR.pdf](Astra-Effort-Guia-pt-BR.pdf) | PDF de la traducciÃ³n |
| [PROMPTS.md](PROMPTS.md) y [prompts/](prompts/) | Diez plantillas de prompts en portuguÃ©s |
| [SOURCE-NOTES.md](SOURCE-NOTES.md) | Ocho complementos con fuentes, traducidos |
| [experiment/](experiment/) | Enunciado y condiciones traducidos; cuadro y encabezados originales |
| [evidence/](evidence/) | Explicaciones en portuguÃ©s, datos bilingÃ¼es y capturas originales |
| [canvases/](canvases/) | Siete planes originales editables en Excalidraw, en inglÃ©s |
| [docs/](docs/) | Hoja de cÃ¡lculo XLSX, resumen, transcripciÃ³n traducida, referencia visual y glosario |
| [original-en/](original-en/) | Kit descomprimido y transcripciÃ³n originales en inglÃ©s |
| [files/](files/) | PDF y ZIP originales en inglÃ©s |
| [source/](source/) | PresentaciÃ³n, metadatos y procedencia de la importaciÃ³n |

## PortuguÃ©s e inglÃ©s

Los textos de estudio, las explicaciones y los prompts estÃ¡n en portuguÃ©s. Los comandos, nombres propios, identificadores como `reasoning.effort`, claves JSON/CSV y nombres de configuraciones como `low`, `medium` y `xhigh` permanecen en inglÃ©s. El PDF original, las capturas, los cuadros y los datos sin procesar se conservaron para auditorÃ­a.

El [glosario de la traducciÃ³n](docs/TRADUCAO.md) explica las decisiones y los campos de los datos. Los resÃºmenes, la hoja de cÃ¡lculo y la referencia visual enviados por el usuario incluyen aproximaciones e interpretaciones propias; para comparar, usa las cifras exactas y los lÃ­mites de la guÃ­a original traducida.

## Uso local

No se necesitan dependencias para leer el material ni para servir los archivos ya generados:

```bash
git clone https://github.com/linnoff88-dev/astra-effort.git
cd astra-effort
python3 -m http.server 8000
```

Abre `http://localhost:8000/guia/`. Para editar los cuadros, abre los archivos `.excalidraw` en Excalidraw.

Para volver a generar las pÃ¡ginas de lectura despuÃ©s de editar los documentos:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build_docs.py
```

El PDF en portuguÃ©s se generÃ³ a partir de `guia/leitura.html` con Chromium, en A4; la pÃ¡gina tambiÃ©n incluye estilos de impresiÃ³n para exportarla desde el navegador. El HTML de la pÃ¡gina de inicio se mantiene directamente en `guia/index.html`. GitHub Pages publica los archivos estÃ¡ticos mediante [.github/workflows/pages.yml](.github/workflows/pages.yml).

## Integridad y origen

```bash
python3 scripts/verify.py
```

DespuÃ©s de hacer cambios intencionales, actualiza el manifiesto y vuelve a verificar:

```bash
python3 scripts/verify.py --write-manifest
python3 scripts/verify.py
```

- [Carpeta original en GitHub](https://github.com/earlyaidopters/gumroad-resources/tree/ecfbc2cc3d212672404d346043e47e492fb30198/resources/gpt-6-astra-effort-super-guide).
- Commit de origen: `ecfbc2cc3d212672404d346043e47e492fb30198`.
- ImportaciÃ³n y traducciÃ³n: 10 de septiembre de 2026.
- [source/provenance.json](source/provenance.json): registro de los 45 archivos importados, con hashes anteriores a la traducciÃ³n.
- [original-en/MANIFEST.json](original-en/MANIFEST.json): manifiesto original del kit.
- [MANIFEST.json](MANIFEST.json): manifiesto de la ediciÃ³n actual.

Los documentos en `source/` son copias de la presentaciÃ³n original; sus enlaces relativos reflejan la estructura de origen. Usa el Ã­ndice anterior para navegar por esta ediciÃ³n. La autorÃ­a y los derechos de los materiales originales siguen perteneciendo a sus respectivos titulares.
