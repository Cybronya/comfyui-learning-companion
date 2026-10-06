# LayerUtility: ImageBlendAdvance V3

## 节点类型

`LayerUtility: ImageBlendAdvance V3`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `layer_image:IMAGE`（2 次）
- `background_image:IMAGE`（2 次）
- `layer_mask:MASK`（2 次）
- `invert_mask:BOOLEAN`（2 次）
- `blend_mode:COMBO`（2 次）
- `opacity:INT`（2 次）
- `x_percent:FLOAT`（2 次）
- `y_percent:FLOAT`（2 次）
- `mirror:COMBO`（2 次）
- `scale:FLOAT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "normal", 70, 50, 50, "None", 1, 1, 0, "lanczos", 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
