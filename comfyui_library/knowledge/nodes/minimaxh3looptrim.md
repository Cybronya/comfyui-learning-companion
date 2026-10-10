# MiniMaxH3LoopTrim

## 节点类型

`MiniMaxH3LoopTrim`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `state:H3_CHAIN_STATE`（1 次）
- `trim_frames:INT`（1 次）
- `fps:FLOAT`（1 次）
- `match_tail:BOOLEAN`（1 次）
- `retain_overlap_frames:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `images_with_overlap:IMAGE`（1 次）
- `overlap_frames:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 24, true, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
