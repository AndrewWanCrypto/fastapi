# FastAPI 入门与安装

## FastAPI 的技术基础

FastAPI 主要建立在两个强大的库之上：

1. **Starlette**：负责 Web 部分的高性能异步框架
   - 提供请求和响应处理
   - 路由系统
   - WebSocket 支持
   - 中间件系统

2. **Pydantic**：负责数据验证和序列化
   - 基于 Python 类型注解的数据验证
   - 复杂数据模型定义和处理
   - 序列化和反序列化
   - 配置管理

## 安装方法

### 基本安装

```bash
# 使用pip
pip install fastapi uvicorn

# 使用uv (更快的替代方案)
uv pip install fastapi uvicorn
```

说明：
- `fastapi`：框架本身
- `uvicorn`：ASGI服务器，用于运行FastAPI应用

### 包含所有可选依赖的完整安装

```bash
pip install fastapi[all]
```

这将安装所有可选依赖，包括：
- `uvicorn`：ASGI服务器
- `python-multipart`：表单处理
- `aiofiles`：异步文件处理
- `itsdangerous`：安全相关功能
- `pyyaml`：YAML支持
- `ujson`：高性能JSON
- 等等...

### 创建虚拟环境

推荐在虚拟环境中安装，保持项目依赖隔离：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境 (MacOS/Linux)
source venv/bin/activate

# 激活虚拟环境 (Windows)
venv\Scripts\activate

# 安装依赖
pip install fastapi uvicorn
```

## 版本兼容性

FastAPI 需要 Python 3.6 及以上版本，因为它依赖于：
- 类型提示 (type hints)
- f-strings
- 异步语法 (async/await)

## 验证安装

安装完成后，可以创建一个简单的应用来验证安装是否成功：

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

运行应用：

```bash
uvicorn main:app --reload
```

然后访问：http://127.0.0.1:8000 和 http://127.0.0.1:8000/docs 验证是否正常工作。

## 开发工具配置

为获得更好的开发体验，推荐配置：

1. **代码编辑器/IDE**：
   - VS Code + Python扩展
   - PyCharm Professional
   - 任何支持Python类型提示的编辑器

2. **代码格式化和检查工具**：
   - `black`：代码格式化
   - `flake8`：代码检查
   - `mypy`：类型检查 