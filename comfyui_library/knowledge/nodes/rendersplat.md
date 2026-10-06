# RenderSplat

## 节点类型

`RenderSplat`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `splat:SPLAT`（3 次）
- `bg_image:IMAGE`（3 次）
- `camera_info:LOAD3D_CAMERA`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `frames:INT`（3 次）
- `splat_scale:FLOAT`（3 次）
- `sharpen:FLOAT`（3 次）
- `headlight_shading:FLOAT`（3 次）
- `opacity_threshold:FLOAT`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, 1, 1, 2, 0, 0, "color", "#848484"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
