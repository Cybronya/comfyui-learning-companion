# RH_BytedanceDoubaoSeedAudio10

## 节点类型

`RH_BytedanceDoubaoSeedAudio10`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_url:IMAGE`（1 次）
- `audio_url1:AUDIO`（1 次）
- `audio_url2:AUDIO`（1 次）
- `audio_url3:AUDIO`（1 次）
- `api_config:RH_OPENAPI_CONFIG`（1 次）
- `text_prompt:STRING`（1 次）
- `speech_rate:INT`（1 次）
- `speaker:STRING`（1 次）
- `format:COMBO`（1 次）
- `sample_rate:STRING`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `url:STRING`（1 次）
- `response:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "mp3", "", "wav", "", 0, 0, false, 0, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
