# IndexTTS2_SpeakerEmotionConfig

## 节点类型

`IndexTTS2_SpeakerEmotionConfig`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `speaker_name:STRING`（20 次）
- `emotion_mode:COMBO`（20 次）
- `emotion_audio:STRING`（20 次）
- `emotion_alpha:FLOAT`（20 次）
- `happy:FLOAT`（20 次）
- `angry:FLOAT`（20 次）
- `sad:FLOAT`（20 次）
- `fear:FLOAT`（20 次）
- `hate:FLOAT`（20 次）
- `low:FLOAT`（20 次）

## 输出

- `emotion_config:SPEAKER_EMOTION_CONFIG`（20 次）
- `info:STRING`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Student3", "emotion_vector", "", 1, 0.4, 0, 0, 0, 0, 0, 0, 0.6, "", true]`（2 次）
- `["Student1", "emotion_vector", "", 1, 0.6, 0, 0, 0, 0, 0, 0, 0.4, "", true]`（2 次）
- `["Teacher", "emotion_vector", "", 1, 0.30000000000000004, 0, 0, 0, 0, 0, 0, 0.7, "", true]`（2 次）
- `["Student2", "emotion_vector", "", 1, 0.5, 0, 0, 0, 0, 0, 0, 0.5, "", true]`（2 次）
- `["Speaker3", "emotion_vector", "", 1, 0.6, 0, 0, 0, 0, 0, 0, 0.4, "", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
