# LTXVAddGuideMulti

## 节点类型

`LTXVAddGuideMulti`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `positive:CONDITIONING`（12 次）
- `negative:CONDITIONING`（12 次）
- `vae:VAE`（12 次）
- `latent:LATENT`（12 次）
- `image_1:IMAGE`（10 次）
- `image_2:IMAGE`（10 次）
- `image_3:IMAGE`（10 次）
- `image_4:IMAGE`（10 次）
- `image_5:IMAGE`（10 次）
- `frame_idx_1:INT`（10 次）

## 输出

- `positive:CONDITIONING`（12 次）
- `negative:CONDITIONING`（12 次）
- `latent:LATENT`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 1, 60, 0.5000000000000001, 120, 0.5000000000000001, 180, 1, 240, 1]`（4 次）
- `[0, 1, 60, 0.5000000000000001, 120, 0.5000000000000001, 180, 1, 1, 1]`（3 次）
- `["9", 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]`（2 次）
- `["1", 0, 1, 1, 0, 1, 0, 1, 0, 1]`（2 次）
- `["2", 0, 1, -1, 0.8, 1, 0, 1, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
