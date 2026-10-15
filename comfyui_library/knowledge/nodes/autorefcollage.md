# AutoRefCollage

## 节点类型

`AutoRefCollage`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 22 个 workflow 中。

## 输入

- `model:MODEL`（23 次）
- `clip:CLIP`（23 次）
- `image_1:IMAGE`（23 次）
- `image_2:IMAGE`（23 次）
- `image_3:IMAGE`（23 次）
- `image_4:IMAGE`（23 次）
- `image_5:IMAGE`（23 次）
- `prompt:STRING`（23 次）
- `width:INT`（23 次）
- `height:INT`（23 次）

## 输出

- `collage:IMAGE`（23 次）
- `alpha_mask:MASK`（23 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["person", 1024, 768, 0.5, "black"]`（19 次）
- `["person", 64, 1280, 0.5, "white"]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
