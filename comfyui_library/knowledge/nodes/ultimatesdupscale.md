# UltimateSDUpscale

## 节点类型

`UltimateSDUpscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `vae:VAE`（2 次）
- `upscale_model:UPSCALE_MODEL`（2 次）
- `upscale_by:FLOAT`（2 次）
- `seed:INT`（2 次）
- `steps:INT`（2 次）
- `cfg:FLOAT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 298216916505304, "randomize", 2, 1, "dpmpp_2m", "sgm_uniform", 0.12, "Linear", 1024, 1024, 8, 96, "None", 1, 64, 8, `（1 次）
- `[2, 186577806567934, "randomize", 2, 1, "dpmpp_2m", "sgm_uniform", 0.12, "Linear", 1024, 1024, 8, 96, "None", 1, 64, 8, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
