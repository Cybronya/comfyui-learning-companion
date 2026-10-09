# AILab_ImageStitch

## 节点类型

`AILab_ImageStitch`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `stitch_mode:COMBO`（1 次）
- `match_image_size:BOOLEAN`（1 次）
- `megapixels:FLOAT`（1 次）
- `max_width:INT`（1 次）
- `max_height:INT`（1 次）
- `upscale_method:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `WIDTH:INT`（1 次）
- `HEIGHT:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["up", false, 0, 0, 0, "lanczos", 0, "#969696"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
