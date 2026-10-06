# AudioCrop

## 节点类型

`AudioCrop`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `audio:AUDIO`（8 次）
- `start_time:STRING`（8 次）
- `end_time:STRING`（8 次）

## 输出

- `AUDIO:AUDIO`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["1:00", "1:10"]`（2 次）
- `["0:00", "0:06"]`（2 次）
- `["0:00", "0:15"]`（1 次）
- `["0:00", "0:16"]`（1 次）
- `["0:00", "0:07"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
