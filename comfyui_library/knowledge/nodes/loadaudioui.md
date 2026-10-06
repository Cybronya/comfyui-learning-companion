# LoadAudioUI

## 节点类型

`LoadAudioUI`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:COMBO`（2 次）
- `audioUI:AUDIO_UI`（2 次）
- `start_time:FLOAT`（2 次）
- `end_time:FLOAT`（2 次）
- `duration:FLOAT`（2 次）
- `upload:AUDIOUPLOAD`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `duration:FLOAT`（2 次）
- `filename:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["06d16104cbf732b85679781b81a4246c.mp4", null, 0, 0, 0, 14.51, ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
