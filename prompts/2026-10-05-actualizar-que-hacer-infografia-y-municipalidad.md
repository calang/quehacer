# Actualizar que-hacer.md con la infografía de seguridad y el sitio de la Municipalidad de Curridabat
Creado el 2026-10-05

## Pregunta 1

lee e interpreta el contenido del archivo docs/archive/llamadas_de_emergencia_CyP_Curri.jpeg.  Revisa el contenido de docs/que-hacer.md y corrígelo o complétalo con esta nueva información. déjalo en el mismo sitio, para revisar los cambios.

## Respuesta 1

Actualicé `docs/que-hacer.md` en el mismo sitio. Los cambios no están confirmados en git; puedes verlos con `git diff docs/que-hacer.md`.

**Qué dice la imagen:** es una infografía de la Red de Seguridad Distrital de Curridabat y la Fuerza Pública. Cubre cuatro temas:
- **9-1-1:** cuándo llamar y cuándo no, y cómo debe ser la llamada.
- **Reportar un hecho:** al Centro de Información Confidencial (CICO) del OIJ.
- **Denunciar un delito:** ante la Fiscalía (Ministerio Público) o el OIJ.
- **Drogas:** la Policía de Control de Drogas atiende venta, almacenamiento y distribución en el **1176** y en un formulario en línea.

**Cambios en la guía:**
1. **Llamada al 9-1-1:** la dirección ahora se da como provincia, cantón, distrito, barrio y señas. Añadí que hay que responder las preguntas del operador y que la llamada dura al menos 20 segundos.
2. **Nuevo párrafo "No llame al 9-1-1":** por extravío de documentos o del celular, para consultar teléfonos de instituciones, por congestión vial, por problemas en servicios públicos ni para pedir asistencia en carretera.
3. **Regla general sobre denuncias:**
   - De preferencia se presentan en la Fiscalía más cercana al lugar del hecho o al domicilio.
   - Cualquier persona puede denunciar, sin importar su edad o nacionalidad.
   - En el OIJ no se pide ningún requisito.
   - La Oficina de Recepción de Denuncias del OIJ en San José atiende 24 horas, todos los días.
4. **Drogas:** añadí el 1176 y el formulario en línea como vía principal para la actividad recurrente. La línea del OIJ queda como alternativa.
5. **Nueva fila en "Otras situaciones":** información sobre delitos ya cometidos y sobre personas requeridas, prófugas o desaparecidas, que se reporta al CICO del OIJ.
6. **Vehículo sospechoso:** agregué la forma 800-8000-OIJ al número del OIJ.
7. **Fuentes:** añadí la infografía.
8. **"Conviene revisar":**
   - Quité el pendiente del 1176, porque la infografía lo confirma.
   - Quité el WhatsApp del OIJ de la lista de datos que solo venían de la prensa. La infografía lo confirma (8-8000-645 es el mismo 8800-0645).
   - Agregué al punto sobre denuncia formal que la infografía la respalda.

**Para revisar:**
- **Teléfono de la Policía Municipal (2272-0724):** sigue pendiente. La infografía no lo menciona.
- **Persona desaparecida:** en la fila nueva la mandé al CICO, como indica la infografía. En la práctica, la desaparición de un familiar suele denunciarse directamente ante el OIJ, así que conviene revisar esa redacción.

## Pregunta 2

elimina las referencias en que-hacer.md, a la Policía Municipal de Curridabat, ya que esta ya no existe.  revisa que en los casos en los que se elimine esa referencia quede algún otro sitio con el cual hacer contacto.  si no es así, anota el faltante entre cosas por revisar.

## Respuesta 2

Quité de `docs/que-hacer.md` todas las referencias a la Policía Municipal de Curridabat y a su número (2272-0724).

**Situaciones afectadas.** Las cuatro siguen teniendo a quién llamar, porque el 9-1-1 ya aparecía junto a la Policía Municipal:
- Persona desconocida merodeando: 9-1-1, y avisar al comité de seguridad comunitaria del barrio.
- Vehículo sospechoso: 9-1-1 y la línea confidencial del OIJ.
- Escándalo o ruido excesivo: 9-1-1 si está ocurriendo y Ministerio de Salud si es recurrente.
- Vandalismo en curso: 9-1-1.

**Lo que falta.** Ahora no queda ningún contacto policial local para casos que no son urgentes; varios de estos dependen solo del 9-1-1. Lo anoté en «Conviene revisar»: habría que añadir el teléfono de la delegación de la Fuerza Pública de Curridabat, que no encontré porque su página daba error 404.

