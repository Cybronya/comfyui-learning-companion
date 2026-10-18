# SparkTTS_AudioRecorder

## 节点类型

`SparkTTS_AudioRecorder`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `recording:BOOLEAN`（2 次）
- `recording_duration:INT`（2 次）
- `sample_rate:COMBO`（2 次）
- `noise_threshold:FLOAT`（2 次）
- `smoothing_kernel_size:INT`（2 次）

## 输出

- `audio:AUDIO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 10, "48000", 0.5, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
