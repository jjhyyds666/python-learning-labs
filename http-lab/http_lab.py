import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from urllib.error import HTTPError
from urllib.request import urlopen

ANNOTATIONS = [
    {"id": 1, "label": "positive"},
    {"id": 2, "label": "negative"},
]

ANNOTATORS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]


class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/annotations":
            status_code = 200
            response_data = ANNOTATIONS
        elif self.path == "/annotators":
            status_code = 200
            response_data = ANNOTATORS
        else:
            status_code = 404
            response_data = {
                "error": "not found",
                "path": self.path,
            }

        body = json.dumps(response_data, ensure_ascii=False).encode("utf-8")

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass


def fetch_url(url):
    try:
        with urlopen(url) as response:
            status_code = response.status
            body = response.read().decode("utf-8")
    except HTTPError as error:
        status_code = error.status
        body = error.read().decode("utf-8")

    return status_code, body


def start_server():
    server = HTTPServer(("127.0.0.1", 0), DemoHandler)
    thread = Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    return server


def main():
    server = start_server()
    host, port = server.server_address

    try:
        status_code, body = fetch_url(f"http://{host}:{port}/projects")
        print(status_code)
        print(body)
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
