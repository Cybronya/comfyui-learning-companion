# IndexTTS2_Advanced

## 节点类型

`IndexTTS2_Advanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `speaker_audio:AUDIO`（2 次）
- `model_manager:INDEXTTS2_MODEL`（2 次）
- `text:STRING`（2 次）
- `output_filename:STRING`（2 次）
- `enable_duration_control:BOOLEAN`（2 次）
- `duration_mode:COMBO`（2 次）
- `speed_multiplier:FLOAT`（2 次）
- `target_duration:FLOAT`（2 次）
- `token_count:INT`（2 次）
- `enable_emotion_control:BOOLEAN`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `output_path:STRING`（2 次）
- `info:STRING`（2 次）
- `duration:FLOAT`（2 次）
- `emotion_analysis:STRING`（2 次）
- `synthesis_stats:DICT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["This is advanced IndexTTS2 synthesis with full control.", "indextts2_advanced_output.wav", false, "speed_control", 1.0`（1 次）
- `["This is advanced IndexTTS2 synthesis with full control.", "indextts2_advanced_output.wav", false, "speed_control", 1.0`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
