# FastAPI 装饰器工作原理 - Mermaid图解

## 装饰器执行流程图

```mermaid
flowchart TD
    A["@app.get('/items/{item_id}')\ndef read_item(item_id: int):\n    return {'item_id': item_id}"] -->|"Python解释器执行装饰器"| B
    B["等价于:\ndef read_item(item_id: int):\n    return {'item_id': item_id}\n\nread_item = app.get('/items/{item_id}')(read_item)"] -->|"步骤1: 调用app.get()"| C
    C["FastAPI.get() 方法\ndef get(self, path, ...):\n    return self.router.get(path, ...)"] -->|"步骤2: 调用router.get()"| D
    D["APIRouter.get() 方法\ndef get(self, path, ...):\n    return self.api_route(\n        path=path,\n        methods=['GET'],\n        ...)"] -->|"步骤3: 返回装饰器函数"| E
    E["api_route返回装饰器函数\ndef decorator(func):\n    self.add_api_route(path, func, ...)\n    return func\n\nreturn decorator"] -->|"步骤4: 执行装饰器函数"| F
    F["decorator(read_item)\n\n# 在decorator内部\nself.add_api_route('/items/{item_id}', read_item, methods=['GET'], ...)\nreturn read_item"] -->|"步骤5: 路由注册"| G
    G["# 在add_api_route内部\nroute = APIRoute(\n    '/items/{item_id}',\n    endpoint=read_item,\n    methods=['GET'],\n    ...)\n\nself.routes.append(route)"]
```

## 时序图：装饰器执行时间

```mermaid
sequenceDiagram
    participant App as 应用启动
    participant Dec as 执行装饰器
    participant Reg as 注册路由
    participant Table as 路由表
    participant Req as 接收请求
    participant Match as 匹配路由
    participant Exec as 执行函数
    
    App ->> Dec: 应用启动时
    Dec ->> Reg: 执行装饰器
    Reg ->> Table: 注册路由
    Note over App,Table: 应用初始化完成
    
    Req ->> Match: 请求处理时
    Match ->> Exec: 匹配路由
    Exec -->> Req: 返回响应
```

## 类图：装饰器与路由的关系

```mermaid
classDiagram
    class FastAPI {
        +router
        +get()
        +post()
        +put()
    }
    class APIRouter {
        +routes[]
        +get()
        +api_route()
        +add_api_route()
    }
    class APIRoute {
        +path
        +endpoint
        +methods
    }
    
    FastAPI --> APIRouter: 包含
    APIRouter --> APIRoute: 包含多个
```

## 动手练习

尝试在你的FastAPI应用中添加不同的装饰器参数，观察其效果：

```python
@app.get(
    "/items/{item_id}",
    tags=["items"],
    summary="获取单个物品",
    response_description="物品信息",
    status_code=200
)
def read_item(item_id: int):
    return {"item_id": item_id}
```

在支持Mermaid的Markdown查看器中（如VS Code+Markdown预览或GitHub），以上图表会被渲染为美观的可视化图形。 