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

### package-install-lab

练习内容：

- 为实验创建独立虚拟环境
- 使用 `pyproject.toml` 描述可安装 Python 项目
- 使用 `[project.scripts]` 注册命令行入口
- 使用 `pip install -e .` 进行可编辑安装
- 直接通过 `greet-lab` 命令运行 Python 函数
- 为位置参数、可选整数参数和参数边界编写自动测试

安装与运行：

```powershell
cd .\package-install-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
greet-lab 小明 --times 3
```

测试命令：

```powershell
python -m pytest -q .\package-install-lab
```

验证结果：`10 passed`

### ruff-lab

练习内容：

- 区分“代码可以运行”和“代码质量检查通过”
- 使用 `ruff format --check` 检查格式
- 使用 `ruff format` 自动整理代码
- 使用 `ruff check` 发现未使用导入等问题
- 使用 `ruff check --fix` 自动修复可安全处理的问题
- 在 lint 修复后再次格式化和运行测试
- 使用 `pyproject.toml` 保存统一 Ruff 配置

安装开发工具：

```powershell
cd .\ruff-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

检查命令：

```powershell
ruff check .
ruff format --check .
python -m pytest -q
```

验证结果：`4 passed`，lint 和格式检查通过。
