# HYMotionGenerate

## 节点类型

`HYMotionGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `network:HYMOTION_NET`（4 次）
- `conditioning:HYMOTION_COND`（4 次）
- `duration:FLOAT`（4 次）
- `seed:INT`（4 次）
- `cfg_scale:FLOAT`（4 次）
- `num_samples:INT`（4 次）

## 输出

- `motion_data:HYMOTION_DATA`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[5, 1887865463, "randomize", 5, 1]`（1 次）
- `[12, 135792760, "randomize", 5, 1]`（1 次）
- `[12, 1022273219, "randomize", 5, 1]`（1 次）
- `[12, 2997381, "randomize", 5, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
