# MiniMaxH3TaggedAudioReference

## 节点类型

`MiniMaxH3TaggedAudioReference`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `audio:AUDIO`（4 次）
- `previous:H3_TAGGED_REFERENCES`（4 次）
- `tag:STRING`（4 次）
- `timeline_mode:COMBO`（4 次）
- `align_audio_reference:BOOLEAN`（4 次）

## 输出

- `references:H3_TAGGED_REFERENCES`（4 次）
- `reference_fingerprint:STRING`（4 次）
- `status:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["voice", "source_timeline", false]`（2 次）
- `["voice", "standalone", false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
