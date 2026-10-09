# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este proyecto

Una guía en español para que los vecinos de Curridabat (Costa Rica) sepan qué hacer y a quién avisar ante actividad sospechosa, emergencias, daños y otras situaciones. El entregable principal es `docs/que-hacer.md`. Por ahora no hay código: `src/`, `scripts/` y `tests/` están vacíos.

El objetivo de la próxima etapa está en `specs/roadmap.md` (Fase 1): generar a partir del Markdown un HTML con estilo básico y búsqueda por palabras clave. Las secciones "Misión" y "A quién servimos" de `specs/mission.md` no se cambian sin una discusión y una aprobación explícitas.

## Comandos

```bash
make init                                        # primera vez: crea .env desde .env_template y ejecuta uv sync (incluye el grupo dev)
make update-env                                  # uv sync
make lint                                        # pylint sobre scripts/ y src/ (pylintrc: Google Python Style Guide)
uv run pytest                                    # todas las pruebas (testpaths = tests)
uv run pytest tests/path/test_foo.py::test_name  # una sola prueba
```

Para los ambientes solo se usa uv (`pyproject.toml` + `uv.lock`); no hay conda.

## Cómo editar `docs/que-hacer.md`

- **Estructura:** primero una fecha de verificación y los párrafos generales (cómo llamar al 9-1-1, cuándo no llamar, regla general sobre denuncias). Después viene una sola tabla de dos columnas. Al final están las secciones `## Fuentes consultadas (AAAA-MM-DD)`, `## Notas` y `## Créditos`.
- **Formato de la tabla:** cada categoría es una fila con el título en negrita y la segunda celda vacía. Los pasos van numerados dentro de la celda (`1. ...<br>2. ...`). Teléfonos, correos y nombres de instituciones van en **negrita**, y las direcciones web sin protocolo, en *cursiva*.
- **Tono:** se trata al lector de "usted", con frases cortas e imperativas.
- **Fuentes:** todo dato (número, horario, trámite) debe salir de una fuente citada en "Fuentes consultadas", de preferencia institucional. Si cambian las fuentes o se vuelven a verificar, actualiza las fechas del encabezado y de esa sección. Lo que no se pudo confirmar va en "Notas", no en la tabla.
- **Hechos ya establecidos:** Curridabat no tiene Policía Municipal general, solo Policía de Tránsito Municipal, así que no la menciones. Las denuncias formales se presentan ante el OIJ o la Fiscalía; una llamada al 9-1-1 no es una denuncia.
- `docs/archive/` guarda documentos fuente primarios (infografía de la Red de Seguridad Distrital, minuta). Se citan, no se editan.

## Registro de sesiones con IA

Cada sesión relevante se guarda en `prompts/AAAA-MM-DD-<tema>.md` con el formato `# Título`, `Creado el AAAA-MM-DD` y pares `## Pregunta` / `## Respuesta`. Usa los archivos existentes como modelo. Si cambias el modelo o la forma de producir la guía, actualiza los créditos de `README.md` y de `docs/que-hacer.md`.
