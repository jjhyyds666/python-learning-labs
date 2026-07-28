import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="输出指定次数的问候语")

    parser.add_argument(
        "name",
        help="要问候的名字",
    )

    parser.add_argument(
        "--times",
        type=int,
        default=1,
        help="问候次数，默认 1 次",
    )

    args = parser.parse_args()

    if args.times < 1:
        parser.error("--times 必须大于 0")

    return args


def main():
    args = parse_args()

    for _ in range(args.times):
        print(f"你好，{args.name}")


if __name__ == "__main__":
    main()
