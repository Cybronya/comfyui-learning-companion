# Qwen3_VQA_Plus

## 节点类型

`Qwen3_VQA_Plus`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `source_path:PATH`（2 次）
- `image:IMAGE`（2 次）
- `text:STRING`（2 次）
- `text2:STRING`（2 次）
- `model:COMBO`（2 次）
- `quantization:COMBO`（2 次）
- `keep_model_loaded:BOOLEAN`（2 次）
- `temperature:FLOAT`（2 次）
- `max_new_tokens:INT`（2 次）
- `min_pixels:INT`（2 次）

## 输出

- `STRING:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "Qwen3-VL-4B-Instruct-FP8", "none", false, 0.7, 2048, 200704, 1003520, 561, "randomize", "sdpa"]`（1 次）
- `["", "", "Qwen3-VL-4B-Instruct-FP8", "none", false, 0.7, 2048, 200704, 1003520, 1634, "randomize", "sdpa"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
