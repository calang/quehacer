# Plan — Fase 1: Versión inicial consumible de la guía

## 1. Dependencias y comandos

1. Agregar `markdown` a `dependencies` en `pyproject.toml` (`uv add markdown`) y actualizar `uv.lock`.
2. Agregar al `Makefile` el target `html` (`uv run python -m src.build_html`) e incluirlo en `.PHONY`.

## 2. Conversión de Markdown a HTML

1. Crear `src/__init__.py` y `src/build_html.py`.
2. Escribir la función `render_body(markdown_text: str) -> str`, que convierte con Python-Markdown y la extensión `tables`.
3. Hacer que los enlaces externos se abran con `target="_blank" rel="noopener"`, mediante una extensión pequeña o un posprocesamiento del HTML.
4. Marcar las filas de categoría (primera celda en negrita y segunda vacía) con la clase `categoria`.

## 3. Página autocontenida

1. Crear la plantilla `src/templates/guia.html` con `lang="es"`, `meta viewport`, `<title>` tomado del primer `#` y los lugares donde van el CSS, el JS y el cuerpo.
2. Crear `src/templates/guia.css`: tipografía del sistema, ancho legible, tabla apilada por debajo de unos 640 px, filas de categoría como subtítulos, estilos de `mark` y `mark.activa`, y barra de búsqueda fija.
3. Escribir la función `build_page(markdown_text: str) -> str`, que inserta el cuerpo, el CSS y el JS en línea en la plantilla.
4. Escribir la función `main()`, que lee `docs/que-hacer.md`, crea `dist/` y escribe `dist/que-hacer.html`. Las rutas de entrada y salida son argumentos opcionales con valores por omisión.

## 4. Búsqueda con resaltado

1. Crear `src/templates/buscar.js`, en JS nativo, que recorra los nodos de texto del contenido con `TreeWalker`.
2. Normalizar el texto para comparar (NFD, sin diacríticos, en minúsculas) y conservar el mapeo de índices al texto original, para resaltar el fragmento correcto.
3. Envolver las coincidencias en `<mark>`, contarlas y llevar el índice de la coincidencia activa.
4. Conectar los controles: búsqueda al escribir (desde 2 caracteres), botones "Anterior" y "Siguiente", Enter y Shift+Enter, Escape para limpiar y el contador "n de m" o "Sin resultados" (con `aria-live`).
5. Antes de cada búsqueda nueva, quitar los resaltados anteriores y unir los nodos de texto con `normalize()`.

## 5. Pruebas

1. Crear `tests/test_build_html.py` con pruebas de `render_body` y `build_page` (ver `validation.md`).
2. Agregar una prueba que genere la página a partir de `docs/que-hacer.md` y compruebe que es autocontenida.

## 6. Documentación

1. Actualizar `specs/tech-stack.md`: lenguaje, Front-end (HTML, CSS y JS estático, sin frameworks), dependencia `markdown` y filas que no aplican.
2. Agregar `make html` a "Comandos comunes" en `README.md` y a "Comandos" en `.claude/CLAUDE.md`.
3. Marcar como hechas las funcionalidades de la Fase 1 en `specs/roadmap.md`.
