# LayerMask: SegmentAnythingUltra Li

## 节点类型

`LayerMask: SegmentAnythingUltra Li`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `sam_model:COMBO`（1 次）
- `grounding_dino_model:COMBO`（1 次）
- `threshold:FLOAT`（1 次）
- `detail_method:COMBO`（1 次）
- `detail_erode:INT`（1 次）
- `detail_dilate:INT`（1 次）
- `black_point:FLOAT`（1 次）
- `white_point:FLOAT`（1 次）
- `process_detail:BOOLEAN`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `mask_union:MASK`（1 次）
- `mask_list:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sam_vit_h (2.56GB)", "GroundingDINO_SwinT_OGC (694MB)", 0.3, "VITMatte", 6, 6, 0.15, 0.99, true, "face,forehead,ear", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
