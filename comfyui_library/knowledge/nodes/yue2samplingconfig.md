# YuE2SamplingConfig

## 节点类型

`YuE2SamplingConfig`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `semantic_temperature:FLOAT`（2 次）
- `semantic_top_p:FLOAT`（2 次）
- `semantic_top_k:INT`（2 次）
- `semantic_repetition_penalty:FLOAT`（2 次）
- `semantic_max_tokens:INT`（2 次）
- `abc_temperature:FLOAT`（2 次）
- `abc_top_p:FLOAT`（2 次）
- `abc_top_k:INT`（2 次）
- `abc_max_tokens:INT`（2 次）

## 输出

- `sampling:YUE2_SAMPLING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0.95, 100, 1.2, 9000, 0.7, 0.9, 30, 4096]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
