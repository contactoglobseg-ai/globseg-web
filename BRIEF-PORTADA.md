# Brief de superficie — Portada (seguridadgarridos)

Alcance: portada (index.html). Modo de visitante: **Persuade**.
Audiencia elegida: empresas, industria y bodegas (jefes de operaciones y prevención).
Acción: dejar nombre, teléfono y qué hay que cuidar, para que la empresa contacte.
Cambio 08-10-2026 (pedido del usuario): la captación reemplaza al WhatsApp saliente.
Ya no se le pide al visitante que escriba; el sitio toma sus datos y la empresa llama.
Proceso: no se ejecutó el lanzador `impeccable` (binario descargado); se siguió la vía
documentada de leer el contexto del proyecto y las referencias directamente. Sin
concept-seed, por lo tanto sin seed key y sin comps: build **code-led**.

## Direction contract

**THESIS.** La portada es la bitácora del turno, no un folleto. Lo que se vende no es
"confianza": es que cada turno queda escrito con hora, punto, novedad y firma. Rechaza
el arreglo por defecto del rubro: hero partido con texto a un lado y escudo al otro,
sobre una grilla de cuatro tarjetas iguales de icono + título + párrafo.

**OWN-WORLD.** Tinta azul marino de la marca (#130052) como fondo dominante y papel de
planilla verdoso pálido (#E7EBE3) como las superficies mayores donde se lee. Las rayas
del papel son reales (es un libro de registro), la raya de margen es el degradado
verde-cian del logo usado como estructura, nunca como acento decorativo. Display
condensado que recuerda el letrado del escudo; cuerpo grotesco con cifras tabulares
para las horas. Elevación declarada una vez: papel con sombra, paneles con filete de
1px. Tema único comprometido (fondo oscuro, lectura sobre papel claro), elegido por la
escena de uso: se decide de día, en oficina de planta o en el teléfono.

**STORY.** Un jefe de operaciones entiende en segundos que puede tomar guardias, rondas
y cámaras con una empresa que documenta el turno; cree que el puesto no queda a la
improvisación porque ve el registro y los procedimientos que ya existen firmados; actúa
llenando una línea de bitácora que se va por WhatsApp.

**FIRST VIEWPORT.** Barra delgada: escudo y nombre a la izquierda, navegación y acción a
la derecha. Debajo, a la izquierda y a ~55% del ancho: titular condensado en tres líneas
que nombra la oferta, una línea que carga la tesis, y la acción en su forma de trabajo
— tres campos (nombre, teléfono, qué cuidar) que dejan el contacto, visible sin scroll. A la derecha, la hoja del libro de novedades con registros de ejemplo
rotulados, cortada por el borde inferior para que se lea que la página sigue como libro.
El escudo entra como timbre sobre la hoja, no como ilustración central.

**FORM.** Bitácora de turno (libro de novedades de conserjería), primera de mi lista
ordenada de siete candidatas del mundo del cliente. Descartadas por el rut del rubro:
sala de monitoreo y radio. Alternativas vivas: credencial OS-10, panel de faena.
Seed key: ninguna (concept-seed no se ejecutó; declarado arriba).

**FINISH.** unreviewed and undocumented is unfinished; this build ends with the finish
review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Pendiente del usuario (bloquea publicar, no revisar)
- Dónde llegan los datos del formulario (servicio de envío y su clave).
  Sin eso el formulario valida pero avisa que no está conectado.
- Teléfono y correo para quien prefiera llamar
- Zona de cobertura (comuna/región) — importa para Google y para el titular
- Confirmar credencial OS-10 del personal
- Confirmar el compromiso de reemplazo ante ausencia (hoy no se afirma en la página)
- Dominio
