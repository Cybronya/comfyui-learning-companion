# OpenH3ICDraft

## 节点类型

`OpenH3ICDraft`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `source_fps:FLOAT`（2 次）
- `target_width:INT`（2 次）
- `target_height:INT`（2 次）
- `frame_count:INT`（2 次）
- `output_fps:INT`（2 次）
- `fit:COMBO`（2 次）
- `audio_mode:COMBO`（2 次）

## 输出

- `draft_frames:IMAGE`（2 次）
- `draft_audio:AUDIO`（2 次）
- `report:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 1344, 768, 124, 24, "cover", "passthrough"]`（1 次）
- `[24, 1344, 768, 124, 24, "cover", "trim_pad"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
