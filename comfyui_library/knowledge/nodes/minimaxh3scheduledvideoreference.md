# MiniMaxH3ScheduledVideoReference

## 节点类型

`MiniMaxH3ScheduledVideoReference`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `previous:H3_REFERENCE_SCHEDULE`（1 次）
- `tag:STRING`（1 次）
- `scenes:STRING`（1 次）
- `audio_tag:STRING`（1 次）
- `timeline_mode:COMBO`（1 次）

## 输出

- `schedule:H3_REFERENCE_SCHEDULE`（1 次）
- `schedule_fingerprint:STRING`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["performance", "4:6", "performance_audio", "restart_each_scene"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
