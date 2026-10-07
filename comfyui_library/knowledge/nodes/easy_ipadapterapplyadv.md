# easy ipadapterApplyADV

## 节点类型

`easy ipadapterApplyADV`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `image:IMAGE`（1 次）
- `image_negative:IMAGE`（1 次）
- `attn_mask:MASK`（1 次）
- `clip_vision:CLIP_VISION`（1 次）
- `optional_ipadapter:IPADAPTER`（1 次）

## 输出

- `model:MODEL`（1 次）
- `images:IMAGE`（1 次）
- `masks:MASK`（1 次）
- `ipadapter:IPADAPTER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["PLUS (high strength)", 0.6, "CPU", 0.7, 1, "strong style transfer", "concat", 0, 1, "V only", "all", false, false, 0, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
