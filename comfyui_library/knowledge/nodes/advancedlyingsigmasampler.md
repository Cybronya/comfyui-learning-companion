# AdvancedLyingSigmaSampler

## 节点类型

`AdvancedLyingSigmaSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `sampler:SAMPLER`（2 次）
- `dishonesty_factor:FLOAT`（1 次）
- `start_percent:FLOAT`（1 次）
- `end_percent:FLOAT`（1 次）
- `smooth_factor:FLOAT`（1 次）

## 输出

- `SAMPLER:SAMPLER`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[-0.05, 0.1, 0.9, 0.5]`（1 次）
- `[-0.10000000000000002, 0, 0.9000000000000001, 0.5000000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
