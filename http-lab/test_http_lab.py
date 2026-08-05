import json

import pytest

from http_lab import fetch_url, start_server


@pytest.fixture
def server():
    http_server = start_server()

    try:
        yield http_server
    finally:
        http_server.shutdown()


def build_url(server, path):
    host, port = server.server_address

    return f"http://{host}:{port}{path}"


def test_fetch_annotations_returns_json_list(server):
    status_code, body = fetch_url(build_url(server, "/annotations"))

    assert status_code == 200
    assert json.loads(body) == [
        {"id": 1, "label": "positive"},
        {"id": 2, "label": "negative"},
    ]


def test_fetch_annotators_returns_json_list(server):
    status_code, body = fetch_url(build_url(server, "/annotators"))

    assert status_code == 200
    assert json.loads(body) == [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]


def test_fetch_missing_path_returns_404(server):
    status_code, body = fetch_url(build_url(server, "/projects"))

    assert status_code == 404
    assert json.loads(body) == {
        "error": "not found",
        "path": "/projects",
    }
