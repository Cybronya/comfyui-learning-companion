# MiniMaxH3AudioWindowT8

## 节点类型

`MiniMaxH3AudioWindowT8`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `scene_start_seconds:FLOAT`（1 次）
- `scene_duration_seconds:FLOAT`（1 次）
- `warmup_seconds:FLOAT`（1 次）
- `cooldown_seconds:FLOAT`（1 次）
- `ensure_minimum_context:BOOLEAN`（1 次）

## 输出

- `context_audio:AUDIO`（1 次）
- `length:INT`（1 次）
- `final_trim_start_seconds:FLOAT`（1 次）
- `final_duration_seconds:FLOAT`（1 次）
- `prompt_timing_note:STRING`（1 次）
- `report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 5, 0, 0, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
