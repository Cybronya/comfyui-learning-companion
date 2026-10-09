# QwenVisionNode

## 节点类型

`QwenVisionNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `api_token:STRING`（2 次）
- `model:STRING`（2 次）
- `max_tokens:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `seed:INT`（2 次）

## 输出

- `description:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["详细描述一下这张图片", "", "Qwen/Qwen3-VL-235B-A22B-Instruct", 2500, 0.7, 1963483399, "randomize"]`（1 次）
- `["详细描述一下这张图片", "", "Qwen/Qwen3-VL-235B-A22B-Instruct", 2500, 0.7, 1237189574, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
