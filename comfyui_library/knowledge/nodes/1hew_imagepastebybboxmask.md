# 1hew_ImagePasteByBBoxMask

## 节点类型

`1hew_ImagePasteByBBoxMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `paste_image:IMAGE`（1 次）
- `base_image:IMAGE`（1 次）
- `bbox_mask:MASK`（1 次）
- `paste_mask:MASK`（1 次）
- `position_x:INT`（1 次）
- `position_y:INT`（1 次）
- `scale:FLOAT`（1 次）
- `rotation:FLOAT`（1 次）
- `opacity:FLOAT`（1 次）
- `apply_paste_mask:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 1, 0, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
