# MiniMaxH3DirectorSelfLift

## 节点类型

`MiniMaxH3DirectorSelfLift`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model_hires:MODEL`（3 次）
- `bd_grp_selflift_sample:BDGROUP`（3 次）
- `split_mode:COMBO`（3 次）
- `highres_steps:INT`（3 次）
- `transition_step:INT`（3 次）
- `lowres_scale:FLOAT`（3 次）
- `sampler_mode:COMBO`（3 次）
- `native_low_carry:BOOLEAN`（3 次）
- `bd_grp_selflift_lift:BDGROUP`（3 次）
- `latent_upscale_model:COMBO`（3 次）

## 输出

- `selflift:MMX_DIR_SELFLIFT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["渐进采样", "highres_steps", 2, 6, 0.5, "euler", true, "提升 / 3D", "minimax_h3_latent_upscaler_3d_bf16.safetensors", "biline`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
