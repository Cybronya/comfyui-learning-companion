# IPAdapterClipVisionEnhancer

## 节点类型

`IPAdapterClipVisionEnhancer`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `ipadapter:IPADAPTER`（3 次）
- `image:IMAGE`（3 次）
- `image_negative:IMAGE`（3 次）
- `attn_mask:MASK`（3 次）
- `clip_vision:CLIP_VISION`（3 次）
- `end_at:FLOAT`（2 次）
- `enhance_tiles:INT`（2 次）
- `weight:FLOAT`（2 次）
- `weight_type:COMBO`（1 次）

## 输出

- `MODEL:MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "linear", "concat", 0, 1, "V only", 2, 1]`（1 次）
- `[0.88, "reverse in-out", "concat", 0, 1, "V only", 2, 1]`（1 次）
- `[0.8, "linear", "concat", 0, 1, "V only", 2, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
