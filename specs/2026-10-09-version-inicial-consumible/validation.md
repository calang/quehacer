# Validación — Fase 1: Versión inicial consumible de la guía

## Automática

- `uv run pytest` pasa.
- `make lint` no reporta errores en `src/`.
- `make html` genera `dist/que-hacer.html` sin errores.
- `tests/test_build_html.py` comprueba que:
  - una tabla Markdown se convierte en `<table>`, con los `<br>` y las negritas de las celdas preservados;
  - las filas de categoría reciben la clase `categoria` y las filas normales no;
  - los enlaces externos llevan `target="_blank"` y `rel="noopener"`;
  - la página tiene `lang="es"`, `meta viewport` y el `<title>` igual al primer encabezado;
  - la página generada desde `docs/que-hacer.md` no contiene `<script src=`, `<link rel="stylesheet"` ni URL de CDN, y sí contiene el cuadro de búsqueda;
  - el número de filas `<tr>` del cuerpo coincide con el de filas de la tabla Markdown.
- `specs/tech-stack.md` está actualizado con la dependencia `markdown` y el front-end estático.

## Manual

- **Recorrido:** abrir `dist/que-hacer.html` sin conexión, en un navegador de escritorio y en un celular (o con la emulación móvil del navegador).
  - La guía completa se ve: introducción, tabla, fuentes, notas y créditos.
  - En el celular la tabla se apila sin desplazamiento horizontal y las categorías se distinguen como subtítulos.
  - Los enlaces abren en una pestaña nueva.
- **Búsqueda:**
  - "policia" resalta "Policía" y "policía"; "9-1-1" resalta todas sus apariciones.
  - El contador muestra "n de m"; Siguiente y Anterior, y Enter y Shift+Enter, recorren las coincidencias de forma circular y desplazan la activa a la vista.
- **Casos límite:**
  - Una búsqueda de 1 carácter no resalta nada.
  - "xyz" muestra "Sin resultados".
  - Escape o vaciar el cuadro quitan todos los resaltados.
  - Buscar dos veces seguidas no deja `<mark>` anidados.
  - Una coincidencia que cruza una negrita (por ejemplo "llame al 9-1-1") se resalta al menos dentro de cada nodo de texto, sin romper el formato.
- **Accesibilidad básica:** el cuadro tiene etiqueta, los botones se pueden usar con el teclado y el contador se anuncia (`aria-live`).

## Tono

- Los textos de la interfaz están en español, tratan al lector de "usted" y son breves.
- El contenido del HTML es idéntico en información a `docs/que-hacer.md`.

## Definición de terminado

- Todas las comprobaciones automáticas pasan y el recorrido manual se completó sin defectos.
- `/quality-check` no reporta problemas.
- Las tres funcionalidades de la Fase 1 están marcadas `[x]` en `specs/roadmap.md`.
- README, `.claude/CLAUDE.md` y `specs/tech-stack.md` documentan `make html`.
