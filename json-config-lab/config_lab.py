import json

config = {
    "required_fields": ["id", "label"],
    "allowed_value_rules": {
        "label": ["positive", "negative"],
    },
}


def save_config(file_path, config_data):
    json_text = json.dumps(config_data)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json_text)


def read_config(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            loaded_config = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError("配置文件不是有效的 JSON") from error
    except FileNotFoundError as error:
        raise ValueError("配置文件不存在") from error
    return loaded_config


def validate_config(config_data):
    if not isinstance(config_data, dict):
        raise ValueError("配置最外层必须是字典")
    required_fields = config_data.get("required_fields", [])
    if not isinstance(required_fields, list):
        raise ValueError("required_fields 必须是字符串列表")
    for required_field in required_fields:
        if not isinstance(required_field, str):
            raise ValueError("required_fields 必须是字符串列表")
    allowed_value_rules = config_data.get("allowed_value_rules", {})
    if not isinstance(allowed_value_rules, dict):
        raise ValueError("allowed_value_rules 必须是字典")
    for field, allowed_values in allowed_value_rules.items():
        if not isinstance(allowed_values, list):
            raise ValueError("每个字段的允许值必须是字符串列表")
        for allowed_value in allowed_values:
            if not isinstance(allowed_value, str):
                raise ValueError("每个字段的允许值必须是字符串列表")
    return {
        "required_fields": required_fields,
        "allowed_value_rules": allowed_value_rules,
    }


def load_config(file_path):
    loaded_config = read_config(file_path)
    loaded_config = validate_config(loaded_config)
    return loaded_config


if __name__ == "__main__":
    save_config("rules.json", config)

    loaded_config = load_config("rules.json")
    print(type(loaded_config))
    print(loaded_config)
    print(loaded_config == config)
