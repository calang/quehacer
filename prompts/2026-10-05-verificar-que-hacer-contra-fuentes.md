# Verificar el contenido de que-hacer.md contra sus fuentes
Creado el 2026-10-05

## Pregunta

revisa el contenido del archivo que-hacer.md y compáralo con el mencionado en las fuentes, dentro del mismo archivo, para comprobarlo. Corrige cualquier incorformidad en el contenido del archivo con la información de las fuentes.

## Respuesta

Revisé `docs/que-hacer.md` contra cada fuente que cita y corregí lo que no coincidía. La infografía y los datos de la Municipalidad están bien (el sitio carga las preguntas frecuentes y el directorio por JavaScript, así que los consulté directamente).

**Correcciones**
- **Choque sin heridos:** la fuente no dice nada de «15 minutos» ni del número del INS (800-800-8000), así que los quité. Reescribí los pasos según el Pacto Amistoso que describe la fuente: solo dos vehículos, sin motocicletas, bicicletas ni peatones, con el responsable asegurado y con acuerdo de ambas partes.
- **Sismo:** la nota de la CNE que se cita no dice «agáchese, cúbrase y sujétese» ni «use el teléfono solo para emergencias». Puse lo que sí dice: alejarse de ventanas y espejos, no usar ascensores, ir al punto de reunión, conocer las llaves de agua y gas y preparar el kit con su contenido.
- **SENASA:** el 2587-1600, el correo info@senasa.go.cr y el horario no aparecen en la fuente. Los cambié por el trámite que describe: descargar el formulario de senasa.go.cr y entregarlo en una oficina regional, o enviarlo en línea con firma digital.
- **Ministerio de Salud:** el 4003-5000 no es WhatsApp (el sitio solo tiene un canal informativo) y la fuente no menciona ninguna app «Denuncia Salud». Lo cambié por el teléfono, el correo y el formulario digital del sitio. Confirmé el correo denuncias.minsa@misalud.go.cr.
- **CNFL:** en la página citada el 1026 aparece solo dentro de un comentario del código. Agregué como fuente la página de medios de atención, que sí dice «1026, disponible 24 horas», y cambié «la app» por el formulario en línea.
- **PANI:** agregué el horario del WhatsApp 8989-1147 (L-V de 7:30 a.m. a 4 p.m.), con fuente.
- **Robo de vivienda:** ajusté el texto a la guía del Poder Judicial: delegación del OIJ más cercana a su domicilio (en San José, la Oficina de Recepción de Denuncias) y la Fiscalía si sabe quién fue.
- **Gas:** cambié «llave del regulador» por «llave de paso del gas».
- **Enlaces caídos:** quité dos páginas del OIJ que dan error 404 y reemplacé el PDF de Bomberos, que también daba 404, por su página sobre gas LPG.
- **Fechas:** actualicé la fecha de verificación y la de la lista de fuentes a 2026-10-05.

**Agregué a «Conviene revisar»:** no pude confirmar el horario de la Línea 1147 del PANI, porque su sitio bloquea el acceso automatizado. Tampoco pude abrir la página nueva de Bomberos: los consejos sobre gas coinciden con lo que muestra el buscador sobre esa página, no con la página misma.

**Sin cambios:** las afirmaciones generales que ninguna fuente confirma pero tampoco contradicen, como que el 9-1-1 es gratuito.

Los cambios no están en un commit; puedes verlos con `git diff docs/que-hacer.md`.

Fuentes adicionales consultadas:
- [CNFL – Medios de atención](https://www.cnfl.go.cr/contacto/medios-atencion)
- [crhoy – WhatsApp del PANI](https://www.crhoy.com/pani-habilita-numero-para-atender-denuncias-y-dudas-de-adolescentes/)
- [La Nación – PANI](https://www.nacion.com/el-pais/servicios/pani-atendera-denuncias-por-violencia-contra-ninos/QZ6K2UG47BCI5GI7G45QXHRTIA/story/)
- [Bomberos – Gas LPG](https://www.bomberos.go.cr/7-evitemos-los-incidentes-con-gas-licuado-de-petroleo/)
