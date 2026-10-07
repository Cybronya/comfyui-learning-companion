# RH_Jimeng4_Image2Image

## 节点类型

`RH_Jimeng4_Image2Image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `image3:IMAGE`（2 次）
- `image4:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `size:COMBO`（2 次）
- `sequential_image_generation:COMBO`（2 次）
- `max_images:COMBO`（2 次）
- `seed:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `image_urls:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "2K", "auto", 1, 1541845610, "randomize"]`（1 次）
- `["", "4K", "auto", 1, 753055062, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
