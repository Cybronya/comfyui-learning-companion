# RH_RhartAudioTextToAudioSpeech28Hd

## 节点类型

`RH_RhartAudioTextToAudioSpeech28Hd`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `api_config:RH_OPENAPI_CONFIG`（2 次）
- `text:STRING`（2 次）
- `voice_id:STRING`（2 次）
- `enable_base64_output:BOOLEAN`（2 次）
- `english_normalization:BOOLEAN`（2 次）
- `pronunciation_dict:STRING`（2 次）
- `speed:FLOAT`（2 次）
- `volume:FLOAT`（2 次）
- `pitch:INT`（2 次）
- `emotion:COMBO`（2 次）

## 输出

- `audio:AUDIO`（2 次）
- `url:STRING`（2 次）
- `response:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["female-shaonv", false, true, "", 1, 1, 0, "happy", false, 42, 0, "randomize"]`（1 次）
- `["", "Wise_Woman", false, false, "", 1.0000000000000002, 1, 0, "neutral", false, 0, "fixed"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
