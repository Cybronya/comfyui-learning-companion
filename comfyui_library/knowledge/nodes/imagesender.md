# ImageSender

## 节点类型

`ImageSender`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `images:IMAGE`（8 次）
- `filename_prefix:STRING`（2 次）
- `link_id:INT`（2 次）

## 输出

- `image_urls:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ImgSender", 1]`（3 次）
- `["ImgSender", 0]`（3 次）
- `["ImgSender", 2]`（1 次）
- `["ImgSender", 3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
