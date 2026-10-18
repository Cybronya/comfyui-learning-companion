# IndexTTS2BaseNode

## 节点类型

`IndexTTS2BaseNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（3 次）
- `cache_control:DICT`（3 次）
- `text:STRING`（3 次）
- `mode:COMBO`（3 次）
- `do_sample_mode:COMBO`（3 次）
- `temperature:FLOAT`（3 次）
- `top_p:FLOAT`（3 次）
- `top_k:INT`（3 次）
- `num_beams:INT`（3 次）
- `repetition_penalty:FLOAT`（3 次）

## 输出

- `audio:AUDIO`（3 次）
- `seed:INT`（3 次）
- `subtitle:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello everyone. I'm SevenFading. Today I'm sharing an AI image generation tool with you.", "Auto", "on", 0.8, 0.9, 30,`（1 次）
- `["Hello everyone. I'm SevenFading. Today I'm sharing an AI image generation tool with you.", "Auto", "on", 0.8, 0.9, 30,`（1 次）
- `["Hello, this is IndexTTS2.", "Auto", "on", 0.8, 0.9, 30, 3, 10, 0, 1815, 120, 72146654, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
