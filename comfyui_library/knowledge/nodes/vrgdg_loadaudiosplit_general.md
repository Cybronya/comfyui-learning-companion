# VRGDG_LoadAudioSplit_General

## 节点类型

`VRGDG_LoadAudioSplit_General`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（2 次）
- `trigger:*`（2 次）
- `scene_duration_seconds:FLOAT`（2 次）
- `fps:INT`（2 次）
- `folder_path:STRING`（2 次）
- `enable_auto_queue:BOOLEAN`（2 次）
- `override_chunk_index:INT`（2 次）
- `overwrite_mode:COMBO`（2 次）
- `use_humo_alignment:BOOLEAN`（2 次）
- `List_of_Scene_durations:FLOAT`（2 次）

## 输出

- `meta:DICT`（2 次）
- `total_duration:FLOAT`（2 次）
- `index:INT`（2 次）
- `frames_for_ltx:INT`（2 次）
- `start_time:STRING`（2 次）
- `end_time:STRING`（2 次）
- `instructions:STRING`（2 次）
- `total_sets:INT`（2 次）
- `frames_per_scene:INT`（2 次）
- `preroll_frames:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, 24, "VRGDG_Video0010", true, -1, "backup", false, 0, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
