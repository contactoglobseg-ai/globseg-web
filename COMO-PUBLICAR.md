# Cómo publicar el sitio en Cloudflare Pages

El dominio ya está en Cloudflare, así que publicamos ahí mismo: es gratis,
el certificado HTTPS se emite solo y no hay que configurar DNS a mano.

**Solo se sube la carpeta `sitio/`.** Lo demás que hay en `PAGINA WEB/`
son archivos de trabajo que no deben quedar públicos (el código de la
planilla lleva el ID de tu base de datos).

```
PAGINA WEB/
├── sitio/                     ← esto se sube
│   ├── index.html
│   ├── robots.txt
│   ├── _headers
│   └── assets/logo.png
├── planilla-google.gs         ← NO subir (tiene el ID de la planilla)
├── COMO-CONECTAR-LA-PLANILLA.md
├── COMO-PUBLICAR.md
└── BRIEF-PORTADA.md
```

---

## 1. Entra a Cloudflare

[dash.cloudflare.com](https://dash.cloudflare.com) con la cuenta donde
compraste el dominio.

## 2. Crea el proyecto

En el menú de la izquierda: **Compute (Workers) → Workers & Pages**, botón
**Create**, y luego la pestaña **Pages**.

Elige **Upload assets** (subir archivos), no la opción de conectar con Git.

- **Nombre del proyecto:** `seguridad-garridos`

## 3. Sube la carpeta

Arrastra la carpeta **`sitio`** completa a la zona de subida, o usa
**Select from computer → Upload folder** y elige `sitio`.

Importante: arrastra la carpeta `sitio`, no los archivos uno por uno, para
que `assets/logo.png` conserve su ubicación.

Botón **Deploy**.

En menos de un minuto queda publicado en una dirección de prueba del tipo
`seguridad-garridos.pages.dev`. Ábrela y revisa que se vea bien.

## 4. Conecta tu dominio

Dentro del proyecto: pestaña **Custom domains → Set up a custom domain**.

Escribe tu dominio. Como ya está en Cloudflare, los registros DNS se crean
solos; no hay que copiar nada.

Conviene agregarlo dos veces:

- `tudominio.cl` (el dominio pelado)
- `www.tudominio.cl`

Cloudflare redirige uno al otro y emite el certificado. Puede tardar unos
minutos en quedar activo.

## 5. Avísame

Cuando esté arriba, mándame la dirección. Me queda pendiente dejar en la
página:

- la dirección canónica y las etiquetas para compartir en WhatsApp y redes
- el `sitemap.xml` y la línea `Sitemap:` en `robots.txt`
- el título con la zona de cobertura, que es lo que Google usa para
  mostrarte en búsquedas locales

Y probar el formulario contra la planilla desde el dominio real, que es el
único lugar donde se puede verificar de verdad.

---

## Para actualizar el sitio más adelante

Entra al proyecto en Cloudflare → **Create new deployment** → arrastra la
carpeta `sitio` otra vez. La versión anterior queda guardada, así que se
puede volver atrás con un clic si algo sale mal.

## Qué hace el archivo `_headers`

No es parte de la página: son instrucciones para Cloudflare.

- Cabeceras de seguridad (evitan que el sitio se incruste en otra página o
  que el navegador adivine tipos de archivo).
- Una política que limita a qué servidores externos puede conectarse la
  página: solo las tipografías de Google y el Apps Script de la planilla.
  **Si cambias el destino del formulario, hay que agregarlo ahí**, o el
  navegador bloqueará el envío.
- Cache larga para el logo, que no cambia.
