# FullASRProcessor

## 节点类型

`FullASRProcessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `vad_threshold:FLOAT`（1 次）
- `max_silence:FLOAT`（1 次）
- `max_segment:FLOAT`（1 次）
- `enable_punctuation:BOOLEAN`（1 次）
- `enable_speaker:BOOLEAN`（1 次）
- `denoise_enable:BOOLEAN`（1 次）
- `unload_model:BOOLEAN`（1 次）
- `preset_spk_num:INT`（1 次）
- `min_voice_duration:FLOAT`（1 次）

## 输出

- `asr_result:STRING`（1 次）
- `vad_result:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, 2, 10, true, true, true, false, 0, 0.3, 12, -50]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
