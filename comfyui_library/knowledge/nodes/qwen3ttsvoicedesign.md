# Qwen3TTSVoiceDesign

## 节点类型

`Qwen3TTSVoiceDesign`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:QWEN3_TTS_MODEL`（1 次）
- `文本:STRING`（1 次）
- `提示词:STRING`（1 次）
- `语言:COMBO`（1 次）
- `自动卸载模型:BOOLEAN`（1 次）
- `最大生成Token数:INT`（1 次）
- `seed:INT`（1 次）
- `语速:FLOAT`（1 次）
- `批量模式:BOOLEAN`（1 次）
- `top_p:FLOAT`（1 次）

## 输出

- `音频:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello, this is a test.", "A young female voice, energetic and bright.", "自动", false, 2048, 1, "固定", 1, false, 0.8, 50,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
