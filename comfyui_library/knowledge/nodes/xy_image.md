# XY_Image

## 节点类型

`XY_Image`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `gap_size:INT`（1 次）
- `font_size:INT`（1 次）
- `panel_mode:COMBO`（1 次）
- `x_attr:STRING`（1 次）
- `y_attr:STRING`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `xyimage:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, 50, "XY Plot", "<1:X1>\n[43:text]='fly'\n<2:X2>\n[43:text]='man' \n<3:X3>\n[43:text]='dog'", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
