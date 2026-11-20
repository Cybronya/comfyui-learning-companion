# [Comfy3D] MVDream Model

## 节点类型

`[Comfy3D] MVDream Model`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `mvdream_pipe:DIFFUSERS_PIPE`（3 次）
- `reference_image:IMAGE`（3 次）
- `reference_mask:MASK`（3 次）

## 输出

- `multiview_images:IMAGE`（3 次）
- `orbit_camposes:ORBIT_CAMPOSES`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "ugly, blurry, pixelated obscure, unnatural colors, poor lighting, dull, unclear, cropped, lowres, low quality, art`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
