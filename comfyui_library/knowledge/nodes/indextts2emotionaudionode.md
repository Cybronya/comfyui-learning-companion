# IndexTTS2EmotionAudioNode

## 节点类型

`IndexTTS2EmotionAudioNode`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（1 次）
- `cache_control:DICT`（1 次）
- `emo_ref_audio:AUDIO`（1 次）
- `text:STRING`（1 次）
- `mode:COMBO`（1 次）
- `do_sample_mode:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `num_beams:INT`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `seed:INT`（1 次）
- `subtitle:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello, this is IndexTTS2.", "Auto", "on", 0.8500000000000002, 0.9000000000000001, 30, 3, 10, 0, 1815, 125, 1109505047,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
