# MiniMaxH3FaceRefineWindowExtractT8Advanced

## 节点类型

`MiniMaxH3FaceRefineWindowExtractT8Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `base_frames:IMAGE`（1 次）
- `window_plan:H3_T8_FACE_REFINE_WINDOW_PLAN`（1 次）
- `source_audio:AUDIO`（1 次）
- `window_index:INT`（1 次）
- `pad_policy:COMBO`（1 次）

## 输出

- `render_frames:IMAGE`（1 次）
- `render_audio:AUDIO`（1 次）
- `window_mapping:H3_T8_FACE_REFINE_WINDOW_MAPPING`（1 次）
- `source_start_seconds:FLOAT`（1 次）
- `render_duration_seconds:FLOAT`（1 次）
- `accept_relative_ranges_json:STRING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "edge_hold_exp"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
