# FastAPI 装饰器实现原理

## 装饰器概述

在 FastAPI 中，`@app.get()`、`@app.post()` 等路径操作装饰器是整个框架的核心功能。这些装饰器使我们能够以简洁的方式定义 API 端点。

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

## 装饰器实现原理

通过分析 FastAPI 源码，我们可以看到装饰器的实现涉及多层调用:

### 1. 装饰器链路

当我们使用 `@app.get()` 时，实际上发生了以下调用链:

1. `FastAPI.get()` - 定义在 `applications.py` 中
2. `APIRouter.get()` - 定义在 `routing.py` 中 
3. `APIRouter.api_route()` - 通用路由装饰器
4. `APIRouter.add_api_route()` - 实际添加路由的方法
5. 创建 `APIRoute` 实例并添加到路由列表

### 2. 关键源码解析

#### FastAPI 类中的 get 方法

```python
# FastAPI.get() 方法 (applications.py)
def get(self, path: str, *, response_model=None, ...):
    return self.router.get(
        path,
        response_model=response_model,
        ...
    )
```

FastAPI 类的 get 方法实际上是将调用转发给内部的 router 对象。

#### APIRouter 类中的 get 方法

```python
# APIRouter.get() 方法 (routing.py)
def get(self, path: str, *, response_model=None, ...):
    return self.api_route(
        path=path,
        response_model=response_model,
        methods=["GET"],
        ...
    )
```

APIRouter 的 get 方法调用通用的 api_route 方法，并指定 methods=["GET"]。

#### api_route 方法 (核心)

```python
# APIRouter.api_route() 方法 (routing.py)
def api_route(self, path, *, methods=None, ...):
    def decorator(func: Callable) -> Callable:
        self.add_api_route(
            path,
            func,
            methods=methods,
            ...
        )
        return func
    return decorator
```

这是装饰器模式的典型实现:
1. 返回一个 decorator 函数
2. decorator 函数接收被装饰的函数 func
3. 在内部调用 add_api_route 注册路由
4. 返回原始函数 func

#### add_api_route 方法

```python
# APIRouter.add_api_route() 方法 (routing.py)
def add_api_route(self, path, endpoint, *, methods=None, ...):
    route = APIRoute(
        path,
        endpoint=endpoint,
        methods=methods,
        ...
    )
    self.routes.append(route)
```

最终创建 APIRoute 实例并添加到路由列表。

## 装饰器执行流程

当解释器遇到 `@app.get("/")` 时:

1. 调用 `app.get("/")` 并获取返回的装饰器函数
2. 将下面定义的函数传给装饰器
3. 装饰器将函数和路径注册到路由系统
4. 返回原始函数

## FastAPI 应用初始化与路由注册

在 FastAPI 应用初始化时:

```python
# FastAPI 初始化 (applications.py)
def __init__(self, ...):
    self.router: routing.APIRouter = routing.APIRouter()
    ...
```

创建 APIRouter 实例用于路由管理。

## 装饰器额外参数的作用

装饰器接受的参数都会传递给 APIRoute:

- `response_model`: 指定响应数据模型
- `status_code`: 指定响应状态码
- `tags`: 用于 API 文档分组
- `summary`/`description`: API 文档说明
- 等等...

这些参数不仅影响路由注册，还用于生成 OpenAPI 文档。

## 实际应用示例

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get(
    "/items/{item_id}",
    response_model=Item,
    status_code=200,
    tags=["items"],
    summary="获取物品"
)
def read_item(item_id: int = Path(..., description="物品ID")):
    return {"id": item_id}
```

上面的装饰器调用链:
1. `app.get(...)` 返回装饰器函数
2. 装饰器函数接收 `read_item` 函数
3. 路由 "/items/{item_id}" 与该函数关联
4. 所有元数据（如 response_model）都保存在路由对象中

## 总结

FastAPI 路径操作装饰器基于 Python 装饰器模式，将函数式 API 转换为注册到内部路由系统的端点。这种设计既保持了代码的简洁性，又提供了强大的元数据支持，特别是与 OpenAPI 文档生成的集成。 