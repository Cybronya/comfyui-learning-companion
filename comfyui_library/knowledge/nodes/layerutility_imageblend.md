# LayerUtility: ImageBlend

## 节点类型

`LayerUtility: ImageBlend`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `background_image:IMAGE`（4 次）
- `layer_image:IMAGE`（4 次）
- `layer_mask:MASK`（4 次）
- `invert_mask:BOOLEAN`（4 次）
- `blend_mode:COMBO`（4 次）
- `opacity:INT`（4 次）

## 输出

- `image:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, "normal", 50]`（3 次）
- `[false, "normal", 100]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
