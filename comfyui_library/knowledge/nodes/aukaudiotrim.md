# AuKAudioTrim

## 节点类型

`AuKAudioTrim`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `audio:AUDIO`（3 次）
- `start_seconds:FLOAT`（3 次）
- `end_seconds:FLOAT`（3 次）

## 输出

- `裁剪音频:AUDIO`（3 次）
- `裁剪时长（秒）:FLOAT`（3 次）
- `裁剪说明:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[31.000000000000007, 52.00000000000001]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
