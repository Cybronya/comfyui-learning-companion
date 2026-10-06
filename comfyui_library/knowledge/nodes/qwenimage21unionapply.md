# QwenImage21UnionApply

## 节点类型

`QwenImage21UnionApply`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `union_patch:MODEL_PATCH`（3 次）
- `vae:VAE`（3 次）
- `control_image:IMAGE`（3 次）
- `inpaint_image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `control_mode:COMBO`（3 次）
- `strength:FLOAT`（3 次）
- `start_percent:FLOAT`（3 次）
- `end_percent:FLOAT`（3 次）

## 输出

- `MODEL:MODEL`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Canny", 1, 0, 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
