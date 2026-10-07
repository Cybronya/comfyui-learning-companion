# WanVaceToVideo

## 节点类型

`WanVaceToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `control_video:IMAGE`（3 次）
- `control_masks:MASK`（3 次）
- `reference_image:IMAGE`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `length:INT`（3 次）
- `batch_size:INT`（3 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）
- `trim_latent:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, 21, 1, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
