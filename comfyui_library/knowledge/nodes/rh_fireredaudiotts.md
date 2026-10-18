# RH_FireRedAudioTTS

## 节点类型

`RH_FireRedAudioTTS`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `model:FIREREDAUDIO_MODEL`（16 次）
- `prompt_audio:AUDIO`（16 次）
- `prompt_text:STRING`（16 次）
- `target_text:STRING`（16 次）
- `language:COMBO`（15 次）
- `seed:INT`（15 次）
- `n_timesteps:INT`（15 次）
- `inference_cfg:FLOAT`（15 次）
- `max_new_audio_steps:INT`（15 次）
- `min_new_audio_steps:INT`（15 次）

## 输出

- `audio:AUDIO`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "zh", 0, "fixed", 10, 2, 180, 6, 1024]`（4 次）
- `["夜色这么美， 你却只盯着别处看， 把视线移过来一点， 对， 再近一点， 今晚的时间还很长， 我们有的是耐心慢慢浪费。", "欢迎使用 FireRedAudio 零样本文本转语音工作流。", "zh", 0, "fixed", 10, 2`（3 次）
- `["", "", "zh", 0, "fixed", 10, 2, 60, 6, 512]`（3 次）
- `["", "", "zh", 0, "fixed", 10, 1.8, 280, 6, 1024]`（2 次）
- `["zh", 0, 10, 2, 750, 6, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
