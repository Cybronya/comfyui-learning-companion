# FaceCombine

## 节点类型

`FaceCombine`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `control_net:CONTROL_NET`（3 次）
- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `ref_image_1:IMAGE`（3 次）
- `ref_image_2:IMAGE`（3 次）
- `latent_image:LATENT`（3 次）
- `vae:VAE`（3 次）

## 输出

- `MODEL:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["aes_stage2_img_proj.bin", "CUDA", 0.6000000000000001, 0.6000000000000001, 0.10000000000000002, 0.7000000000000002, fal`（2 次）
- `["sim_stage1_img_proj.bin", "CUDA", 0.6000000000000001, 0.5500000000000002, 0.10000000000000002, 0.7000000000000002, fal`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
