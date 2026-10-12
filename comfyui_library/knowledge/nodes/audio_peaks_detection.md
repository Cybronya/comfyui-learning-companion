# Audio Peaks Detection

## 节点类型

`Audio Peaks Detection`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `audio_weights:FLOAT`（1 次）

## 输出

- `peaks_weights:FLOAT`（1 次）
- `peaks_alternate_weights:FLOAT`（1 次）
- `peaks_index:STRING`（1 次）
- `peaks_count:INT`（1 次）
- `graph_peaks:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0.4, 5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
