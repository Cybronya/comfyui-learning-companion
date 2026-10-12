# IndexTTS2_Emotion

## 节点类型

`IndexTTS2_Emotion`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `speaker_audio:AUDIO`（4 次）
- `model_manager:INDEXTTS2_MODEL`（4 次）
- `emotion_audio:AUDIO`（4 次）
- `text:STRING`（4 次）
- `emotion_mode:COMBO`（4 次）
- `output_filename:STRING`（4 次）
- `emotion_alpha:FLOAT`（4 次）
- `happy:FLOAT`（4 次）
- `angry:FLOAT`（4 次）
- `sad:FLOAT`（4 次）

## 输出

- `audio:AUDIO`（4 次）
- `output_path:STRING`（4 次）
- `info:STRING`（4 次）
- `emotion_analysis:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["AIGC中谦称 “菜”，技术硬核才是牌。若问 TTS 谁部署，寻我定教事无乖。", "audio_prompt", "indextts2_emotion_output-single.wav", 1, 0, 0, 0, 0, 0, 0, `（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
