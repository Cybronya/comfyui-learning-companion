# T8_IndexTTS25_Generate

## 节点类型

`T8_IndexTTS25_Generate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:T8_INDEXTTS25_MODEL`（1 次）
- `speaker_audio:AUDIO`（1 次）
- `emotion:T8_INDEXTTS25_EMOTION`（1 次）
- `sampling:T8_INDEXTTS25_SAMPLING`（1 次）
- `text:STRING`（1 次）
- `language:COMBO`（1 次）
- `duration_factor:FLOAT`（1 次）
- `target_duration_mode:COMBO`（1 次）
- `target_duration_seconds:FLOAT`（1 次）
- `postprocess_preset:COMBO`（1 次）

## 输出

- `生成音频:AUDIO`（1 次）
- `生成信息:STRING`（1 次）
- `全部候选音频:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["狂姐好。", "ZH", 1, "natural", 1, "off", 1, 407103254289972, "randomize", 2, "faster_whisper", "turbo", "cuda", 0.82]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
