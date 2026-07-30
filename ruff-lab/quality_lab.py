import os

def build_messages(name, times):
    messages = []
    for _ in range(times):
        messages.append(f"你好，{name}")
    return messages


def main():
    print(build_messages("小明", 2))


if __name__ == "__main__":
    main()
