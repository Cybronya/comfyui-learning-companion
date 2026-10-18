# RunningHubAudio8Prompt

## 节点类型

`RunningHubAudio8Prompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（13 次）
- `text:STRING`（13 次）
- `reference_text:STRING`（13 次）

## 输出

- `AUDIO8_TTS_PROMPT:AUDIO8_TTS_PROMPT`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", ""]`（8 次）
- `["嘩，前日真係好好天喎！我哋飲完早茶就出去行吓，跟住同朋友食咗個叉燒飯，大家一路傾偈一路行街，玩到夜晚先返屋企。", ""]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
