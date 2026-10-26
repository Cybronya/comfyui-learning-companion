# SpectrumMOSSImageAdaptive

## 节点类型

`SpectrumMOSSImageAdaptive`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `warmup_steps:INT`（3 次）
- `detail_guard_steps:INT`（3 次）
- `tail_actual_steps:INT`（3 次）
- `post_guard_horizon_cap:INT`（3 次）
- `window_size:FLOAT`（3 次）
- `flex_window:FLOAT`（3 次）
- `cache_device:COMBO`（3 次）
- `debug:BOOLEAN`（3 次）
- `error_tolerance:FLOAT`（3 次）

## 输出

- `model:MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, 8, 2, 6, 2, 0.5, "main_device", false, 1, false]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
