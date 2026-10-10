# MiniMaxH3ContextIR

## 节点类型

`MiniMaxH3ContextIR`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `first_frame:IMAGE`（2 次）
- `last_frame:IMAGE`（2 次）
- `ref_images.ref_image_0:IMAGE`（2 次）
- `ref_videos.ref_video_0:IMAGE`（2 次）
- `ref_video_audios.ref_video_audio_0:AUDIO`（2 次）
- `ref_audios.ref_audio_0:AUDIO`（2 次）
- `mode:COMBO`（2 次）
- `text:STRING`（2 次）
- `duration:FLOAT`（2 次）
- `ratio:COMBO`（2 次）

## 输出

- `enhanced_prompt:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["t2va", "", 5, "16:9", "", "cn", ""]`（1 次）
- `["r2va", "", 5, "16:9", "", "cn", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
