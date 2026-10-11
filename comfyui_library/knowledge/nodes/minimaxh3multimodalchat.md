# MiniMaxH3MultimodalChat

## 节点类型

`MiniMaxH3MultimodalChat`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `first_frame:IMAGE`（1 次）
- `last_frame:IMAGE`（1 次）
- `ref_images.ref_image_0:IMAGE`（1 次）
- `ref_images.ref_image_1:IMAGE`（1 次）
- `ref_images.ref_image_2:IMAGE`（1 次）
- `ref_videos.ref_video_0:IMAGE`（1 次）
- `ref_video_audios.ref_video_audio_0:AUDIO`（1 次）
- `ref_audios.ref_audio_0:AUDIO`（1 次）
- `ref_audios.ref_audio_1:AUDIO`（1 次）
- `user_prompt:STRING`（1 次）

## 输出

- `reply:STRING`（1 次）
- `prompt_text:STRING`（1 次）
- `chat_history:STRING`（1 次）
- `report:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "[{\"role\":\"user\",\"content\":\"这个女孩在跳舞\",\"media\":[]},{\"role\":\"assistant\",\"content\":\"subject_definition`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
