# YusuLTXDirectorGuide

## 节点类型

`YusuLTXDirectorGuide`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `latent:LATENT`（1 次）
- `guide_data:GUIDE_DATA`（1 次）
- `motion_guide_data:MOTION_GUIDE_DATA`（1 次）
- `model:MODEL`（1 次）
- `ic_lora_name:COMBO`（1 次）
- `ic_lora_strength:FLOAT`（1 次）
- `scale_by:FLOAT`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `model:MODEL`（1 次）
- `latent_downscale_factor:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["LTX2.3-22B_IC-LoRA-Cameraman_v2_14000.safetensors", 1, 1, "bicubic", 1, "center", true, false, 256, 64, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
