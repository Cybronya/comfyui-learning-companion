# MiniMaxH3LatentUpscaleWithModel

## 节点类型

`MiniMaxH3LatentUpscaleWithModel`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model:LATENT_UPSCALE_MODEL`（7 次）
- `samples:LATENT`（7 次）
- `width:INT`（7 次）
- `height:INT`（7 次）

## 输出

- `LATENT:LATENT`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2560, 1440]`（7 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
