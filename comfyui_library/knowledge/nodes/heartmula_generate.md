# HeartMuLa_Generate

## 节点类型

`HeartMuLa_Generate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `lyrics:STRING`（1 次）
- `tags:STRING`（1 次）
- `version:COMBO`（1 次）
- `seed:INT`（1 次）
- `max_audio_length_ms:INT`（1 次）
- `topk:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `cfg_scale:FLOAT`（1 次）

## 输出

- `audio_output:AUDIO`（1 次）
- `filepath:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[Verse]\n闭上双眼让喧嚣都停摆\n窗外的风轻轻穿过那片海\n心里的尘埃慢慢落下来\n此刻只有呼吸还在\n\n[Prechorus]\n不需要寻找繁复的答案\n只需要点亮微弱的烛光\n某种力量在悄然生长\n\n[Chorus]\n`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
