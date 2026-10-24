# workflow>放大器

## 节点类型

`workflow>放大器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `模型:MODEL`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）
- `VAE:VAE`（1 次）
- `model_name:COMBO`（1 次）
- `sampler_name:COMBO`（1 次）
- `scheduler:COMBO`（1 次）
- `denoise:FLOAT`（1 次）
- `mode_type:COMBO`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `image_urls:STRING`（1 次）
- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4x-ClearRealityV1.pth", "euler", "normal", 0.2, "Linear", 1024, 1024, 32, 64, "None", 1, 64, 8, 16, true, false, 2, 94`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
