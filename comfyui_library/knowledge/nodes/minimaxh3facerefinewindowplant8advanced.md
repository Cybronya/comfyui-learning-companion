# MiniMaxH3FaceRefineWindowPlanT8Advanced

## 节点类型

`MiniMaxH3FaceRefineWindowPlanT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `base_frames:IMAGE`（1 次）
- `fps:FLOAT`（1 次）
- `repair_ranges:STRING`（1 次）
- `range_mode:COMBO`（1 次）
- `context_before_frames:INT`（1 次）
- `context_after_frames:INT`（1 次）
- `min_render_frames:INT`（1 次）
- `max_render_frames:INT`（1 次）
- `scene_cut_threshold:FLOAT`（1 次）
- `overlap_policy:COMBO`（1 次）

## 输出

- `window_plan:H3_T8_FACE_REFINE_WINDOW_PLAN`（1 次）
- `repair_mask_preview:MASK`（1 次）
- `window_count:INT`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, "0-23", "frames_inclusive", 24, 42, 90, 362, 0.28, "reject", "edge_hold_exp", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
