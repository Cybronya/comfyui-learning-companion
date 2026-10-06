# H3InjectSchedule

## 节点类型

`H3InjectSchedule`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（4 次）
- `scheduler:COMBO`（4 次）
- `total_steps:INT`（4 次）
- `inject:FLOAT`（4 次）
- `preset:COMBO`（4 次）

## 输出

- `SIGMAS:SIGMAS`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["beta", 8, 0.7, "custom"]`（2 次）
- `["beta", 4, 0.7, "custom"]`（1 次）
- `["beta", 4, 0.6, "custom"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
