# RefineNodePasteBack

## 节点类型

`RefineNodePasteBack`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `generated_image:IMAGE`（1 次）
- `info:REFINENODE_INFO`（1 次）
- `paste_back_mode:COMBO`（1 次）
- `mask_grow:INT`（1 次）
- `blend_blur:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `paste_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mask", 3, 5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
