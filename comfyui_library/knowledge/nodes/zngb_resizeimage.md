# ZNGB_ResizeImage

## 节点类型

`ZNGB_ResizeImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `upscale_method:COMBO`（2 次）
- `keep_proportion:COMBO`（2 次）
- `pad_color:STRING`（2 次）
- `crop_position:COMBO`（2 次）
- `divisible_by:INT`（2 次）
- `device:COMBO`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[720, 1280, "lanczos", "stretch", "0, 0, 0", "center", 1, "cpu"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
