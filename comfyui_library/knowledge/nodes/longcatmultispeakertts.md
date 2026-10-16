# LongCatMultiSpeakerTTS

## 节点类型

`LongCatMultiSpeakerTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_path:COMBO`（1 次）
- `text:STRING`（1 次）
- `steps:INT`（1 次）
- `guidance_strength:FLOAT`（1 次）
- `guidance_method:COMBO`（1 次）
- `device:COMBO`（1 次）
- `dtype:COMBO`（1 次）
- `attention:COMBO`（1 次）
- `seed:INT`（1 次）
- `pause_after_speaker:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["LongCat-AudioDiT-3.5B-bf16", "[speaker_1]: Hello, I'm speaker one.\n[speaker_2]: And I'm speaker two!", 32, 4, "apg", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
