# ACEPlusFFTProcessor

## 节点类型

`ACEPlusFFTProcessor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `reference_image:IMAGE`（3 次）
- `edit_image:IMAGE`（3 次）
- `edit_mask:MASK`（3 次）

## 输出

- `UC_IMAGE:IMAGE`（3 次）
- `C_IMAGE:IMAGE`（3 次）
- `MASK:MASK`（3 次）
- `OUT_H:INT`（3 次）
- `OUT_W:INT`（3 次）
- `SLICE_W:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 1024, 1024, "repainting", 0.8, 5120]`（2 次）
- `[true, 1280, 1024, "repainting", 0.8, 3072]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
