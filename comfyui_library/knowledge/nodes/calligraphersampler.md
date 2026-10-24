# CalligrapherSampler

## 节点类型

`CalligrapherSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `model:CalligrapherModel`（10 次）
- `condition:CalligrapherCondition`（10 次）
- `reference_image:IMAGE`（10 次）
- `num_steps:INT`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 32, "randomize"]`（1 次）
- `[8, 62, "randomize"]`（1 次）
- `[8, 1726, "randomize"]`（1 次）
- `[8, 0, "randomize"]`（1 次）
- `[8, 1767, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
