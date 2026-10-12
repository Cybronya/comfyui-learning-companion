# SAM3Segmentation

## 节点类型

`SAM3Segmentation`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `sam3_model:SAM3_MODEL`（5 次）
- `image:IMAGE`（5 次）
- `positive_boxes:SAM3_BOXES_PROMPT`（5 次）
- `negative_boxes:SAM3_BOXES_PROMPT`（5 次）
- `positive_points:SAM3_POINTS_PROMPT`（5 次）
- `negative_points:SAM3_POINTS_PROMPT`（5 次）
- `mask_prompt:MASK`（5 次）
- `confidence_threshold:FLOAT`（5 次）
- `text_prompt:STRING`（5 次）
- `max_detections:INT`（5 次）

## 输出

- `masks:MASK`（5 次）
- `visualization:IMAGE`（5 次）
- `boxes:STRING`（5 次）
- `scores:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.15000000000000002, "", 1]`（2 次）
- `[0.2, "", 1]`（2 次）
- `[0.2, "person", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
