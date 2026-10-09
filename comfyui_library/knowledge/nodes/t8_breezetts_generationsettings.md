# T8_BreezeTTS_GenerationSettings

## 节点类型

`T8_BreezeTTS_GenerationSettings`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `max_new_tokens:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_k:INT`（2 次）
- `top_p:FLOAT`（2 次）
- `repetition_penalty:FLOAT`（2 次）
- `depth_temperature:FLOAT`（2 次）
- `depth_top_k:INT`（2 次）
- `depth_top_p:FLOAT`（2 次）
- `seed:INT`（2 次）

## 输出

- `settings:BREEZE_T8_SETTINGS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1500, 0.9, 50, 1, 1.1, 0.9, 50, 1, 618764691, "randomize"]`（1 次）
- `[1500, 0.9, 50, 1, 1.1, 0.9, 50, 1, 580608778, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
