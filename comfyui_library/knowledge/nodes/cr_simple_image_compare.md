# CR Simple Image Compare

## 节点类型

`CR Simple Image Compare`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image1:IMAGE`（2 次）
- `image2:IMAGE`（2 次）
- `text1:STRING`（1 次）
- `text2:STRING`（1 次）
- `footer_height:INT`（1 次）
- `font_name:COMBO`（1 次）
- `font_size:INT`（1 次）
- `mode:COMBO`（1 次）
- `border_thickness:INT`（1 次）

## 输出

- `image:IMAGE`（2 次）
- `show_help:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["openflux1", "flux1", 100, "AlumniSansCollegiateOne-Regular.ttf", 50, "normal", 20]`（1 次）
- `["Krea2", "Z-image", 100, "01HomuraM-ExtraLight-2.otf", 50, "normal", 20]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
