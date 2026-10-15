# LTXVContextWindows

## 节点类型

`LTXVContextWindows`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `context_length:INT`（6 次）
- `context_overlap:INT`（6 次）
- `context_schedule:COMBO`（6 次）
- `context_stride:INT`（6 次）
- `closed_loop:BOOLEAN`（6 次）
- `fuse_method:COMBO`（6 次）
- `freenoise:BOOLEAN`（6 次）
- `retain_first_frame:BOOLEAN`（6 次）
- `split_conds_to_windows:BOOLEAN`（6 次）

## 输出

- `MODEL:MODEL`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[185, 48, "standard_uniform", 1, false, "pyramid", true, 1, false]`（2 次）
- `[121, 32, "standard_static", 1, false, "pyramid", true, true, false]`（2 次）
- `[177, 72, "standard_uniform", 1, false, "pyramid", true, true, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
