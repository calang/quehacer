// Búsqueda con resaltado: no distingue mayúsculas ni tildes.
(function () {
  'use strict';

  var MINIMO = 2;
  var contenido = document.getElementById('contenido');
  var consulta = document.getElementById('consulta');
  var contador = document.getElementById('contador');
  var marcas = [];
  var activa = -1;

  // Devuelve el texto sin tildes y en minúsculas, y para cada carácter
  // resultante el índice del carácter original del que proviene.
  function normalizar(texto) {
    var plano = '';
    var origen = [];
    for (var i = 0; i < texto.length; i++) {
      var base = texto[i].normalize('NFD').replace(/[̀-ͯ]/g, '')
        .toLowerCase();
      for (var j = 0; j < base.length; j++) {
        plano += base[j];
        origen.push(i);
      }
    }
    return { plano: plano, origen: origen };
  }

  function limpiar() {
    marcas.forEach(function (marca) {
      marca.replaceWith(document.createTextNode(marca.textContent));
    });
    contenido.normalize();
    marcas = [];
    activa = -1;
  }

  function resaltarNodo(nodo, buscado) {
    var texto = normalizar(nodo.nodeValue);
    var rangos = [];
    var desde = texto.plano.indexOf(buscado);
    while (desde !== -1) {
      var hasta = desde + buscado.length - 1;
      rangos.push([texto.origen[desde], texto.origen[hasta] + 1]);
      desde = texto.plano.indexOf(buscado, desde + buscado.length);
    }
    // De atrás hacia adelante, para que los índices previos sigan válidos.
    for (var k = rangos.length - 1; k >= 0; k--) {
      var rango = document.createRange();
      rango.setStart(nodo, rangos[k][0]);
      rango.setEnd(nodo, rangos[k][1]);
      rango.surroundContents(document.createElement('mark'));
    }
  }

  function activar(indice) {
    if (activa >= 0) {
      marcas[activa].classList.remove('activa');
    }
    activa = (indice + marcas.length) % marcas.length;
    marcas[activa].classList.add('activa');
    marcas[activa].scrollIntoView({ block: 'center' });
    contador.textContent = (activa + 1) + ' de ' + marcas.length;
  }

  function buscar() {
    limpiar();
    var buscado = normalizar(consulta.value.trim()).plano;
    if (buscado.length < MINIMO) {
      contador.textContent = '';
      return;
    }
    var recorrido = document.createTreeWalker(contenido, NodeFilter.SHOW_TEXT);
    var nodos = [];
    while (recorrido.nextNode()) {
      nodos.push(recorrido.currentNode);
    }
    nodos.forEach(function (nodo) { resaltarNodo(nodo, buscado); });
    marcas = Array.prototype.slice.call(contenido.querySelectorAll('mark'));
    if (marcas.length === 0) {
      contador.textContent = 'Sin resultados';
    } else {
      activar(0);
    }
  }

  function mover(paso) {
    if (marcas.length > 0) {
      activar(activa + paso);
    }
  }

  consulta.addEventListener('input', buscar);
  consulta.addEventListener('keydown', function (evento) {
    if (evento.key === 'Enter') {
      evento.preventDefault();
      mover(evento.shiftKey ? -1 : 1);
    } else if (evento.key === 'Escape') {
      consulta.value = '';
      buscar();
    }
  });
  document.getElementById('buscador').addEventListener('submit', function (e) {
    e.preventDefault();
  });
  document.getElementById('anterior').addEventListener('click', function () {
    mover(-1);
  });
  document.getElementById('siguiente').addEventListener('click', function () {
    mover(1);
  });
}());
