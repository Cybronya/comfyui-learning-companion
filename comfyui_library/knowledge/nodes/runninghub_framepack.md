# RunningHub_FramePack

## 节点类型

`RunningHub_FramePack`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `ref_image:IMAGE`（5 次）
- `prompt:STRING`（5 次）
- `end_image:IMAGE`（3 次）
- `total_second_length:INT`（2 次）

## 输出

- `frames:IMAGE`（5 次）
- `fps:FLOAT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The girl dances energetically, leaping mid-air with fluid arm swings and quick footwork.", 5, 1030, "randomize", 25, t`（1 次）
- `["", 5, 1173, "fixed", 25, true, 1]`（1 次）
- `["The girl dances energetically, leaping mid-air with fluid arm swings and quick footwork.", 5, 879, "randomize", 25, tr`（1 次）
- `["The girl dances energetically, leaping mid-air with fluid arm swings and quick footwork.", 5, 1364, "randomize", 25, t`（1 次）
- `["The girl dances energetically, leaping mid-air with fluid arm swings and quick footwork.", 5, 631, "randomize", 25, tr`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
