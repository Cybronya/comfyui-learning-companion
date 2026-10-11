# workflow>参数设置组

## 节点类型

`workflow>参数设置组`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（2 次）
- `vae:VAE`（2 次）
- `first_frame:IMAGE`（2 次）
- `last_frame:IMAGE`（2 次）
- `aspect_ratio:COMBO`（2 次）
- `megapixels:FLOAT`（2 次）
- `multiple:INT`（2 次）
- `value:FLOAT`（2 次）
- `expression:STRING`（2 次）
- `prompt:STRING`（2 次）

## 输出

- `FLOAT:FLOAT`（2 次）
- `BOOL:BOOLEAN`（2 次）
- `positive:CONDITIONING`（2 次）
- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["16:9 (Widescreen)", 0.4, 32, 15, "max(5, round(a * 24)) + (5 - (max(5, round(a * 24)) % 17)) % 17", "Shot 1: Rainy day`（1 次）
- `["16:9 (Widescreen)", 0.4, 32, 5, "max(5, round(a * 24)) + (5 - (max(5, round(a * 24)) % 17)) % 17", "Single continuous `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
