# QwenImage21SpectrumT8

## 节点类型

`QwenImage21SpectrumT8`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 28 个 workflow 中。

## 输入

- `model:MODEL`（28 次）
- `history:INT`（28 次）
- `degree:INT`（28 次）
- `ridge:FLOAT`（28 次）
- `guard_threshold:FLOAT`（28 次）
- `start_percent:FLOAT`（28 次）
- `end_percent:FLOAT`（28 次）
- `max_consecutive_hits:INT`（28 次）
- `cache_device:COMBO`（28 次）
- `max_cache_mb:INT`（28 次）

## 输出

- `MODEL:MODEL`（28 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[4, 2, 0.01, 0.25, 0.15, 0.85, 1, "cpu", 1024, "constant", 0.5, 0.08]`（17 次）
- `[4, 2, 0.01, 0.08, 0.1, 0.9, 1, "cpu", 1024, "constant", 0.3500000000000001, 0.25000000000000006]`（11 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
