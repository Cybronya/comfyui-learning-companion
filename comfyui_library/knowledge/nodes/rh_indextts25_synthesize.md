# RH_IndexTTS25_Synthesize

## 节点类型

`RH_IndexTTS25_Synthesize`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:INDEXTTS25_MODEL`（6 次）
- `speaker_audio:AUDIO`（6 次）
- `emotion_audio:AUDIO`（6 次）
- `text:STRING`（6 次）
- `language:COMBO`（6 次）
- `duration_factor:FLOAT`（6 次）
- `seed:INT`（6 次）
- `use_random:BOOLEAN`（6 次）
- `emotion_mode:COMBO`（6 次）
- `emotion_alpha:FLOAT`（6 次）

## 输出

- `Audio:AUDIO`（6 次）
- `Status JSON:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["大家好，欢迎使用 IndexTTS 二点五。", "JA", 1, 839404442, "randomize", false, "audio", 0.6000000000000001, "[0, 0, 0, 0, 0, 0, 0, 0`（2 次）
- `["大家好，欢迎使用 IndexTTS 二点五。", "JA", 1, 804310857, "randomize", false, "audio", 0.6000000000000001, "[0, 0, 0, 0, 0, 0, 0, 0`（2 次）
- `["大家好，欢迎使用 IndexTTS 二点五。", "JA", 1, 1348726851, "randomize", false, "audio", 0.6000000000000001, "[0, 0, 0, 0, 0, 0, 0, `（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
