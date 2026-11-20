# MiniMaxH3FaceRefineManualReviewT8Advanced

## 节点类型

`MiniMaxH3FaceRefineManualReviewT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `base_frames:IMAGE`（1 次）
- `candidate_window_frames:IMAGE`（1 次）
- `changed_mask:MASK`（1 次）
- `window_mapping:H3_T8_FACE_REFINE_WINDOW_MAPPING`（1 次）
- `decision:COMBO`（1 次）
- `accepted_subranges:STRING`（1 次）
- `confirm_accept:BOOLEAN`（1 次）
- `edge_fade_frames:INT`（1 次）

## 输出

- `review_frames:IMAGE`（1 次）
- `result_frames:IMAGE`（1 次）
- `accepted_change_mask:MASK`（1 次）
- `rejected_change_mask:MASK`（1 次）
- `accepted_frame_count:INT`（1 次）
- `rejected_frame_count:INT`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["preview_only", "0-23", false, 2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
