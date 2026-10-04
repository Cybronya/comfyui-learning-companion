from context.context_manager import (
    ContextManager
)

from pathlib import Path

# 用 __file__ 定位，保证从任意工作目录运行都能找到文件。
store_path = (
    Path(__file__).resolve().parent
    / "context"
    / "context_store.json"
)



context = ContextManager(
    store_path
)



context.update_question(

    "为什么我的图片很模糊？",

    "KSampler"

)



print(
    context.get_context()
)



# 结束后清空状态
context.clear()
