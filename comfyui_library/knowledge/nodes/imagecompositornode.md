# ImageCompositorNode

## 节点类型

`ImageCompositorNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `layer_image:IMAGE`（4 次）
- `layer_mask:MASK`（4 次）
- `background_image:IMAGE`（4 次）
- `layer_x:INT`（4 次）
- `layer_y:INT`（4 次）
- `layer_scale:FLOAT`（4 次）
- `layer_opacity:FLOAT`（4 次）
- `blend_mode:COMBO`（4 次）

## 输出

- `合成图片:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 1, 1, "正常"]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
