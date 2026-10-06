# llama_cpp_model_loader

## 节点类型

`llama_cpp_model_loader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 35 个 workflow 中。

## 输入

- `model:COMBO`（40 次）
- `mmproj:COMBO`（40 次）
- `chat_handler:COMBO`（40 次）
- `n_ctx:INT`（40 次）
- `vram_limit:INT`（40 次）
- `image_min_tokens:INT`（40 次）
- `image_max_tokens:INT`（40 次）
- `load_mtp:BOOLEAN`（40 次）

## 输出

- `llama_model:LLAMACPPMODEL`（40 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3.8-27B-IQ4_XS.gguf", "Qwen3.8-27B-mmproj-BF16.gguf", "Qwen3.8", 11520, -1, 0, 0, false]`（6 次）
- `["Qwen3.5-9B-Q8_0.gguf", "Qwen3.5-9B-mmproj-BF16.gguf", "Qwen3.5-Thinking", 8192, -1, 0, 0, false]`（6 次）
- `["Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-Q8_0.gguf", "mmproj-Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-BF16.gguf", "Q`（5 次）
- `["Qwen3.5-9B-Q8_0.gguf", "Qwen3.5-9B-mmproj-F16.gguf", "Qwen3.5", 29952, -1, 0, 0, false]`（3 次）
- `["Qwen3.5-9b-heretic-v2-q8_0.gguf", "mmproj-Qwen3.5-9B-Uncensored-HauhauCS-Aggressive-BF16.gguf", "Qwen3.5", 8192, -1, 0`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
