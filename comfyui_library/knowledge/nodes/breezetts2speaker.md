# BreezeTTS2Speaker

## 节点类型

`BreezeTTS2Speaker`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `reference_audio:AUDIO`（26 次）
- `name:STRING`（26 次）
- `audio:COMBO`（26 次）
- `audioUI:AUDIO_UI`（26 次）
- `reference_text:STRING`（26 次）
- `auto_transcribe_if_empty:BOOLEAN`（26 次）
- `instruction:STRING`（26 次）
- `cfg_scale:FLOAT`（26 次）
- `upload:AUDIOUPLOAD`（26 次）

## 输出

- `speaker:BREEZE_SPEAKER`（26 次）
- `audio:AUDIO`（26 次）
- `transcript:STRING`（26 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["阿杰", "b7fbc802e83d31aec66784d7ac4a037f0debc91850fbbf62a974aefec087b404.mp3", null, "", "", "", "", ""]`（3 次）
- `["小雨", "8645f41649c042e9e662cab5228943026de88a1f4fa8cba92dc341786a77609d.mp3", null, "", "", "", "", ""]`（3 次）
- `["安安", "e626ceedfa693f0d3ed41447fb5ca8d8d10f05d5bdc9f3883c2e74605f1bc23f.mp3", null, "", "", "", "", ""]`（3 次）
- `["安安", "e626ceedfa693f0d3ed41447fb5ca8d8d10f05d5bdc9f3883c2e74605f1bc23f.mp3", null, "", "今天难得不用工作，我一个人去了海边。坐在熟悉的咖啡店里，看着`（2 次）
- `["阿杰", "b7fbc802e83d31aec66784d7ac4a037f0debc91850fbbf62a974aefec087b404.mp3", null, "", "今天难得不用工作，我一个人去了海边。坐在熟悉的咖啡店里，看着`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
