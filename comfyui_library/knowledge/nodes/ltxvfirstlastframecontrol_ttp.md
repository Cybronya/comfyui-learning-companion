# LTXVFirstLastFrameControl_TTP

## 节点类型

`LTXVFirstLastFrameControl_TTP`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `vae:VAE`（8 次）
- `latent:LATENT`（8 次）
- `first_image:IMAGE`（8 次）
- `last_image:IMAGE`（8 次）
- `middle_frames:*`（8 次）
- `first_strength:FLOAT`（8 次）
- `last_strength:FLOAT`（8 次）

## 输出

- `latent:LATENT`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
