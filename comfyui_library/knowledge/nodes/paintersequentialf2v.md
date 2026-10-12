# PainterSequentialF2V

## 节点类型

`PainterSequentialF2V`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `start_image:IMAGE`（2 次）
- `end_image:IMAGE`（2 次）
- `previous_video:IMAGE`（2 次）
- `positive:LIST`（2 次）
- `negative:LIST`（2 次）
- `segment_index:INT`（2 次）
- `num_segments:INT`（2 次）
- `frames_per_segment:INT`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent:LATENT`（2 次）
- `current_index:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 3, 81, 832, 480, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
