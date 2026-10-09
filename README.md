# Que Hacer

Este repositorio contiene una guía de tareas y actividades que se deben realizar cuando se observe alguna actividad sospechosa o irregular en el barrio.

La finalidad es mantener la seguridad y el bienestar de la comunidad, promoviendo la colaboración entre los vecinos y las autoridades locales.

Está enfocado en las condiciones de seguridad y vigilancia dentro del cantón de Curridabat, en Costa Rica, pero puede ser adaptado a otras localidades según sea necesario.

Situaciones para las que se suministran instrucciones incluyen:
- Actividades sospechosas de personas desconocidas.
- Comportamientos inusuales de vecinos o visitantes.
- Incidentes de vandalismo o daños a la propiedad.
- Emergencias médicas o accidentes.
- Situaciones de emergencia relacionadas con el clima o desastres naturales.

La guía básica con los pasos a seguir en cada situación está en [docs/que-hacer.md](docs/que-hacer.md).

## Requisitos

Linux, MacOS o WSL con:

- Python 3.14+
- [`uv`](https://docs.astral.sh/uv/) (ver [docs/reference/uv-guide.md](docs/reference/uv-guide.md))

## Ambiente

- Primera vez: `make init` (crea `.env` desde `.env_template` y ejecuta `uv sync`).
- Variables de entorno en `.env`; `PYTHONPATH` apunta a `PROJECT_ROOT`.
- El `.bashrc` del proyecto carga `.env` y activa `.venv` (si `~/.bashrc` lo invoca).

## Comandos comunes

```bash
make help                                       # lista los targets del Makefile
make update-env                                 # uv sync
make rm-env                                     # borra .venv
make lint                                       # pylint (pylintrc: Google Python Style Guide)
make html                                       # genera dist/que-hacer.html desde docs/que-hacer.md
make jupl                                       # Jupyter Lab
uv run pytest                                   # todas las pruebas
uv run pytest tests/path/test_foo.py::test_name # una prueba
```

## Estándares de código

Definidos en el skill de Claude `python-standards`; linting configurado en `pylintrc`.

## Estructura del proyecto

```
- .claude/          # configuración de Claude Code
- data/             # datos
- docs/             # documentación (system_architecture.md, reference/)
- experiments/      # experimentos
- models/           # modelos
- prompts/          # prompts usados con agentes de IA
- scripts/          # scripts auxiliares
- specs/            # misión, hoja de ruta y tech stack
- src/              # código fuente
- tests/            # pruebas
- .bashrc           # inicialización de bash del proyecto
- .env_template     # plantilla de .env
- Makefile          # comandos comunes
- pyproject.toml    # dependencias (uv)
```

## Referencias

- [Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/short-courses/spec-driven-development-with-coding-agents)
