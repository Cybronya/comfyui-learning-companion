# MeanCache_ZImage

## 节点类型

`MeanCache_ZImage`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `model:MODEL`（12 次）
- `preset:COMBO`（12 次）
- `cache_device:COMBO`（12 次）
- `rel_l1_thresh:FLOAT`（12 次）
- `skip_budget:FLOAT`（12 次）
- `start_step:INT`（12 次）
- `end_step:INT`（12 次）
- `enable_pssp:BOOLEAN`（12 次）
- `peak_threshold:FLOAT`（12 次）
- `debug:BOOLEAN`（12 次）

## 输出

- `Patched Model:MODEL`（12 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Custom", "cpu", 0.5, 0.4, 1, -1, true, 0.2, false, false]`（3 次）
- `["Balanced", "cpu", 0.3, 0.4, 2, -1, true, 0.15, true, false]`（1 次）
- `["Speed", "cpu", 0.5, 0.55, 1, -1, true, 0.35, true, false]`（1 次）
- `["Turbo", "cpu", 0.55, 0.6, 1, -1, true, 0.45, true, false]`（1 次）
- `["Custom", "cpu", 0.15, 0.2, 3, -1, true, 0.08, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
