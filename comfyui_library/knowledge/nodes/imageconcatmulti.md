# ImageConcatMulti

## 节点类型

`ImageConcatMulti`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 11 个 workflow 中。

## 输入

- `image_1:IMAGE,MASK`（13 次）
- `image_2:IMAGE,MASK`（13 次）
- `inputcount:INT`（13 次）
- `direction:COMBO`（13 次）
- `match_image_size:BOOLEAN`（13 次）
- `image_3:IMAGE,MASK`（7 次）
- `image_4:IMAGE,MASK`（2 次）
- `image_5:IMAGE,MASK`（2 次）
- `image_6:IMAGE,MASK`（2 次）
- `image_3:IMAGE`（1 次）

## 输出

- `output:*`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[3, "right", true, null]`（5 次）
- `[2, "right", true, null]`（2 次）
- `[2, "down", true, null]`（2 次）
- `[6, "right", true, null]`（2 次）
- `[2, "right", false, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
