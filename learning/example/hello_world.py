from fastapi import FastAPI

# 创建FastAPI应用实例
app = FastAPI(
    title="FastAPI 学习示例",
    description="这是一个用于学习FastAPI的示例应用",
    version="0.1.0",
)

# 定义根路径操作


@app.get("/")
def read_root():
    """
    返回一个简单的欢迎消息
    """
    return {"message": "Hello World from FastAPI!"}

# 带路径参数的路径操作


@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    """
    获取指定ID的物品

    - **item_id**: 物品的ID，必须是整数
    - **query_param**: 可选的查询参数
    """
    return {
        "item_id": item_id,
        "query_param": query_param
    }

# 运行说明:
# 1. 在终端中导航到此文件所在目录
# 2. 执行命令: uvicorn hello_world:app --reload
# 3. 打开浏览器访问: http://127.0.0.1:8000/docs
