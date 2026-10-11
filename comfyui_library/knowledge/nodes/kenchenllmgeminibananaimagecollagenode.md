# KenChenLLMGeminiBananaImageCollageNode

## 节点类型

`KenChenLLMGeminiBananaImageCollageNode`

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
- `image5:IMAGE`（1 次）
- `image6:IMAGE`（1 次）
- `image7:IMAGE`（1 次）
- `max_cell_size:INT`（1 次）
- `resize_mode:COMBO`（1 次）
- `add_numbers:BOOLEAN`（1 次）

## 输出

- `collage_image:IMAGE`（1 次）
- `position_guide:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, "keep_aspect_ratio", true, 48, "top-left", "black"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
