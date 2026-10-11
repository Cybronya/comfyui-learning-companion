# FL_Audio_BPM_Analyzer

## 节点类型

`FL_Audio_BPM_Analyzer`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio:AUDIO`（1 次）
- `bpm_method:COMBO`（1 次）
- `half_time:BOOLEAN`（1 次）
- `beat_offset_ms:INT`（1 次）

## 输出

- `audio:AUDIO`（1 次）
- `bpm:FLOAT`（1 次）
- `beat_positions:STRING`（1 次）
- `visualization:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["beat_intervals", false, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
