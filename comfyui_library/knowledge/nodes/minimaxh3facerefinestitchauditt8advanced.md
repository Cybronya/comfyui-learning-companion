# MiniMaxH3FaceRefineStitchAuditT8Advanced

## 节点类型

`MiniMaxH3FaceRefineStitchAuditT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `base_frames:IMAGE`（2 次）
- `refined_crops:IMAGE`（2 次）
- `face_plan:H3_T8_FACE_REFINE_PLAN`（2 次）
- `paste_region:COMBO`（2 次）
- `feather_source_px:FLOAT`（2 次）
- `blend_strength:FLOAT`（2 次）
- `color_match_strength:FLOAT`（2 次）
- `max_face_mean_abs_delta:FLOAT`（2 次）
- `fallback_neighbor_frames:INT`（2 次）
- `processing_device:COMBO`（2 次）

## 输出

- `candidate_frames:IMAGE`（2 次）
- `changed_mask:MASK`（2 次）
- `fallback_mask:MASK`（2 次）
- `fallback_count:INT`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ellipse", 12, 1, 0.65, 0.4, 1, "cpu_memory_safe"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