**Otros ajustes.**
- En la lista de fuentes quité «y Policía Municipal» de la línea de la Municipalidad.
- El pendiente sobre la Policía Municipal en «Conviene revisar» ya no tenía sentido. En su lugar quedó un punto para confirmar el teléfono de la Municipalidad (2216-5200), que solo encontré en un directorio de terceros (munis.cr).

Puedes ver los cambios con `git diff docs/que-hacer.md`.

## Pregunta 3

como fuente de información sobre la Municipalidad de Curridabat utiliza https://www.curridabat.go.cr/ en lugar de https://www.munis.cr/municipalidad-de-curridabat.  revisa el contenido de la nueva referencia, para actualizar o completar el contenido de que-hacer.md según corresponda.

## Respuesta 3

Cambié la fuente de la Municipalidad de Curridabat a su sitio oficial, https://www.curridabat.go.cr/, y completé `docs/que-hacer.md` con lo que encontré ahí. Ya no queda ninguna referencia a munis.cr. La portada del sitio casi no tiene datos; los contactos salen del pie de página, del directorio y de las preguntas frecuentes.

**Datos confirmados.** El teléfono 2216-5200 es correcto. Quité el pendiente que pedía confirmarlo. También quité el horario «L-V de 7:30 a 4:30», porque el sitio oficial no lo publica.

**Contactos nuevos por situación:**
- **Daños a bienes públicos** (aceras, huecos en calles municipales, señales, alcantarillas obstruidas o sin tapa, luminarias de parques): servicios.plataforma@curridabat.go.cr o el 2216-5200. Por correo hay que adjuntar firma digital o una nota firmada a mano, y se asigna un número de seguimiento.
- **Árbol o ramas peligrosas** en un espacio público, cuando no es urgente: el mismo correo de plataforma.
- **Inundación o deslizamiento** sin riesgo inminente: gestion.riesgo@curridabat.go.cr. Sustituye al «llame a la Municipalidad» del deslizamiento.
- **Maltrato animal:** bienestaranimal@curridabat.go.cr, además de SENASA.
- **Basura y animales muertos** en calles, parques o lotes: gestion.residuos@curridabat.go.cr. Un lote abandonado lleno de residuos se reporta al correo de plataforma.
- **Fila nueva, uso inapropiado de parques o espacios públicos:** 9-1-1 si está ocurriendo; si es recurrente, Cultura de Paz (culturadepaz@curridabat.go.cr, 2216-5324).
- **Fila nueva, casa abandonada:** Inspecciones de la Municipalidad, teléfonos 2216-5295, 5296, 5297 o 5299.

**Lo que no agregué.** Las preguntas frecuentes también dan un correo de la Policía de Tránsito Municipal (transito.municipal@curridabat.go.cr). Lo dejé fuera porque dijiste que la Policía Municipal ya no existe y no sé si Tránsito Municipal sigue operando. Si me lo confirmas, se puede añadir en la fila del vehículo sospechoso o abandonado.

El pendiente de un contacto policial local para casos no urgentes sigue abierto en «Conviene revisar». Los cambios no están confirmados en git; puedes verlos con `git diff docs/que-hacer.md`.

## Pregunta 4

"Policía Municipal" (de carácter general) no existe en Curridabat, pero si hay una Policía de Tránsito.  Agrega las referencias a esta última en donde proceda.

## Respuesta 4

Agregué la Policía de Tránsito Municipal (transito.municipal@curridabat.go.cr) en `docs/que-hacer.md`:

- **Vehículo desconocido estacionado mucho tiempo:** nuevo paso 4. Si parece abandonado o está mal estacionado y no hay indicios de delito, se reporta a Tránsito Municipal.
- **Fila nueva, vehículo mal estacionado que obstruye una entrada, la acera o la vía:** fotografiar el vehículo y la placa y reportarlo a Tránsito Municipal. Si impide el paso de una ambulancia o pone en riesgo a personas, llamar al 9-1-1.
- **«Conviene revisar»:** corregí la redacción para decir que Curridabat no tiene Policía Municipal de carácter general, solo de Tránsito. Agregué un punto nuevo: el sitio oficial solo da el correo de Tránsito Municipal; no tiene teléfono y no aparece en el directorio.

Dejé igual las filas de accidente con heridos y choque sin heridos, que siguen enviando al 9-1-1 y a «Tránsito». No sé si Tránsito Municipal atiende colisiones o solo estacionamiento; si las atiende, se puede mencionar ahí también.
