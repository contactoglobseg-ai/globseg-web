#!/usr/bin/env python3
"""Servidor para ver el sitio localmente.

No usa `python3 -m http.server` a propósito: ese módulo consulta el
directorio actual al arrancar, y el entorno de vista previa puede lanzarlo
desde una carpeta que no se puede leer. Acá se hace chdir primero.

Uso: python3 "PAGINA WEB/servir-local.py" [puerto]
"""
import functools
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitio")
PUERTO = int(sys.argv[1]) if len(sys.argv) > 1 else 8777

os.chdir(RAIZ)


class Silencioso(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


servidor = ThreadingHTTPServer(
    ("127.0.0.1", PUERTO), functools.partial(Silencioso, directory=RAIZ)
)
print(f"Sirviendo {RAIZ} en http://127.0.0.1:{PUERTO}", flush=True)
servidor.serve_forever()
