# BatchUncrop

## 节点类型

`BatchUncrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `original_images:IMAGE`（1 次）
- `cropped_images:IMAGE`（1 次）
- `bboxes:BBOX`（1 次）
- `border_blending:FLOAT`（1 次）
- `crop_rescale:FLOAT`（1 次）
- `border_top:BOOLEAN`（1 次）
- `border_bottom:BOOLEAN`（1 次）
- `border_left:BOOLEAN`（1 次）
- `border_right:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.25, 1, true, true, true, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
