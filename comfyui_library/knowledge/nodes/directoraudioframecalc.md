# DirectorAudioFrameCalc

## 节点类型

`DirectorAudioFrameCalc`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `audio:*`（3 次）
- `fps:INT`（3 次）
- `min_frames:INT`（3 次）
- `buffer_frames:INT`（3 次）

## 输出

- `Frames:INT`（3 次）
- `Debug_Info:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[20, 20, 16]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
