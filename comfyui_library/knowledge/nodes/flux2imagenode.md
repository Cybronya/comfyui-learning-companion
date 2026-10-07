# Flux2ImageNode

## 节点类型

`Flux2ImageNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model.images.image_1:IMAGE`（2 次）
- `model.images.image_2:IMAGE`（2 次）
- `model.images.image_3:IMAGE`（2 次）
- `model.images.image_4:IMAGE`（2 次）
- `model.width:INT`（1 次）
- `model.height:INT`（1 次）
- `model.images.image_5:IMAGE`（1 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Replace the current sofa with the one in Image 2, then place the character from Image 3 on the new sofa. Keep the scen`（1 次）
- `["Create a photoshoot-style group portrait with four characters, each based on the four provided reference inputs .\nArr`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
