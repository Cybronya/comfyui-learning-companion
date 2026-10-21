# XB_llamaModelLoader

## 节点类型

`XB_llamaModelLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:COMBO`（2 次）
- `mmproj:COMBO`（2 次）
- `chat_handler:COMBO`（2 次）
- `n_ctx:INT`（2 次）
- `vram_limit:INT`（2 次）
- `image_min_tokens:INT`（2 次）
- `image_max_tokens:INT`（2 次）

## 输出

- `llama_model:LLAMACPPMODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Huihui-Qwen3-VL-4B-Instruct-abliterated.Q8_0.gguf", "Huihui-Qwen3-VL-4B-Instruct-abliterated.mmproj-Q8_0.gguf", "Qwen3`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
