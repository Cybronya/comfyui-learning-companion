# PainterI2V

## 节点类型

`PainterI2V`

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
- `clip_vision_output:CLIP_VISION_OUTPUT`（1 次）
- `start_image:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `length:INT`（1 次）
- `batch_size:INT`（1 次）
- `motion_amplitude:FLOAT`（1 次）

## 输出

- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 1, 1.15]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
