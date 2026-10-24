# IPAdapterTiled

## 节点类型

`IPAdapterTiled`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `ipadapter:IPADAPTER`（3 次）
- `image:IMAGE`（3 次）
- `image_negative:IMAGE`（3 次）
- `attn_mask:MASK`（3 次）
- `clip_vision:CLIP_VISION`（3 次）
- `weight:FLOAT`（1 次）
- `weight_type:COMBO`（1 次）
- `combine_embeds:COMBO`（1 次）
- `start_at:FLOAT`（1 次）

## 输出

- `MODEL:MODEL`（3 次）
- `tiles:IMAGE`（3 次）
- `masks:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "linear", "concat", 0, 1, 0, "V only"]`（2 次）
- `[0.84, "style transfer", "concat", 0, 1, 0, "V only"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
