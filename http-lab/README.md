# http-lab

这个实验用于理解最小 HTTP 请求和响应流程。

已练习内容：

- 客户端使用 URL 访问服务端。
- 服务端根据 path 判断请求的是哪个资源。
- `GET /annotations` 返回标注列表。
- `GET /annotators` 返回标注员列表。
- 未定义的 path 返回 `404` 和错误 JSON。
- 客户端接住 `HTTPError`，把 404 当作响应结果处理。

运行：

```powershell
python .\http_lab.py
```

测试：

```powershell
python -m pytest -q
```

当前验证结果：`3 passed`
