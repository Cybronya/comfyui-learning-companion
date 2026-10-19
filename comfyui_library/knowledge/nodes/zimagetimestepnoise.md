# ZImageTimestepNoise

## 节点类型

`ZImageTimestepNoise`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `sigmas:SIGMAS`（2 次）
- `mask:MASK`（2 次）
- `mode:COMBO`（2 次）
- `noise_strength:FLOAT`（2 次）
- `seed:INT`（2 次）
- `start_percent:FLOAT`（2 次）
- `end_percent:FLOAT`（2 次）

## 输出

- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flow", 0.30000000000000004, 29784612857881, "fixed", 0, 0.30000000000000004]`（1 次）
- `["flow", 0.4000000000000001, 29784612857881, "fixed", 0, 0.33000000000000007]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
