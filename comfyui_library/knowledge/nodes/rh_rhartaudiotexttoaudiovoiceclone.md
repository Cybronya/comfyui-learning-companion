# RH_RhartAudioTextToAudioVoiceClone

## 节点类型

`RH_RhartAudioTextToAudioVoiceClone`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `text:STRING`（1 次）
- `custom_voice_id:STRING`（1 次）
- `need_noise_reduction:BOOLEAN`（1 次）
- `need_volume_normalization:BOOLEAN`（1 次）
- `model:COMBO`（1 次）
- `accuracy:FLOAT`（1 次）
- `language_boost:COMBO`（1 次）
- `skip_error:BOOLEAN`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["I", "MordorfRef20260914A", false, false, "speech-2.8-hd", 0.7, "English", false, 0, "fixed"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
