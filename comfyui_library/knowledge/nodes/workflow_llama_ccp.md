# workflow>LLama-ccp提示词反推

## 节点类型

`workflow>LLama-ccp提示词反推`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `queue_handler:*`（1 次）
- `model:COMBO`（1 次）
- `mmproj:COMBO`（1 次）
- `chat_handler:COMBO`（1 次）
- `n_ctx:INT`（1 次）
- `vram_limit:INT`（1 次）
- `image_min_tokens:INT`（1 次）
- `image_max_tokens:INT`（1 次）
- `max_tokens:INT`（1 次）

## 输出

- `output:STRING`（1 次）
- `output_list:STRING`（1 次）
- `state_uid:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3.5-9b-heretic-v2-q8_0.gguf", "Qwen3.5-9B-mmproj-BF16.gguf", "Qwen3.5", 8192, -1, 0, 0, 1024, 30, 0.1, 5, -1, 0.9,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
