import sys

import pytest

from argparse_lab import parse_args


def test_file_path_is_required(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["argparse_lab.py"])

    with pytest.raises(SystemExit):
        parse_args()


def test_parse_args_reads_file_path(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["argparse_lab.py", "sample.csv"])

    args = parse_args()

    assert args.file_path == "sample.csv"


def test_preview_defaults_to_five(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["argparse_lab.py", "sample.csv"])

    args = parse_args()

    assert args.preview == 5


def test_preview_accepts_custom_integer(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["argparse_lab.py", "sample.csv", "--preview", "3"],
    )

    args = parse_args()

    assert args.preview == 3


def test_preview_rejects_non_integer(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["argparse_lab.py", "sample.csv", "--preview", "abc"],
    )

    with pytest.raises(SystemExit):
        parse_args()


def test_verbose_defaults_to_false(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["argparse_lab.py", "sample.csv"])

    args = parse_args()

    assert args.verbose is False


def test_verbose_becomes_true_when_supplied(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["argparse_lab.py", "sample.csv", "--verbose"],
    )

    args = parse_args()

    assert args.verbose is True
