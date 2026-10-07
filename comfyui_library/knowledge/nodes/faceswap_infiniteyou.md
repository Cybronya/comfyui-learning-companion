# FaceSwap_InfiniteYou

## 节点类型

`FaceSwap_InfiniteYou`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `control_net:CONTROL_NET`（1 次）
- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `ref_image:IMAGE`（1 次）
- `image:IMAGE`（1 次）
- `vae:VAE`（1 次）
- `mask:MASK`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["aes_stage2_img_proj.bin", 1, 0, 1, 9]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
