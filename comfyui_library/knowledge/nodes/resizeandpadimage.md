# ResizeAndPadImage

## 节点类型

`ResizeAndPadImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `target_width:INT`（2 次）
- `target_height:INT`（2 次）
- `padding_color:COMBO`（2 次）
- `interpolation:COMBO`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2048, 2048, "black", "lanczos"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
