# VoiceBridgeASRTranscribe

## 节点类型

`VoiceBridgeASRTranscribe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_key:MODEL_KEY`（4 次）
- `audio:AUDIO`（4 次）
- `language:COMBO`（4 次）
- `context:STRING`（4 次）
- `return_timestamps:BOOLEAN`（4 次）
- `model:QWEN3_ASR_MODEL`（4 次）

## 输出

- `forced_aligns:LIST`（4 次）
- `text:STRING`（4 次）
- `language:STRING`（4 次）
- `timestamps:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "", true]`（2 次）
- `["auto", "", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
