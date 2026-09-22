"""Serve only the generated static directory on loopback."""
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from functools import partial
from pathlib import Path
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8765);args=parser.parse_args()
dist=Path(__file__).resolve().parent/'dist'
if not (dist/'site-data.json').exists():raise SystemExit('Run python site/build.py first')
class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control','no-cache')
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Referrer-Policy','no-referrer')
        self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        super().end_headers()
    def list_directory(self,path):self.send_error(404);return None
server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(Handler,directory=str(dist)))
print(f'Local only: http://127.0.0.1:{args.port}',flush=True)
try:server.serve_forever()
except KeyboardInterrupt:server.server_close()
