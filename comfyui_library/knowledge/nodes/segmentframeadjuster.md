# SegmentFrameAdjuster

## 节点类型

`SegmentFrameAdjuster`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `segment_frames:STRING`（1 次）
- `max_frames:INT`（1 次）
- `min_frames:INT`（1 次）
- `max_frames_all:INT`（1 次）

## 输出

- `每轮长度:STRING`（1 次）
- `总帧数:INT`（1 次）
- `轮数:INT`（1 次）
- `每轮index:STRING`（1 次）
- `每轮index和index+1:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 97, 25, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
