# WanDancerEncodeAudio

## 节点类型

`WanDancerEncodeAudio`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 12 个 workflow 中。

## 输入

- `audio:AUDIO`（24 次）
- `video_frames:INT`（24 次）
- `audio_inject_scale:FLOAT`（24 次）

## 输出

- `audio_encoder_output:AUDIO_ENCODER_OUTPUT`（24 次）
- `fps_string:STRING`（24 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[149, 1]`（24 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
