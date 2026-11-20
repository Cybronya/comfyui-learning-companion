# BFSMiniMaxH3NativeTemporal

## 节点类型

`BFSMiniMaxH3NativeTemporal`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `motion_video_index:INT`（2 次）
- `strength:FLOAT`（2 次）
- `window_seconds:FLOAT`（2 次）
- `falloff_seconds:FLOAT`（2 次）
- `max_penalty:FLOAT`（2 次）
- `attention_backend:COMBO`（2 次）
- `structure_guidance:FLOAT`（2 次）
- `structure_sigma_min:FLOAT`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 2, 0.2, 0.25, 6, "flash partitions (no compile)", 1, 0, false, ""]`（1 次）
- `[1, 2, 0.25, 0.25, 6, "flash partitions (no compile)", 1, 0, true, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
