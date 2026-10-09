"""Pruebas de la generación de la página HTML de la guía."""

import re

import pytest

from src import build_html

TABLA = '''# Guía de prueba

| Situación | Pasos a seguir |
|---|---|
| **Categoría** | |
| Caso **con** negrita | 1. Llame al **9-1-1**.<br>2. Vea *sitio.go.cr*. |

Fuente: <https://ejemplo.org/pagina>
'''


@pytest.fixture(name='cuerpo')
def fixture_cuerpo():
    return build_html.render_body(TABLA)


@pytest.fixture(name='guia', scope='module')
def fixture_guia():
    return build_html.DEFAULT_SOURCE.read_text(encoding='utf-8')


def _filas(fragmento):
    return re.findall(r'<tr[^>]*>.*?</tr>', fragmento, re.DOTALL)


def test_tabla_se_convierte_en_table(cuerpo):
    assert '<table>' in cuerpo


def test_celdas_conservan_br_y_negritas(cuerpo):
    assert '<br>' in cuerpo
    assert '<strong>9-1-1</strong>' in cuerpo
    assert '<em>sitio.go.cr</em>' in cuerpo


def test_fila_de_categoria_tiene_clase(cuerpo):
    assert '<tr class="categoria">' in _filas(cuerpo)[1]


def test_filas_normales_no_tienen_clase(cuerpo):
    filas = _filas(cuerpo)
    assert 'categoria' not in filas[0]
    assert 'categoria' not in filas[2]


def test_enlace_externo_abre_en_otra_pestana(cuerpo):
    enlace = re.search(r'<a [^>]*href="https://ejemplo.org/pagina"[^>]*>',
                       cuerpo)
    assert enlace is not None
    assert 'target="_blank"' in enlace.group(0)
    assert 'rel="noopener"' in enlace.group(0)


def test_pagina_tiene_idioma_viewport_y_titulo():
    pagina = build_html.build_page(TABLA)
    assert '<html lang="es">' in pagina
    assert 'name="viewport"' in pagina
    assert '<title>Guía de prueba</title>' in pagina


def test_pagina_de_la_guia_es_autocontenida(guia):
    pagina = build_html.build_page(guia).lower()
    assert '<script src=' not in pagina
    assert '<link rel="stylesheet"' not in pagina
    assert 'cdn' not in pagina


def test_pagina_de_la_guia_tiene_cuadro_de_busqueda(guia):
    assert 'type="search"' in build_html.build_page(guia)


def test_pagina_de_la_guia_conserva_todas_las_filas(guia):
    lineas = [linea for linea in guia.splitlines()
              if linea.startswith('|') and not linea.startswith('|---')]
    assert len(_filas(build_html.render_body(guia))) == len(lineas)


def test_main_escribe_la_pagina(tmp_path):
    fuente = tmp_path / 'guia.md'
    fuente.write_text(TABLA, encoding='utf-8')
    salida = tmp_path / 'dist' / 'guia.html'
    build_html.main(['--source', str(fuente), '--output', str(salida)])
    assert '<title>Guía de prueba</title>' in salida.read_text(
        encoding='utf-8')
