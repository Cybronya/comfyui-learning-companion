# SharpPredict

## 节点类型

`SharpPredict`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:SHARP_MODEL`（1 次）
- `image:IMAGE`（1 次）
- `focal_length_mm:FLOAT`（1 次）
- `filename_prefix:STRING`（1 次）
- `max_gaussians:INT`（1 次）

## 输出

- `ply_path:STRING`（1 次）
- `extrinsics:EXTRINSICS`（1 次）
- `intrinsics:INTRINSICS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, "sharp", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
