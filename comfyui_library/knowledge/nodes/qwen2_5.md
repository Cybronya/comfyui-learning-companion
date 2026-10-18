# Qwen2.5

## 节点类型

`Qwen2.5`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `system:STRING`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `keep_model_loaded:BOOLEAN`（1 次）
- `temperature:FLOAT`（1 次）
- `max_new_tokens:INT`（1 次）
- `seed:INT`（1 次）

## 输出

- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["You are a helpful assistant.", "", "Qwen2.5-7B-Instruct", "none", false, 0.7, 512, 1133, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
