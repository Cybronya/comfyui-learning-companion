# YusuLoadAudioUI

## 节点类型

`YusuLoadAudioUI`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:COMBO`（3 次）
- `start_time:FLOAT`（3 次）
- `end_time:FLOAT`（3 次）
- `duration:FLOAT`（3 次）
- `audioUI:AUDIO_UI`（3 次）
- `upload:AUDIOUPLOAD`（3 次）

## 输出

- `audio:AUDIO`（3 次）
- `duration:FLOAT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["531c0355b5c67f1ca0d503285fbbeff3babf4529af6bb30bba6a7b03e70e3d18.mp3", 9, 12.5, 3.5, "", ""]`（1 次）
- `["7f4d0a8fb8fa56a2783750b7054742e2faffda9874dee3946a8c693216e52ba4.mp3", 9, 12.5, 3.5, "", ""]`（1 次）
- `["none", 0, 0, 0, "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
