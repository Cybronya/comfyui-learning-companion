# KSamplerTheMisto

## 节点类型

`KSamplerTheMisto`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `ae:VAE`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `controlnet_condition:ControlNetCondition`（2 次）
- `batch_size:INT`（1 次）
- `guidance:FLOAT`（1 次）
- `seed:INT`（1 次）
- `steps:INT`（1 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 4, 601386903869312, "randomize", 16]`（1 次）
- `[1, 4, 592370733942692, "randomize", 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
