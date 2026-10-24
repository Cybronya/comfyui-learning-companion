# workflow>IMGVE

## 节点类型

`workflow>IMGVE`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `vae_name:COMBO`（1 次）
- `model_name:COMBO`（1 次）
- `upscale_method:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `width_factor:INT`（1 次）
- `height_factor:INT`（1 次）
- `overlap_rate:FLOAT`（1 次）

## 输出

- `VAE:VAE`（1 次）
- `图像:IMAGE`（1 次）
- `POSITIONS:LIST`（1 次）
- `ORIGINAL_SIZE:TUPLE`（1 次）
- `GRID_SIZE:TUPLE`（1 次）
- `Latent:LATENT`（1 次）
- `output:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Wan2.1_VAE.pth", "4x-ClearRealityV1.pth", "lanczos", 6.000000000000001, 2, 2, 0.05000000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
