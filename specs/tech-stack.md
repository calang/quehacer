# Tech Stack

Un generador de sitio estático mínimo: la guía se edita en Markdown y un script de Python produce un único HTML autocontenido.

## Core

Cada fila es un componente típico de un proyecto. Si no aplica, borra la fila; si aplica, complétala con la elección y la razón.

| Layer                    | Choice                             | Rationale |
|--------------------------|-------------------------------------|-----------|
| Language                 | Python 3.14 (gestionado con `uv`)   | Scripts simples y fáciles de probar con pytest. |
| Front-end                | HTML, CSS y JS nativos en un solo archivo (`src/templates/`) | Funciona sin conexión, se descarga o comparte como un archivo y no depende de CDN ni frameworks. |
| Conversión Markdown → HTML | Python-Markdown (`markdown`, extensión `tables`) | Se instala con uv y se prueba con pytest; no depende de herramientas del sistema como pandoc. |
| Data Storage (archivos)  | Markdown en git (`docs/que-hacer.md`) | Formato editable, abierto y versionado. |
| Data Retrieval / Search  | Búsqueda en el navegador con resaltado (`buscar.js`) | La guía es pequeña; no requiere índice ni servidor. |
| CI/CD Tools              | _Pendiente (fase posterior)_        | _..._     |
| Deployment tools         | _Pendiente (fase posterior)_        | _..._     |


## Data

La fuente es `docs/que-hacer.md`; `make html` genera `dist/que-hacer.html`, que no se versiona.


## Testing

- **pytest** (`uv run pytest`) para el código Python
- **pylint** (`make lint`, con `pylintrc` que implementa la Google Python Style Guide) para calidad de código Python


## Tooling

- **uv** para gestión de dependencias y entorno virtual (`make init`, `make update-env`, `make rm-env`)
- **Makefile** como interfaz de comandos comunes
- **Jupyter Lab** (`make jupl`) para exploración/experimentación
- Variables de entorno en `.env` (`PROJECT_ROOT`, `PYTHONPATH`, ...), cargadas automáticamente por el `.bashrc` del proyecto


## What We Are Not Using

- Backend, base de datos ni modelos de ML: el resultado es un archivo estático.
- Frameworks o bibliotecas de JS y CDN: el HTML debe funcionar sin conexión.
- pandoc: evita depender de una herramienta instalada fuera de uv.
