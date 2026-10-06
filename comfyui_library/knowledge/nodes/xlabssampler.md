# XlabsSampler

## 节点类型

`XlabsSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `conditioning:CONDITIONING`（6 次）
- `neg_conditioning:CONDITIONING`（6 次）
- `latent_image:LATENT`（6 次）
- `controlnet_condition:ControlNetCondition`（6 次）

## 输出

- `latent:LATENT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[802467852436685, "randomize", 20, 1, 3.5, 0, 1]`（1 次）
- `[144645277211032, "randomize", 20, 1, 3.5, 0, 1]`（1 次）
- `[987378549305391, "randomize", 20, 1, 3.5, 0, 1]`（1 次）
- `[608843965335545, "randomize", 20, 1, 3.5, 0, 1]`（1 次）
- `[110693205872683, "fixed", 20, 20, 1, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
