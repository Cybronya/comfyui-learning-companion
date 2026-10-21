# FL_ImageOverlay

## 节点类型

`FL_ImageOverlay`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `base_image:IMAGE`（1 次）
- `overlay_image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `x_offset:INT`（1 次）
- `y_offset:INT`（1 次）
- `alignment:COMBO`（1 次）
- `resize_overlay:COMBO`（1 次）
- `blend_mode:COMBO`（1 次）
- `opacity:FLOAT`（1 次）
- `invert_mask:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, "custom", "none", "normal", 1, false, 0, "clip", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
