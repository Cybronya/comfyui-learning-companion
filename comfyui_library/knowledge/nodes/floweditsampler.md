# FlowEditSampler

## 节点类型

`FlowEditSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `seed:INT`（2 次）
- `skip_steps:INT`（1 次）
- `refine_steps:INT`（1 次）

## 输出

- `SAMPLER:SAMPLER`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 24, 0, "fixed"]`（3 次）
- `[4, 24, 922020591296079, "randomize"]`（1 次）
- `[3, 0, 626929240309393, "increment"]`（1 次）
- `[1, 1, 775550780339886, "fixed"]`（1 次）
- `[2, 10, 496196499060820, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
