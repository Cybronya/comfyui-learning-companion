# EcommercePromptGenerator

## 节点类型

`EcommercePromptGenerator`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `product_image:IMAGE`（1 次）
- `api_url:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model_name:STRING`（1 次）
- `product_type:STRING`（1 次）
- `selling_points:STRING`（1 次）
- `design_style:COMBO`（1 次）
- `seed:INT`（1 次）

## 输出

- `prompts_list:STRING`（1 次）
- `debug_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://api-inference.modelscope.cn/v1", "ms-f6129b82-777f-4e6e-8510-538973e45a98", "Qwen/Qwen3-VL-235B-A22B-Instruct"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
