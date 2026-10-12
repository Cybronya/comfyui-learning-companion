# ComfyUI_Image_Round__ImageRoundAdvanced

## 节点类型

`ComfyUI_Image_Round__ImageRoundAdvanced`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `nearest_x_override:INT`（1 次）
- `nearest_y_override:INT`（1 次）
- `split_x_override:FLOAT`（1 次）
- `split_y_override:FLOAT`（1 次）
- `pad_value_override:FLOAT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `crop_left:INT`（1 次）
- `crop_right:INT`（1 次）
- `crop_bottom:INT`（1 次）
- `crop_top:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Pad", 16, 16, 0.5, 0.5, 1, 1, 1, 0, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
