# SelfLiftSplitTransitionH3

## 节点类型

`SelfLiftSplitTransitionH3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `state:SELF_LIFT_SPLIT_STATE`（1 次）
- `upscaled_video:LATENT`（1 次）
- `model_high:MODEL`（1 次）
- `vae:VAE`（1 次）
- `mode:COMBO`（1 次）
- `rho:FLOAT`（1 次）
- `w_min:FLOAT`（1 次）
- `w_max:FLOAT`（1 次）

## 输出

- `resume_latent:LATENT`（1 次）
- `tail_sigmas:SIGMAS`（1 次）
- `model_high:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["upstream", 0, 0.5, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
