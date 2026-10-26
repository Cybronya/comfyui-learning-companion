# SAMDetectorSegmented

## 节点类型

`SAMDetectorSegmented`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `sam_model:SAM_MODEL`（2 次）
- `segs:SEGS`（2 次）
- `image:IMAGE`（2 次）
- `detection_hint:COMBO`（2 次）
- `dilation:INT`（2 次）
- `threshold:FLOAT`（2 次）
- `bbox_expansion:INT`（2 次）
- `mask_hint_threshold:FLOAT`（2 次）
- `mask_hint_use_negative:COMBO`（2 次）

## 输出

- `combined_mask:MASK`（2 次）
- `batch_masks:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["center-1", 0, 0.7000000000000002, 0, 0.7, "Small"]`（1 次）
- `["center-1", 0, 0.7800000000000001, 0, 0.7, "Small"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
