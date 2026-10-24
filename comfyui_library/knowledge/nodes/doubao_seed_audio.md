# Doubao_Seed_Audio

## 节点类型

`Doubao_Seed_Audio`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_image:IMAGE`（1 次）
- `reference_audio1:AUDIO`（1 次）
- `reference_audio2:AUDIO`（1 次）
- `reference_audio3:AUDIO`（1 次）
- `api_config:SEEDANCE_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `speaker:STRING`（1 次）
- `output_format:COMBO`（1 次）
- `sample_rate:COMBO`（1 次）
- `speech_rate:INT`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `audio_url:STRING`（1 次）
- `audio_path:STRING`（1 次）
- `task_id:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "wav", "24000", 0, 0, 0, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
