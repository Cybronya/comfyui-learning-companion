# ImageResizeKJv2

## 节点类型

`ImageResizeKJv2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 21 个 workflow 中。

## 输入

- `image:IMAGE`（36 次）
- `mask:MASK`（36 次）
- `width:INT`（36 次）
- `height:INT`（36 次）
- `upscale_method:COMBO`（36 次）
- `keep_proportion:COMBO`（36 次）
- `pad_color:STRING`（36 次）
- `crop_position:COMBO`（36 次）
- `divisible_by:INT`（36 次）
- `device:COMBO`（36 次）

## 输出

- `IMAGE:IMAGE`（36 次）
- `width:INT`（36 次）
- `height:INT`（36 次）
- `mask:MASK`（36 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, "lanczos", "resize", "0, 0, 0", "center", 8, "cpu"]`（13 次）
- `[2048, 2048, "nearest-exact", "resize", "0, 0, 0", "center", 2, "cpu"]`（5 次）
- `[512, 512, "lanczos", "stretch", "0, 0, 0", "center", 2, "cpu"]`（3 次）
- `[512, 512, "nearest-exact", "total_pixels", "0, 0, 0", "center", 32, "cpu"]`（2 次）
- `[1536, 1536, "lanczos", "resize", "0, 0, 0", "center", 16, "cpu"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
