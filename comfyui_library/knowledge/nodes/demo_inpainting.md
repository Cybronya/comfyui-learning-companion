# 呆毛Demo_Inpainting

## 节点类型

`呆毛Demo_Inpainting`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `vae:VAE`（3 次）
- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `positive_cond:CONDITIONING`（3 次）
- `negative_cond:CONDITIONING`（3 次）
- `cfg:FLOAT`（2 次）
- `non_redraw_strength:FLOAT`（2 次）
- `redraw_strength:FLOAT`（2 次）
- `steps:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 0.10000000000000002, 0.9000000000000001, 40, true, "flux", 816524202667346, "randomize"]`（1 次）
- `[1, 0.10000000000000002, 0.9000000000000001, 40, true, "flux", 542921401905774, "randomize"]`（1 次）
- `[1, 0.10000000000000002, 0.9000000000000001, 40, true, "flux", 580603248231558, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
