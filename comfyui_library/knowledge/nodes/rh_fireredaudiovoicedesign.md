# RH_FireRedAudioVoiceDesign

## 节点类型

`RH_FireRedAudioVoiceDesign`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `model:FIREREDAUDIO_MODEL`（15 次）
- `instruction:STRING`（15 次）
- `text:STRING`（15 次）
- `seed:INT`（14 次）
- `n_timesteps:INT`（14 次）
- `inference_cfg:FLOAT`（14 次）
- `max_new_audio_steps:INT`（14 次）
- `min_new_audio_steps:INT`（14 次）
- `max_new_text_tokens:INT`（14 次）

## 输出

- `audio:AUDIO`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 4173136006, "fixed", 20, 2, 180, 6, 1024]`（4 次）
- `["以女性高音区的清亮音色，表现出青年阶段的特质，音量略强，语速适中稍快，语调自然友好。", "这是 FireRedAudio 音色设计节点生成的示例语音。", 2, "randomize", 10, 2, 60, 6, 512]`（3 次）
- `["", "这是 FireRedAudio 音色设计节点生成的示例语音。", 3293110735, "randomize", 10, 2, 60, 6, 512]`（3 次）
- `["以女性高音区的清亮音色，表现出青年阶段的特质，音量略强，语速适中稍快，语调自然友好。", "这是 FireRedAudio 音色设计节点生成的示例语音。", 3476487999, "randomize", 10, 2, 180, 6,`（1 次）
- `[0, 10, 2, 750, 6, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
