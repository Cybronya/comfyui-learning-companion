# WanVACEPrep

## 节点类型

`WanVACEPrep`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video_1:IMAGE`（1 次）
- `video_2:IMAGE`（1 次）

## 输出

- `control_video:IMAGE`（1 次）
- `control_mask:MASK`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `length:INT`（1 次）
- `start_images:IMAGE`（1 次）
- `end_images:IMAGE`（1 次）
- `context_frames:INT`（1 次）
- `replace_frames:INT`（1 次）
- `new_frames:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[12, 12, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
