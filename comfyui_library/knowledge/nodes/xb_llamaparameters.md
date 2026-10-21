# XB_llamaParameters

## 节点类型

`XB_llamaParameters`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `max_tokens:INT`（2 次）
- `top_k:INT`（2 次）
- `top_p:FLOAT`（2 次）
- `min_p:FLOAT`（2 次）
- `typical_p:FLOAT`（2 次）
- `temperature:FLOAT`（2 次）
- `repeat_penalty:FLOAT`（2 次）
- `frequency_penalty:FLOAT`（2 次）
- `present_penalty:FLOAT`（2 次）
- `mirostat_mode:INT`（2 次）

## 输出

- `parameters:LLAMACPPARAMS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 30, 0.9, 0.05, 1, 0.8, 1, 0, 0, 0, 0.1, 5, -1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
