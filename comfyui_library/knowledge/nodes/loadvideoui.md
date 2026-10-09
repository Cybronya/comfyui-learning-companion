# LoadVideoUI

## 节点类型

`LoadVideoUI`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video:STRING`（1 次）
- `start_time:FLOAT`（1 次）
- `end_time:FLOAT`（1 次）
- `duration:FLOAT`（1 次）
- `start_frame:INT`（1 次）
- `end_frame:INT`（1 次）
- `duration_frames:INT`（1 次）
- `resize_method:COMBO`（1 次）
- `custom_width:INT`（1 次）
- `custom_height:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `duration:FLOAT`（1 次）
- `frame_count:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0, 0, 0, 0, 0, 0, "maintain aspect ratio", 0, 0, 24, "seconds", 0, 0, 1, 1, null, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
