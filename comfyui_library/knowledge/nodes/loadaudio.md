# LoadAudio

## 节点类型

`LoadAudio`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 22 个 workflow 中。

## 输入

- `audio:COMBO`（38 次）
- `audioUI:AUDIO_UI`（38 次）
- `upload:AUDIOUPLOAD`（38 次）

## 输出

- `AUDIO:AUDIO`（38 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["None", null, null]`（16 次）
- `["000) 跳舞 (2).mp4", null, null]`（9 次）
- `["123.flac", null, null]`（8 次）
- `["7c373294d8fe1ea7e73d00c7eb0a60e41f29796c9b85e1171045f463d5363b4a.wav", null, null]`（1 次）
- `["a867c859f1f22956b0ae36e2b4d7e9c94f5e082b6f8231ca28144292c1f481da.mp3", null, null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
