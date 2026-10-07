# IndexTTSNode

## 节点类型

`IndexTTSNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（1 次）
- `text:STRING`（1 次）
- `model_version:COMBO`（1 次）
- `language:COMBO`（1 次）
- `speed:FLOAT`（1 次）
- `seed:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `repetition_penalty:FLOAT`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `seed:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["你好，这是一段测试文本。", "Index-TTS", "auto", 1, 4163189584, "randomize", 1, 0.8, 30, 10, 0, 3, 600, "auto"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
