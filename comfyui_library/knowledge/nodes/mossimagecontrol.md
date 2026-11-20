# MOSSImageControl

## 节点类型

`MOSSImageControl`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）
- `vae:VAE`（4 次）
- `color_map:IMAGE`（4 次）
- `depth_map:IMAGE`（4 次）
- `strength:FLOAT`（4 次）
- `start_percent:FLOAT`（4 次）
- `end_percent:FLOAT`（4 次）

## 输出

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.7, 0, 0.75]`（2 次）
- `[1, 0, 0.8]`（1 次）
- `[0.5, 0, 0.75]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
