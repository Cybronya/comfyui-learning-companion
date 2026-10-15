# ContextWindowsVisualizerKJ

## 节点类型

`ContextWindowsVisualizerKJ`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `frame_units:COMBO`（2 次）
- `dim:INT`（2 次）
- `temporal_downscale:INT`（2 次）
- `num_frames:INT`（2 次）
- `context_length:INT`（2 次）
- `context_overlap:INT`（2 次）
- `context_schedule:COMBO`（2 次）
- `context_stride:INT`（2 次）
- `closed_loop:BOOLEAN`（2 次）

## 输出

- `model:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["pixel", 2, 4, 73, 73, 30, "standard_uniform", 1, false, "pyramid", false, true, "", ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
