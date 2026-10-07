# IPAdapterStyleComposition

## 节点类型

`IPAdapterStyleComposition`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `ipadapter:IPADAPTER`（1 次）
- `image_style:IMAGE`（1 次）
- `image_composition:IMAGE`（1 次）
- `image_negative:IMAGE`（1 次）
- `attn_mask:MASK`（1 次）
- `clip_vision:CLIP_VISION`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, false, "average", 0, 1, "V only"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
