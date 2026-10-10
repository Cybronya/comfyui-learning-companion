# ClownSampler_Beta

## 节点类型

`ClownSampler_Beta`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `guides:GUIDES`（4 次）
- `options:OPTIONS`（4 次）
- `eta:FLOAT`（4 次）
- `sampler_name:COMBO`（4 次）
- `seed:INT`（4 次）
- `bongmath:BOOLEAN`（4 次）
- `options 2:OPTIONS`（2 次）
- `options 3:OPTIONS`（2 次）
- `options 4:OPTIONS`（1 次）

## 输出

- `sampler:SAMPLER`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.25, "exponential/res_2s", 94, "fixed", true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
