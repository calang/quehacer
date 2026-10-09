# Tech Stack

[Descripción general].

## Core

Cada fila es un componente típico de un proyecto. Si no aplica, borra la fila; si aplica, complétala con la elección y la razón.

| Layer                    | Choice                             | Rationale |
|--------------------------|-------------------------------------|-----------|
| Language                 | Python 3.14 (gestionado con `uv`)   | _..._     |
| Front-end                | _..._                                | _..._     |
| Backend / API framework  | _..._                                | _..._     |
| Data Base                | _..._                                | _..._     |
| Data Storage (archivos)  | _..._                                | _..._     |
| Data Retrieval / Search  | _..._                                | _..._     |
| ML / Modelos             | _..._                                | _..._     |
| Content Quality / Validación | _..._                            | _..._     |
| CI/CD Tools              | _..._                                | _..._     |
| Deployment tools         | _..._                                | _..._     |


## Data

[Descripción general].


## Testing

- **pytest** (`uv run pytest`) para el código Python
- **pylint** (`make lint`, con `pylintrc` que implementa la Google Python Style Guide) para calidad de código Python


## Tooling

- **uv** para gestión de dependencias y entorno virtual (`make init`, `make update-env`, `make rm-env`)
- **Makefile** como interfaz de comandos comunes
- **Jupyter Lab** (`make jupl`) para exploración/experimentación
- Variables de entorno en `.env` (`PROJECT_ROOT`, `PYTHONPATH`, ...), cargadas automáticamente por el `.bashrc` del proyecto


## What We Are Not Using

[Opcional: documentar decisiones explícitas de no usar cierta tecnología y por qué.]
