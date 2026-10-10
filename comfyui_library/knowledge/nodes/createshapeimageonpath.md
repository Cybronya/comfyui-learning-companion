# CreateShapeImageOnPath

## 节点类型

`CreateShapeImageOnPath`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `coordinates:STRING`（1 次）
- `size_multiplier:FLOAT`（1 次）
- `shape:COMBO`（1 次）
- `frame_width:INT`（1 次）
- `frame_height:INT`（1 次）
- `shape_width:INT`（1 次）
- `shape_height:INT`（1 次）
- `shape_color:STRING`（1 次）
- `bg_color:STRING`（1 次）
- `blur_radius:FLOAT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["square", 512, 512, 16, 24, "white", "white", 0, 1, 1, 2, "black"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
