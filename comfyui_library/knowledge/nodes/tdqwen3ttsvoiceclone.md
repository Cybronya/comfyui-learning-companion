# TDQwen3TTSVoiceClone

## 节点类型

`TDQwen3TTSVoiceClone`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:QWEN3_TTS_MODEL`（1 次）
- `ref_audio:AUDIO`（1 次）
- `text:STRING`（1 次）
- `language:COMBO`（1 次）
- `ref_text:STRING`（1 次）
- `x_vector_only_mode:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["这是一个语音克隆测试。", "Chinese", "初音未来的声音", true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
