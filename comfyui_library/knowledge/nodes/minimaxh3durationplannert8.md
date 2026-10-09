# MiniMaxH3DurationPlannerT8

## 节点类型

`MiniMaxH3DurationPlannerT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `scene_start_seconds:FLOAT`（2 次）
- `scene_duration_seconds:FLOAT`（2 次）
- `warmup_seconds:FLOAT`（2 次）
- `cooldown_seconds:FLOAT`（2 次）
- `ensure_minimum_context:BOOLEAN`（2 次）
- `source_duration_seconds:FLOAT`（2 次）

## 输出

- `length:INT`（2 次）
- `render_duration_seconds:FLOAT`（2 次）
- `source_slice_start_seconds:FLOAT`（2 次）
- `source_slice_duration_seconds:FLOAT`（2 次）
- `final_trim_start_seconds:FLOAT`（2 次）
- `final_duration_seconds:FLOAT`（2 次）
- `prompt_timing_note:STRING`（2 次）
- `report_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 3, 0, 0, false, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
