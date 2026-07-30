from quality_lab import build_messages, main


def test_build_messages_returns_requested_number():
    assert build_messages("小明", 3) == [
        "你好，小明",
        "你好，小明",
        "你好，小明",
    ]


def test_build_messages_supports_different_names():
    assert build_messages("小红", 1) == ["你好，小红"]


def test_build_messages_returns_empty_list_for_zero():
    assert build_messages("小明", 0) == []


def test_main_prints_example_messages(capsys):
    main()

    captured = capsys.readouterr()

    assert captured.out == "['你好，小明', '你好，小明']\n"
