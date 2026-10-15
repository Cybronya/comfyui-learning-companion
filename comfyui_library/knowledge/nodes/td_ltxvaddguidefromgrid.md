# TD_LTXVAddGuideFromGrid

## 节点类型

`TD_LTXVAddGuideFromGrid`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）
- `vae:VAE`（6 次）
- `latent:LATENT`（6 次）
- `grid_image:IMAGE`（6 次）
- `columns:INT`（6 次）
- `rows:INT`（6 次）
- `frame_indices:STRING`（6 次）
- `strengths:STRING`（6 次）
- `remove_edge:BOOLEAN`（6 次）

## 输出

- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）
- `latent:LATENT`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 2, "0,96,192,287", "0.7,0.75,0.9,0.85", false, 0]`（4 次）
- `[2, 2, "0,96,192,287", "0.5,0.48,0.6,0.52", false, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
