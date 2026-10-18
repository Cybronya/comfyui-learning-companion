# IndexTTS2_Duration

## 节点类型

`IndexTTS2_Duration`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `speaker_audio:AUDIO`（1 次）
- `model_manager:INDEXTTS2_MODEL`（1 次）
- `text:STRING`（1 次）
- `duration_mode:COMBO`（1 次）
- `output_filename:STRING`（1 次）
- `speed_multiplier:FLOAT`（1 次）
- `target_duration:FLOAT`（1 次）
- `token_count:INT`（1 次）
- `prosody_preservation:FLOAT`（1 次）
- `use_fp16:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `output_path:STRING`（1 次）
- `info:STRING`（1 次）
- `actual_duration:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["这是一个时长控制的语音合成示例。我们可以精确控制语音的播放速度。", "speed_control", "indextts2_duration_output.wav", 1.0000000000000002, 14, 0, 0.8, f`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
