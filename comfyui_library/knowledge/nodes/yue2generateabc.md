# YuE2GenerateABC

## 节点类型

`YuE2GenerateABC`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `style:STRING`（1 次）
- `lyrics:STRING`（1 次）
- `seed:INT`（1 次）
- `mode:COMBO`（1 次）
- `max_abc_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `repetition_penalty:FLOAT`（1 次）

## 输出

- `abc:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 518519671787580, "randomize", "full", 8192, 0.7, 0.9, 30, 1.005, 100]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
