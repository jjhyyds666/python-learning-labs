# Python Learning Labs

这个仓库用于保存彼此独立的 Python 学习实验。每个新知识点从空文件开始，理解并验证后，再决定是否整合进作品项目。

## 已完成实验

### json-config-lab

练习内容：

- JSON 序列化、保存和读取
- 配置结构校验与默认值
- 文件不存在和 JSON 损坏的异常处理
- pytest 自动测试

验证结果：`12 passed`

### argparse-lab

练习内容：

- 必填位置参数
- 带值的可选参数
- `type` 和 `default`
- 使用 `store_true` 创建布尔开关
- 使用 `parse_args()` 和 `main()` 整理程序结构
- 使用 pytest 模拟命令行参数

运行示例：

```powershell
python .\argparse-lab\argparse_lab.py sample.csv
python .\argparse-lab\argparse_lab.py sample.csv --preview 3 --verbose
```

测试命令：

```powershell
python -m pytest -q .\argparse-lab
```

验证结果：`7 passed`

### module-import-lab

练习内容：

- 从另一个 Python 文件导入函数
- 区分直接运行和被其他模块导入
- 使用 `__name__ == "__main__"` 控制入口行为
- 使用 `__init__.py` 建立包并统一提供函数
- 使用相对导入连接包内模块
- 使用 `__main__.py` 和 `python -m` 运行整个包

运行示例：

```powershell
cd .\module-import-lab
python .\app.py
python -m text_tools
```

测试命令：

```powershell
python -m pytest -q .\module-import-lab
```

验证结果：`4 passed`
