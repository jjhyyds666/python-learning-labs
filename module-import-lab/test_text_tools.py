import text_tools

from text_tools.__main__ import main
from text_tools.formatter import normalize_name
from text_tools.message import build_message


def test_normalize_name_strips_surrounding_spaces():
    assert normalize_name("  小明  ") == "小明"


def test_build_message_normalizes_name():
    assert build_message("  小明  ") == "你好，小明"


def test_package_exports_build_message():
    assert text_tools.build_message("小红") == "你好，小红"


def test_package_main_prints_message(capsys):
    main()

    captured = capsys.readouterr()

    assert captured.out == "你好，小明\n"
