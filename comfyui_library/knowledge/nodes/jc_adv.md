# JC_adv

## 节点类型

`JC_adv`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `extra_options:JOYCAPTION_EXTRA_OPTIONS`（1 次）
- `model:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `prompt_style:COMBO`（1 次）
- `caption_length:COMBO`（1 次）
- `max_new_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）

## 输出

- `PROMPT:STRING`（1 次）
- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["joycaption-beta-one", "Balanced (8-bit)", "Descriptive", "short", 512, 0.6, 0.9, 0, "", "Keep in Memory"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
