from .formatter import normalize_name


def build_message(name):
    name = normalize_name(name)
    return f"你好，{name}"