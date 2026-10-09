#!/usr/bin/env python3
"""Genera una página HTML autocontenida a partir de la guía en Markdown.

Uso:
    python -m src.build_html [--source docs/que-hacer.md]
                             [--output dist/que-hacer.html]
"""

import argparse
import html
import logging
import re
import string
from pathlib import Path
from xml.etree import ElementTree

import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = Path(__file__).resolve().parent / 'templates'
DEFAULT_SOURCE = ROOT / 'docs' / 'que-hacer.md'
DEFAULT_OUTPUT = ROOT / 'dist' / 'que-hacer.html'

logger = logging.getLogger(__name__)


def _is_category_row(row: ElementTree.Element) -> bool:
    """Indica si una fila tiene solo un título en negrita y una celda vacía."""
    cells = list(row)
    if len(cells) != 2:
        return False
    title, steps = cells
    children = list(title)
    return (len(children) == 1 and children[0].tag == 'strong'
            and not (title.text or '').strip()
            and not (children[0].tail or '').strip()
            and not (steps.text or '').strip() and len(steps) == 0)


class _GuideTreeprocessor(Treeprocessor):
    """Marca las filas de categoría y abre los enlaces externos aparte."""

    def run(self, root):
        for element in root.iter():
            if element.tag == 'tr' and _is_category_row(element):
                element.set('class', 'categoria')
            elif (element.tag == 'a'
                  and element.get('href', '').startswith(('http://',
                                                          'https://'))):
                element.set('target', '_blank')
                element.set('rel', 'noopener')


class _GuideExtension(Extension):
    """Registra el procesador de la guía después de los enlaces en línea."""

    def extendMarkdown(self, md):  # pylint: disable=invalid-name
        md.treeprocessors.register(_GuideTreeprocessor(md), 'guia', 5)


def render_body(markdown_text: str) -> str:
    """Convierte el Markdown de la guía en el HTML del cuerpo.

    Args:
        markdown_text: Contenido Markdown de la guía.

    Returns:
        El fragmento HTML, con las filas de categoría marcadas con la clase
        ``categoria`` y los enlaces externos abiertos en otra pestaña.
    """
    return markdown.markdown(markdown_text,
                             extensions=['tables', _GuideExtension()])


def _title(markdown_text: str) -> str:
    """Devuelve el texto del primer encabezado de nivel 1, o uno genérico."""
    match = re.search(r'^#\s+(.+?)\s*$', markdown_text, re.MULTILINE)
    return match.group(1) if match else 'Guía'


def build_page(markdown_text: str) -> str:
    """Arma la página completa con el CSS y el JS en línea.

    Args:
        markdown_text: Contenido Markdown de la guía.

    Returns:
        El documento HTML autocontenido.
    """
    template = string.Template(
        (TEMPLATES / 'guia.html').read_text(encoding='utf-8'))
    return template.substitute(
        title=html.escape(_title(markdown_text)),
        style=(TEMPLATES / 'guia.css').read_text(encoding='utf-8'),
        script=(TEMPLATES / 'buscar.js').read_text(encoding='utf-8'),
        body=render_body(markdown_text),
    )


def main(argv: list[str] | None = None) -> None:
    """Lee la guía en Markdown y escribe la página HTML.

    Args:
        argv: Argumentos de línea de comandos; por omisión, los de sys.argv.
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)

    page = build_page(args.source.read_text(encoding='utf-8'))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding='utf-8')
    logger.info('Página generada: %s', args.output)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    main()
