# SamplerLCMCycle

## 节点类型

`SamplerLCMCycle`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `euler_steps:INT`（1 次）
- `lcm_steps:INT`（1 次）
- `tweak_sigmas:BOOLEAN`（1 次）
- `ancestral:FLOAT`（1 次）

## 输出

- `SAMPLER:SAMPLER`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 2, false, 0]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
