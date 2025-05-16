from enum import Enum
from fastapi import FastAPI, Path, HTTPException

app = FastAPI(
    title="路径参数示例",
    description="演示FastAPI中路径参数的各种用法"
)

# 基本路径参数示例


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    获取指定ID的物品

    - **item_id**: 物品ID，必须是整数
    """
    return {"item_id": item_id, "name": f"物品 {item_id}"}

# 路径操作顺序示例


@app.get("/users/me")
def read_current_user():
    """获取当前用户信息"""
    return {"user_id": "current", "name": "当前用户"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    """
    获取指定ID的用户

    - **user_id**: 用户ID
    """
    if user_id == "invalid":
        raise HTTPException(status_code=400, detail="无效的用户ID")
    return {"user_id": user_id, "name": f"用户 {user_id}"}

# 预定义值示例


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    """
    获取指定名称的模型

    - **model_name**: 模型名称，必须是预定义的值之一
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "深度学习万岁！"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeNet处理所有图像"}

    return {"model_name": model_name, "message": "残差网络"}

# 包含路径的参数示例


@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    """
    读取指定路径的文件

    - **file_path**: 文件路径，可以包含斜杠
    """
    return {"file_path": file_path}

# 使用Path增强参数


@app.get("/products/{product_id}")
def read_product(
    product_id: int = Path(..., title="产品ID", ge=1,
                           le=1000, description="产品的唯一标识符")
):
    """
    获取指定ID的产品

    - **product_id**: 产品ID，必须是1到1000之间的整数
    """
    return {"product_id": product_id, "name": f"产品 {product_id}"}

# 运行说明:
# 执行命令: uvicorn path_params:app --reload
# 访问: http://127.0.0.1:8000/docs
