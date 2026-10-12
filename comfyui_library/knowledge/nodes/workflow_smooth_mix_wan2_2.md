# workflow>SMOOTH MIX-WAN2.2

## 节点类型

`workflow>SMOOTH MIX-WAN2.2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `UNETLoader unet_name:COMBO`（1 次）
- `UNETLoader weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `CLIPVisionLoader clip_name:COMBO`（1 次）
- `vae_name:COMBO`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `VAE:VAE`（1 次）
- `MODEL:MODEL`（1 次）
- `ModelPatchTorchSettings MODEL:MODEL`（1 次）
- `CLIP_VISION_OUTPUT:CLIP_VISION_OUTPUT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["smoothMixWan22I2V14B_i2vHigh.safetensors", "default", "smoothMixWan22I2V14B_i2vLow.safetensors", "default", "umt5_xxl_`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
