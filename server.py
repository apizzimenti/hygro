#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from handler import Handler


class RequestHandler(BaseHTTPRequestHandler):
    def _set_json_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def _set_html_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

    def do_GET(self):

        if self.path == "/":
            self._set_html_headers()
            self.wfile.write(Handler.formatted())

        elif self.path == "/now":
            self._set_json_headers()
            self.wfile.write(Handler.latest())

        elif self.path == "/load":
            self._set_json_headers()
            self.wfile.write(Handler.all())


def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print "> Starting server on port {}...".format(port)
    httpd.serve_forever()

run()

