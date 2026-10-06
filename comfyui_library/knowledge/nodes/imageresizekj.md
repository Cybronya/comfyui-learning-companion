# ImageResizeKJ

## 节点类型

`ImageResizeKJ`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `get_image_size:IMAGE`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `upscale_method:COMBO`（3 次）
- `keep_proportion:BOOLEAN`（3 次）
- `divisible_by:INT`（3 次）
- `crop:COMBO`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[768, 768, "lanczos", false, 2, 0]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
