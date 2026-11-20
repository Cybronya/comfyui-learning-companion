# DreamIDV_Sampler_Wrapper_TTP

## 节点类型

`DreamIDV_Sampler_Wrapper_TTP`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `dreamidv_wrapper:DREAMIDV_WRAPPER`（1 次）
- `vae:VAE`（1 次）
- `pose_video:IMAGE`（1 次）
- `ref_video:IMAGE`（1 次）
- `ref_image:IMAGE`（1 次）
- `mask_video:IMAGE`（1 次）
- `size:COMBO`（1 次）
- `frame_num:INT`（1 次）
- `steps:INT`（1 次）
- `cfg_scale:FLOAT`（1 次）

## 输出

- `samples:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["custom", 81, 12, 2.5, 5, 107, "fixed", true, true, 512, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
