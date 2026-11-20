# MiniMaxH3SourceMediaWindowT8

## 节点类型

`MiniMaxH3SourceMediaWindowT8`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `frames:IMAGE`（2 次）
- `source_audio:AUDIO`（2 次）
- `source_fps:FLOAT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `length:INT`（2 次）
- `start_seconds:FLOAT`（2 次）
- `short_video_policy:COMBO`（2 次）
- `short_audio_policy:COMBO`（2 次）

## 输出

- `frames:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `frame_count:INT`（2 次）
- `duration_seconds:FLOAT`（2 次）
- `report:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 480, 832, 107, 0, "hold_last_frame", "pad_silence"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
