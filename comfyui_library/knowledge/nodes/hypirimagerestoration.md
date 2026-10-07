# HYPIRImageRestoration

## 节点类型

`HYPIRImageRestoration`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `model:COMBO`（1 次）
- `hypir_weight:COMBO`（1 次）
- `prompt:STRING`（1 次）
- `upscale_factor:INT`（1 次）
- `preset_config:COMBO`（1 次）
- `lora_rank:INT`（1 次）
- `model_t:INT`（1 次）
- `coeff_t:INT`（1 次）

## 输出

- `restored_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["stable-diffusion-2-1-base", "HYPIR_sd2.pth", "high quality, detailed, sharp, clear", 2, "快速修复", 256, 200, 200]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
