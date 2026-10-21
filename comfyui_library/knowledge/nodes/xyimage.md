# XYImage

## 节点类型

`XYImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `splits:INT`（1 次）
- `x_labels:*`（1 次）
- `y_labels:*`（1 次）
- `z_labels:*`（1 次）
- `flip_axis:COMBO`（1 次）
- `batch_stack_mode:COMBO`（1 次）
- `z_enabled:COMBO`（1 次）
- `x_main_label:STRING`（1 次）
- `y_main_label:STRING`（1 次）

## 输出

- `Image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["False", "horizontal", "False", "", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
