# Cómo conectar el formulario a la planilla de Google

Esto hay que hacerlo una sola vez. Son 7 pasos y toma unos 10 minutos.
Al final, cada persona que complete el formulario de la web aparece como una
fila nueva en tu planilla.

El script **no toca las pestañas que ya tengas**. Crea una pestaña nueva
llamada `Contactos` y escribe solo ahí.

---

## 1. Abre tu planilla

[Abrir la planilla](https://docs.google.com/spreadsheets/d/1xIjS2p7r3M_dif-DJCUe1LHWQHstwisNoCzvB6pe9F8/edit)

Su ID ya viene escrito en el código, así que no hay que configurarlo.

## 2. Abre el editor de script

En la barra de menús de la planilla: **Extensiones → Apps Script**.

Esa barra está arriba, debajo del nombre del archivo, y el orden es:
`Archivo · Editar · Ver · Insertar · Formato · Datos · Herramientas · Extensiones · Ayuda`.
"Extensiones" es la penúltima, justo antes de "Ayuda".

Se abre una pestaña nueva con un archivo que dice `function myFunction() {}`.

Si no aparece el menú:

- Tiene que ser en el **computador, en el navegador**. La app de Sheets del
  teléfono no tiene Apps Script.
- Si no se ve ninguna barra de menús, está plegada: hay una flecha `⌃` a la
  derecha del nombre del archivo, o presiona `Ctrl + Shift + F`.

### Alternativa, sin pasar por el menú

Como el ID de la planilla ya está escrito en el código, el script puede vivir
como proyecto aparte y funciona igual:

1. Entra a [script.google.com/home/projects](https://script.google.com/home/projects)
2. Botón **Nuevo proyecto**
3. Sigue desde el paso 3 de esta guía

## 3. Pega el código

Borra todo lo que aparece en ese archivo y pega el contenido completo de
`planilla-google.gs` (está en esta misma carpeta).

## 4. Pon el correo del aviso

Cerca del comienzo del código está:

```js
const CORREO_AVISO = "";
```

Escribe entre las comillas el correo de la empresa que debe recibir el aviso
de cada contacto nuevo. Por ejemplo:

```js
const CORREO_AVISO = "contacto@seguridadgarridos.cl";
```

Si lo dejas vacío, la fila se guarda igual en la planilla, solo que no llega
correo. Se puede agregar después.

> Si tu base de datos usa otro nombre de pestaña para los contactos, cámbialo
> en la línea siguiente (`const HOJA = "Contactos";`).

Guarda con el icono del disquete o `Cmd + S`.

## 5. Publica la conexión

1. Arriba a la derecha, botón azul **Implementar → Nueva implementación**.
2. Al lado de "Seleccionar tipo", haz clic en el engranaje y elige
   **Aplicación web**.
3. Llena así:
   - **Descripción:** `Formulario del sitio`
   - **Ejecutar como:** `Yo` (tu cuenta)
   - **Quién tiene acceso:** **Cualquier persona**
4. Botón **Implementar**.

> "Cualquier persona" es necesario: el formulario de la web entra sin estar
> conectado a tu cuenta de Google. Esa dirección solo permite **agregar**
> filas con el código que pegaste; no deja leer ni borrar tu planilla.

## 6. Autoriza el permiso

Google te va a pedir permiso la primera vez:

1. **Autorizar acceso** → elige tu cuenta.
2. Aparece una pantalla que dice "Google no ha verificado esta aplicación".
   Es normal, la aplicación eres tú. Haz clic en **Configuración avanzada** y
   después en **Ir a (nombre del proyecto) (no seguro)**.
3. **Permitir**.

## 7. Copia la dirección y mándamela

Al terminar, Google muestra una **URL de la aplicación web** que termina en
`/exec`. Se ve así:

```
https://script.google.com/macros/s/AKfycb.........../exec
```

Cópiala y mándamela. Yo la pego en la página, pruebo un envío de verdad y te
confirmo que la fila llegó.

Si quieres comprobarlo tú antes: pega esa dirección en el navegador. Debe
responder `{"ok":true,"mensaje":"Conexión activa"}`.

---

## Si después cambias el código

Cada vez que edites el script tienes que volver a publicar para que el cambio
tome efecto: **Implementar → Administrar implementaciones →** el lápiz de
editar **→ Versión: Nueva versión → Implementar**. La dirección `/exec` no
cambia, así que no hay que tocar la página.

## Qué columnas llegan

| Columna | De dónde sale |
|---|---|
| Fecha | La pone el script al recibir |
| Nombre | Formulario |
| Teléfono | Formulario |
| Empresa | Solo en el formulario completo |
| Comuna | Solo en el formulario completo |
| Qué hay que cuidar | Ambos formularios |
| Servicio | Solo en el formulario completo |
| Turno | Solo en el formulario completo |
| Detalle | Solo en el formulario completo |
| Origen | Lo pone la página, para saber de qué formulario vino |

El formulario corto de la portada pide solo nombre, teléfono y qué hay que
cuidar. Las demás columnas quedan vacías en esas filas, y eso es esperado.
