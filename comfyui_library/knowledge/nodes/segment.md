# Segment

## 节点类型

`Segment`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `image:IMAGE`（8 次）
- `prompt:STRING`（4 次）
- `sam_model:COMBO`（3 次）
- `dino_model:COMBO`（3 次）
- `threshold:FLOAT`（3 次）
- `mask_blur:INT`（3 次）
- `mask_offset:INT`（3 次）
- `invert_output:BOOLEAN`（3 次）
- `background:COMBO`（3 次）
- `background_color:COLOR`（2 次）

## 输出

- `IMAGE:IMAGE`（8 次）
- `MASK:MASK`（8 次）
- `MASK_IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "sam_vit_l (1.25GB)", "GroundingDINO_SwinT_OGC (694MB)", 0.3, 2, 5, false, "Alpha", "#222222"]`（1 次）
- `["person", "sam_vit_h (2.56GB)", "GroundingDINO_SwinT_OGC (694MB)", 0.3, 0, 0, false, "Alpha", "#222222"]`（1 次）
- `["top-clothes and lower-clothes", "sam_vit_h (2.56GB)", "GroundingDINO_SwinT_OGC (694MB)", 0.35, 6, 2, "Alpha", true]`（1 次）
- `["top-clothes, bottom-clothes", "sam_vit_h (2.56GB)", "GroundingDINO_SwinT_OGC (694MB)", 0.4000000000000001, 6, 2, "Alph`（1 次）
- `["", "sam_vit_h (2.56GB)", "GroundingDINO_SwinT_OGC (694MB)", 0.35, 0, 0, "Alpha", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
