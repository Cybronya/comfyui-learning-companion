# LTXDirectorGuide

## 节点类型

`LTXDirectorGuide`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `latent:LATENT`（2 次）
- `guide_data:GUIDE_DATA`（2 次）
- `motion_guide_data:MOTION_GUIDE_DATA`（2 次）
- `model:MODEL`（2 次）
- `ic_lora_name:COMBO`（2 次）
- `ic_lora_strength:FLOAT`（2 次）
- `scale_by:FLOAT`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `model:MODEL`（2 次）
- `latent_downscale_factor:FLOAT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", 1, 0.5, "bicubic", 1, "center", true, false, 256, 64, false]`（1 次）
- `["None", 1, 1, "bicubic", 1, "center", true, false, 256, 64, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
