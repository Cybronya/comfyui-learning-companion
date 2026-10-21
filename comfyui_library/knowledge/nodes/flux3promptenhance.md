# Flux3PromptEnhance

## 节点类型

`Flux3PromptEnhance`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `pe_model:FLUX3_PE_MODEL`（8 次）
- `images.image_1:IMAGE`（8 次）
- `prompt:STRING`（8 次）
- `keep_loaded:BOOLEAN`（8 次）
- `use_cache:BOOLEAN`（8 次）
- `max_tokens:INT`（8 次）
- `canvas_width:INT`（8 次）
- `canvas_height:INT`（8 次）
- `boxes_json:STRING`（8 次）
- `retry_invalid_output:BOOLEAN`（8 次）

## 输出

- `enhanced_prompt:STRING`（8 次）
- `details_json:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A man walking with his dog, afternoon sun", false, true, 3584, 0, 0, "", true]`（4 次）
- `["A woman walking with his dog, afternoon sun", false, true, 3584, 0, 0, "", true]`（3 次）
- `["", false, true, 3584, 0, 0, "", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
