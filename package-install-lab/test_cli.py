import sys
import tomllib
from pathlib import Path

import pytest

from greet_cli.cli import main, parse_args


def test_name_is_required(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["greet-lab"])

    with pytest.raises(SystemExit):
        parse_args()


def test_parse_args_reads_name(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["greet-lab", "小明"])

    args = parse_args()

    assert args.name == "小明"


def test_times_defaults_to_one(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["greet-lab", "小明"])

    args = parse_args()

    assert args.times == 1


def test_times_accepts_custom_integer(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["greet-lab", "小明", "--times", "3"],
    )

    args = parse_args()

    assert args.times == 3


def test_times_rejects_non_integer(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["greet-lab", "小明", "--times", "abc"],
    )

    with pytest.raises(SystemExit):
        parse_args()


@pytest.mark.parametrize("times", ["0", "-1"])
def test_times_must_be_positive(monkeypatch, times):
    monkeypatch.setattr(
        sys,
        "argv",
        ["greet-lab", "小明", "--times", times],
    )

    with pytest.raises(SystemExit):
        parse_args()


def test_main_prints_one_greeting_by_default(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["greet-lab", "小明"])

    main()

    captured = capsys.readouterr()
    assert captured.out == "你好，小明\n"


def test_main_prints_requested_number_of_greetings(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["greet-lab", "小明", "--times", "3"],
    )

    main()

    captured = capsys.readouterr()
    assert captured.out == "你好，小明\n" * 3


def test_pyproject_defines_console_script():
    pyproject_path = Path(__file__).with_name("pyproject.toml")
    config = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

    assert config["project"]["scripts"]["greet-lab"] == "greet_cli.cli:main"
