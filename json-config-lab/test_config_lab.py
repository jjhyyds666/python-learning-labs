import pytest

from config_lab import load_config, read_config, save_config, validate_config


def test_save_and_read_config(tmp_path):
    config_file = tmp_path / "rules.json"
    config_data = {
        "required_fields": ["id", "label"],
        "allowed_value_rules": {
            "label": ["positive", "negative"],
        },
    }

    save_config(config_file, config_data)
    loaded_config = read_config(config_file)

    assert loaded_config == config_data


def test_load_config_reads_and_validates_config(tmp_path):
    config_file = tmp_path / "rules.json"
    config_data = {
        "required_fields": ["id", "label"],
        "allowed_value_rules": {
            "label": ["positive", "negative"],
        },
    }
    save_config(config_file, config_data)

    loaded_config = load_config(config_file)

    assert loaded_config == config_data


def test_read_config_rejects_invalid_json(tmp_path):
    config_file = tmp_path / "rules.json"
    config_file.write_text(
        '{"required_fields": [',
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match=r"^配置文件不是有效的 JSON$",
    ):
        read_config(config_file)


def test_read_config_rejects_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"

    with pytest.raises(
        ValueError,
        match=r"^配置文件不存在$",
    ):
        read_config(missing_file)


def test_validate_config_accepts_valid_config():
    config_data = {
        "required_fields": ["id", "label"],
        "allowed_value_rules": {
            "label": ["positive", "negative"],
        },
    }

    validate_config(config_data)


def test_validate_config_adds_missing_defaults():
    result = validate_config({})

    assert result == {
        "required_fields": [],
        "allowed_value_rules": {},
    }


def test_validate_config_rejects_non_dict():
    with pytest.raises(
        ValueError,
        match=r"^配置最外层必须是字典$",
    ):
        validate_config([])


def test_validate_config_rejects_non_list_required_fields():
    with pytest.raises(
        ValueError,
        match=r"^required_fields 必须是字符串列表$",
    ):
        validate_config({"required_fields": "id"})


def test_validate_config_rejects_non_string_required_field():
    with pytest.raises(
        ValueError,
        match=r"^required_fields 必须是字符串列表$",
    ):
        validate_config({"required_fields": ["id", 123]})


def test_validate_config_rejects_non_dict_allowed_value_rules():
    with pytest.raises(
        ValueError,
        match=r"^allowed_value_rules 必须是字典$",
    ):
        validate_config({"allowed_value_rules": []})


def test_validate_config_rejects_non_list_allowed_values():
    with pytest.raises(
        ValueError,
        match=r"^每个字段的允许值必须是字符串列表$",
    ):
        validate_config(
            {"allowed_value_rules": {"label": "positive"}}
        )


def test_validate_config_rejects_non_string_allowed_value():
    with pytest.raises(
        ValueError,
        match=r"^每个字段的允许值必须是字符串列表$",
    ):
        validate_config(
            {"allowed_value_rules": {"label": ["positive", 123]}}
        )
