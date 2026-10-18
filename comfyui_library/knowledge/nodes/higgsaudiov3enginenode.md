# HiggsAudioV3EngineNode

## 节点类型

`HiggsAudioV3EngineNode`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:COMBO`（1 次）
- `device:COMBO`（1 次）
- `dtype:COMBO`（1 次）
- `attention:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `top_p:FLOAT`（1 次）
- `top_k:INT`（1 次）
- `max_new_tokens:INT`（1 次）

## 输出

- `tts_engine:TTS_ENGINE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["higgs-audio-v3-tts-4b", "auto", "auto", "sageattention", 1, 0.95, 50, 2048]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
