import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="演示 Python 命令行参数"
    )
    parser.add_argument(
        "file_path",
        help="要处理的文件路径",
    )

    parser.add_argument(
        "--preview",
        type=int,
        default=5,
        help="预览前 N 行，默认 5 行",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="显示详细运行信息",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print(args.file_path)
    print(args.preview)
    print(type(args.preview))

    if args.verbose:
        print(f"正在读取文件: {args.file_path}")
        print(f"预览行数: {args.preview}")

    print("处理完成")


if __name__ == "__main__":
    main()
