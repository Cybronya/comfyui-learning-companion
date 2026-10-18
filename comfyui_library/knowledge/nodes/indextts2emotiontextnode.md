# IndexTTS2EmotionTextNode

## 节点类型

`IndexTTS2EmotionTextNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（1 次）
- `text:STRING`（1 次）
- `mode:COMBO`（1 次）
- `do_sample_mode:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `num_beams:INT`（1 次）
- `repetition_penalty:FLOAT`（1 次）
- `length_penalty:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `seed:INT`（1 次）
- `subtitle:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["IndexTTS 正式发布1.5 版本了，效果666,\n晕XUAN4是一种GAN3觉,\n我爱你！,\nI love you!,\n“我爱你”的英语是“I love you”,\n2.5平方电线,\n共465篇，约315万字,\n20`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
