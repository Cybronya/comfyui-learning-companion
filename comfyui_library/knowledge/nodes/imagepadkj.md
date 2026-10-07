# ImagePadKJ

## 节点类型

`ImagePadKJ`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `target_width:INT`（2 次）
- `target_height:INT`（2 次）
- `left:INT`（2 次）
- `right:INT`（2 次）
- `top:INT`（2 次）
- `bottom:INT`（2 次）
- `extra_padding:INT`（2 次）
- `pad_mode:COMBO`（2 次）

## 输出

- `images:IMAGE`（2 次）
- `masks:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0, 80, 0, "edge", "0, 0, 0"]`（1 次）
- `[0, 0, 0, 60, 0, "edge", "0, 0, 0"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
