# Requisitos — Fase 1: Versión inicial consumible de la guía

## Alcance

Generar, a partir de `docs/que-hacer.md`, un único archivo HTML autocontenido con un estilo visual básico y una búsqueda que resalte las palabras clave.

**Incluye**
- Una conversión completa del Markdown a HTML: título, párrafos introductorios, la tabla de situaciones, "Fuentes consultadas", "Notas" y "Créditos".
- Una hoja de estilos incluida en el archivo, con encabezados, listas, enlaces y la tabla legibles en un celular.
- Un cuadro de búsqueda fijo en la parte superior que resalta las coincidencias, con navegación entre ellas.
- Un comando `make html` que regenera el archivo.

**No incluye**
- Publicación en línea (GitHub Pages u otro sitio) ni CI. Quedan para una fase posterior.
- Cambios en el contenido de `docs/que-hacer.md`.
- Otros formatos de descarga, como PDF.

### Comportamiento de la búsqueda

| Aspecto | Comportamiento |
|---|---|
| Entrada | Cuadro de texto con la etiqueta "Buscar en la guía". Busca a medida que se escribe, desde 2 caracteres. |
| Coincidencia | No distingue mayúsculas ni tildes: "policia" encuentra "Policía". La frase escrita se busca tal cual, como subcadena. |
| Resultado | Todas las coincidencias se envuelven en `<mark>`. La coincidencia activa tiene un estilo distinto y se desplaza a la vista. |
| Navegación | Botones "Anterior" y "Siguiente", más Enter y Shift+Enter. La navegación es circular. |
| Contador | Muestra "n de m" o "Sin resultados". |
| Limpiar | Al vaciar el cuadro o pulsar Escape se quitan todos los resaltados. |
| Alcance | Busca en el texto visible del contenido, pero no dentro del propio cuadro de búsqueda. |

## Decisiones

- **Conversor: Python-Markdown** (`markdown`, con la extensión `tables`). Se agrega como dependencia en `pyproject.toml`, lo que el usuario aprobó en la entrevista. Se eligió para que el proceso quede dentro de uv y se pueda probar con pytest, sin depender de herramientas del sistema como pandoc.
- **Búsqueda: resaltar coincidencias**, sin ocultar filas, para que el lector vea cada coincidencia en su contexto y siga teniendo la guía completa a la vista.
- **Salida autocontenida:** un solo `.html` con el CSS y el JS en línea, sin CDN ni fuentes externas. Funciona sin conexión y se puede descargar o compartir por WhatsApp.
- **Primero el celular:** en pantallas angostas, cada fila de la tabla se apila (situación arriba, pasos abajo) y las filas de categoría se ven como subtítulos.
- **Ubicación de la salida:** `dist/que-hacer.html`. Es un artefacto generado y `dist/` ya está en `.gitignore`.
- **JS sin bibliotecas:** JavaScript nativo, sin frameworks.

## Contexto

- **Idioma y tono:** todos los textos de la interfaz van en español y tratan al lector de "usted" ("Buscar en la guía", "Anterior", "Siguiente", "Sin resultados"), igual que la guía.
- **Contenido:** el HTML refleja fielmente el Markdown. El generador no agrega ni quita información de la guía. Las convenciones de formato de `docs/que-hacer.md` están en `.claude/CLAUDE.md`. El HTML debe mostrar bien los pasos numerados con `<br>` dentro de las celdas, las negritas y las cursivas.
- **Enlaces:** las URL entre `<...>` se convierten en enlaces que se abren en una pestaña nueva (`rel="noopener"`).
- **Stack:** Python 3.14 con uv; el código va en `src/`, las pruebas en `tests/` (pytest) y la calidad se revisa con `make lint` (pylintrc, Google Python Style Guide). Se siguen los estándares del skill `python-standards`.
- **Misión** (`specs/mission.md`): una guía fácil de usar, una versión descargable y la publicación automatizada desde un formato editable, con herramientas abiertas y sin costo.
