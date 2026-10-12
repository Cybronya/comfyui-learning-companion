# SegmentV2

## 节点类型

`SegmentV2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `sam_model:COMBO`（1 次）
- `dino_model:COMBO`（1 次）
- `threshold:FLOAT`（1 次）
- `mask_blur:INT`（1 次）
- `mask_offset:INT`（1 次）
- `invert_output:BOOLEAN`（1 次）
- `background:COMBO`（1 次）
- `background_color:COLOR`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `MASK_IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["person", "sam_vit_h (2.56GB)", "GroundingDINO_SwinB (938MB)", 0.12000000000000002, 0, 0, false, "Alpha", "#222222"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
