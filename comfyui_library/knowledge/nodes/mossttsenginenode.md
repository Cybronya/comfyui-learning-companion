# MossTTSEngineNode

## 节点类型

`MossTTSEngineNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `speaker2_voice:*`（1 次）
- `speaker3_voice:*`（1 次）
- `speaker4_voice:*`（1 次）
- `speaker5_voice:*`（1 次）
- `model_variant:COMBO`（1 次）
- `multi_speaker_mode:COMBO`（1 次）
- `device:COMBO`（1 次）
- `language:COMBO`（1 次）
- `duration_tokens:INT`（1 次）
- `sampler_preset:COMBO`（1 次）

## 输出

- `TTS_engine:TTS_ENGINE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["8B (Delay)", "Custom Character Switching", "auto", "Auto", 0, "Model default", 1, 0.95, 50, 1.1, 4096, 0, "", "", "", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
