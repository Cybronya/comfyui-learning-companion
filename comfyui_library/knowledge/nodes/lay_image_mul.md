# lay_image_mul

## 节点类型

`lay_image_mul`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `out_img:IMAGE`（1 次）
- `input_img1:IMAGE`（1 次）
- `input_img2:IMAGE`（1 次）
- `input_img3:IMAGE`（1 次）
- `long_size:INT`（1 次）
- `template:COMBO`（1 次）
- `out_text:STRING`（1 次）
- `input_text1:STRING`（1 次）
- `input_text2:STRING`（1 次）
- `input_text3:STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1200, "H21", "效果图", "人物图", "场景图", "", 60, "Alibaba-PuHuiTi-Heavy.ttf"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
