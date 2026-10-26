# VHS_Effect_v1

## 节点类型

`VHS_Effect_v1`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `luma_compression_rate:FLOAT`（1 次）
- `luma_noise_sigma:FLOAT`（1 次）
- `luma_noise_mean:FLOAT`（1 次）
- `chroma_compression_rate:FLOAT`（1 次）
- `chroma_noise_intensity:FLOAT`（1 次）
- `vertical_blur:INT`（1 次）
- `horizontal_blur:INT`（1 次）
- `border_size:FLOAT`（1 次）
- `generations:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"border_size": 2, "chroma_compression_rate": 1, "chroma_noise_intensity": 5, "generations": 3, "horizontal_blur": 3, "l`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
