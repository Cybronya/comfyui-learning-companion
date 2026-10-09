# WanContextWindowsManual

## 节点类型

`WanContextWindowsManual`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `context_length:INT`（1 次）
- `context_overlap:INT`（1 次）
- `context_schedule:COMBO`（1 次）
- `context_stride:INT`（1 次）
- `closed_loop:BOOLEAN`（1 次）
- `fuse_method:COMBO`（1 次）
- `freenoise:BOOLEAN`（1 次）
- `retain_first_frame:BOOLEAN`（1 次）
- `split_conds_to_windows:BOOLEAN`（1 次）

## 输出

- `MODEL:MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[121, 30, "standard_static", 1, false, "pyramid", false, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
