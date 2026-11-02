# El dominio: qué quedó listo y qué falta

## ✅ Todo entra por https (02-11-2026)

**Qué pasaba antes.** Si alguien escribía `seggarridos.com` sin el `https://`
adelante —que es como lo escribe cualquiera— Cloudflare entregaba la página
**en claro, por http**, con código 200. No redirigía. Esa primera visita lleva
la portada entera y el formulario donde la persona escribe su nombre y su
teléfono: por http eso viaja a la vista de cualquiera en la misma red wifi.

La cabecera `Strict-Transport-Security` de `sitio/_headers` ya estaba puesta,
pero **solo protege a quien ya entró una vez por https**. La primera visita, que
es la del cliente nuevo, quedaba afuera.

**Cómo se arregló.** No desde el código: el sitio son archivos, no hay servidor
propio que pueda contestar una redirección. Fue un interruptor del panel, que
encendió el gerente:

> **dash.cloudflare.com → dominio seggarridos.com → SSL/TLS → Edge Certificates
> → Always Use HTTPS → On**

**Comprobado el mismo día**, en los tres hosts:

```bash
for h in seggarridos.com adm.seggarridos.com asistencia.seggarridos.com; do
  curl -sI "http://$h/?x=$RANDOM" | grep -i "^HTTP/\|^location"
done
```

Los tres contestan `301 Moved Permanently` con `Location: https://…`, conservan
la cadena de consulta, y la redirección es **de un solo salto**.

Cubre **toda la zona**, así que también vale para los subdominios que se
agreguen después. Al Worker de administración no le hace daño —ya redirigía por
su cuenta en `src/seguridad.js`—; lo que cambia es que ahora la petición en
claro se corta en el borde de Cloudflare y ni siquiera le llega.

---

## ⬜ Falta: `www.seggarridos.com`

Hoy **no existe**: da NXDOMAIN. Quien escriba el «www» por costumbre no llega a
ninguna parte.

Se agrega en el panel, en el Worker `globseg-web` → **Settings → Domains &
Routes → Add → Custom domain**, escribiendo `www.seggarridos.com`. Como el
dominio ya está en Cloudflare, el registro DNS y el certificado se crean solos;
puede tardar unos minutos.

Para comprobarlo:

```bash
curl -sI "https://www.seggarridos.com/?x=$RANDOM" | head -3
```

---

**Nota:** `COMO-PUBLICAR.md` quedó viejo. Describe subir la carpeta a mano a
Cloudflare Pages, y desde el 08-10-2026 esto es un **Worker** conectado al
repositorio: se publica con `git push` a `main` y Cloudflare lo despliega solo
en menos de un minuto.
