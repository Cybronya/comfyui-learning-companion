# LTXSequencer

## 节点类型

`LTXSequencer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `latent:LATENT`（3 次）
- `multi_input:IMAGE`（3 次）
- `num_images:INT`（3 次）
- `insert_mode:COMBO`（3 次）
- `frame_rate:INT`（3 次）
- `insert_frame_1:INT`（3 次）
- `insert_second_1:FLOAT`（3 次）

## 输出

- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "frames", 24, 1, 0, 0.7, 100, 2, 0.7, 170, 3, 0.7, 290, 7, 0.7, 390, 10, 0.7, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,`（2 次）
- `[0, "frames", 24, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
