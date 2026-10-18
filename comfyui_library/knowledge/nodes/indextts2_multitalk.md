# IndexTTS2_MultiTalk

## 节点类型

`IndexTTS2_MultiTalk`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `speaker1_audio:AUDIO`（5 次）
- `speaker2_audio:AUDIO`（5 次）
- `speaker3_audio:AUDIO`（5 次）
- `speaker4_audio:AUDIO`（5 次）
- `model_manager:INDEXTTS2_MODEL`（5 次）
- `speaker1_emotion_config:SPEAKER_EMOTION_CONFIG`（5 次）
- `speaker2_emotion_config:SPEAKER_EMOTION_CONFIG`（5 次）
- `speaker3_emotion_config:SPEAKER_EMOTION_CONFIG`（5 次）
- `speaker4_emotion_config:SPEAKER_EMOTION_CONFIG`（5 次）
- `num_speakers:COMBO`（5 次）

## 输出

- `audio:AUDIO`（5 次）
- `output_path:STRING`（5 次）
- `info:STRING`（5 次）
- `emotion_analysis:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["4", "Speaker1: Today we're going to learn about quantum physics. Who can tell me what they know?\nStudent2: Oh! I know`（2 次）
- `["4", "", "classroom_discussion.wav", "auto", 1, 0.8, 0.7, 0.9, 0.6, 0.71, true, false, true]`（1 次）
- `["4", "Speaker1: Hello, how are you today!\nSpeaker2: I'm doing great, thank you for asking!", "multi_talk_emotion_outpu`（1 次）
- `["4", "Speaker1: 快打开，跑了三家店才抢到的。​\nSpeaker2: 呀！​\nSpeaker3: 小心点姑娘。​\nSpeaker2: 谢谢叔叔！陈阳你看这手链，刻了我名字呢！​\nSpeaker4: 真精致，现在年轻人`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
