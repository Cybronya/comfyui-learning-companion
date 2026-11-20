# SelfLiftSplitLowH3

## 节点类型

`SelfLiftSplitLowH3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `seed:INT`（1 次）
- `cfg:FLOAT`（1 次）
- `transition_step:INT`（1 次）
- `lowres_scale:FLOAT`（1 次）

## 输出

- `state:SELF_LIFT_SPLIT_STATE`（1 次）
- `clean_video:LATENT`（1 次）
- `positive_low:CONDITIONING`（1 次）
- `negative_low:CONDITIONING`（1 次）
- `target_width_pixels:INT`（1 次）
- `target_height_pixels:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[42, "fixed", 1, 5, 0.65]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
