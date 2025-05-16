# FastAPI 入门

## 什么是 FastAPI？

FastAPI 是一个现代化、高性能、易于学习的 Python Web 框架，专为 API 开发而设计。它基于标准的 Python 类型提示，提供自动参数验证、序列化和文档生成。

### 核心特点

- **性能极高**：FastAPI 基于 Starlette 和 Pydantic，性能接近 NodeJS 和 Go
- **快速开发**：提高功能开发速度约 200-300%
- **更少的错误**：减少约 40% 的人为错误
- **直观易用**：强大的编辑器支持，自动补全无处不在
- **简单易学**：文档详尽，设计简洁
- **简短精悍**：代码重复最小化，参数声明功能强大
- **健壮可靠**：自动生成交互式文档，生产环境可用代码

## 技术基础

FastAPI 建立在两个强大的库之上：

1. **Starlette**：负责 Web 部分的高性能异步框架
2. **Pydantic**：负责数据验证和序列化的库，基于 Python 类型注解

## 第一个 FastAPI 应用

### 基本结构

```python
from fastapi import FastAPI

# 创建应用实例
app = FastAPI()

# 定义路径操作
@app.get("/")
def read_root():
    return {"Hello": "World"}
```

### 核心组件分析

1. **FastAPI 类**：整个应用的主入口，继承自 Starlette
   ```python
   app = FastAPI(
       title="我的API",
       description="这是API描述",
       version="0.1.0"
   )
   ```

2. **路径操作装饰器**：如 `@app.get()`、`@app.post()`
   - 定义 HTTP 方法和路径
   - 在底层注册路由

3. **路径操作函数**：处理特定路径的请求的函数
   ```python
   def read_root():
       return {"Hello": "World"}
   ```

### 运行应用

FastAPI 应用需要通过 ASGI 服务器运行，最常用的是 Uvicorn：

```bash
uvicorn main:app --reload
```

其中：
- `main`: Python 模块名 (main.py)
- `app`: FastAPI 实例对象名
- `--reload`: 代码变更时自动重启（仅开发环境使用）

## 自动生成文档

FastAPI 自动为你的 API 提供两种交互式文档：

1. **Swagger UI**：访问 `/docs`
   - 提供交互式探索和测试功能
   - 支持 OAuth2 认证

2. **ReDoc**：访问 `/redoc`
   - 提供更现代化的文档界面
   - 适合 API 使用者阅读

## 使用 Python 类型提示

FastAPI 利用 Python 的类型提示进行多种功能：

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

这里的类型注解实现了：
- 编辑器支持（自动补全、类型检查）
- 参数类型转换
- 数据验证
- 自动文档生成

## 从源码角度看 FastAPI

FastAPI 的核心逻辑在 `FastAPI` 类中，它继承自 Starlette 的 `Starlette` 类，主要添加了：

1. 基于 Pydantic 的数据验证
2. 自动文档生成
3. 依赖注入系统

```python
# 从 fastapi/applications.py 简化版
class FastAPI(Starlette):
    def __init__(
        self,
        debug: bool = False,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        ...
    ) -> None:
        self.router = routing.APIRouter()  # 核心路由器
        ...
```

## 下一步学习

- 探索路径参数和查询参数的使用
- 学习如何使用 Pydantic 模型定义请求体
- 理解响应模型和状态码 