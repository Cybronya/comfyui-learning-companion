# Image_Resize2

## 节点类型

`Image_Resize2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `cut_by_mask:MASK`（2 次）
- `get_image_size:IMAGE`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `keep_ratio:BOOLEAN`（2 次）
- `divisible_by:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, false, 2]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
