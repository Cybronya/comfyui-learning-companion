# BluePixelPrepareImage

## 节点类型

`BluePixelPrepareImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `target_pixels:INT`（4 次）
- `output_width:INT`（4 次）
- `output_height:INT`（4 次）

## 输出

- `reference_image:IMAGE`（4 次）
- `output_width:INT`（4 次）
- `output_height:INT`（4 次）
- `metadata:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16777216, 4096, 4096]`（3 次）
- `[8355840, 3072, 4096]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
