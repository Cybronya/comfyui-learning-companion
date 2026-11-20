# MiniMaxH3TemporalWindow

## 节点类型

`MiniMaxH3TemporalWindow`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `clip:CLIP`（1 次）
- `temporal_windows:BOOLEAN`（1 次）
- `window_frames:INT`（1 次）
- `overlap_frames:INT`（1 次）
- `carry_overlap:BOOLEAN`（1 次）
- `spatial_tiles:BOOLEAN`（1 次）
- `tile_width:INT`（1 次）
- `tile_height:INT`（1 次）
- `tile_overlap:INT`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 56, 5, true, false, 1024, 576, 256, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
