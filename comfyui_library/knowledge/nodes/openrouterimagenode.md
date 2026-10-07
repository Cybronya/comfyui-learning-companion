# OpenRouterImageNode

## 节点类型

`OpenRouterImageNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model.images.image_1:IMAGE`（4 次）
- `model.images.image_2:IMAGE`（2 次）
- `model.images.image_3:IMAGE`（1 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["microsoft/mai-image-2.6-flash", "ethereal fashion portrait, pastel blue and pink hair blown across a face, single dark`（1 次）
- `["microsoft/mai-image-2.6-flash", "The clothing presents a realistic 3D effect as if worn on a human figure, rotating sl`（1 次）
- `["microsoft/mai-image-2.6", "Refer to the lighting and scene of the product in Figure 2, and adjust the product in Figur`（1 次）
- `["microsoft/mai-image-2.6", "editorial adventure poster, dynamic extreme close-up wide-angle view from inside a tilting `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
