# SamplerEulerAncestralDancing_Experimental

## 节点类型

`SamplerEulerAncestralDancing_Experimental`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `noise_sampler_type:COMBO`（1 次）
- `eta:FLOAT`（1 次）
- `eta_dance:FLOAT`（1 次）
- `s_noise:FLOAT`（1 次）
- `leap:INT`（1 次）

## 输出

- `SAMPLER:SAMPLER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["pyramid", 1, 0.9, 1.84, 2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
