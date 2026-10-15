# SCAIL2ChunkKeyframeExtractor

## 节点类型

`SCAIL2ChunkKeyframeExtractor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `video:IMAGE`（9 次）
- `planner_summary:STRING`（9 次）
- `mode:COMBO`（9 次）
- `max_chunk_frames:INT`（9 次）
- `overlap_frames:INT`（9 次）
- `max_frames:INT`（9 次）
- `include_final_anchor:BOOLEAN`（9 次）
- `contact_sheet_columns:INT`（9 次）
- `contact_sheet_thumbnail_width:INT`（9 次）
- `boundary_anchor_mode:COMBO`（9 次）

## 输出

- `boundary_anchor_frames:IMAGE`（9 次）
- `new_chunk_start_frames:IMAGE`（9 次）
- `paired_keyframes:IMAGE`（9 次）
- `contact_sheet:IMAGE`（9 次）
- `summary:STRING`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["planner_summary", 81, 5, 0, false, 4, 256, "overlap_last_frame"]`（9 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
