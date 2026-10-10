# PainterLTXVtoVideo

## 节点类型

`PainterLTXVtoVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `vae:VAE`（5 次）
- `image:IMAGE`（5 次）
- `audio_vae:VAE`（5 次）
- `width:INT`（5 次）
- `height:INT`（5 次）
- `length:INT`（5 次）
- `frame_rate:FLOAT`（5 次）
- `batch_size:INT`（5 次）

## 输出

- `latent:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[960, 544, 201, 25, 1]`（4 次）
- `[960, 544, 201, 24, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
