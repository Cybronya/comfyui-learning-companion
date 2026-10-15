# LTXVPreprocessMasks

## 节点类型

`LTXVPreprocessMasks`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `masks:MASK`（3 次）
- `vae:VAE`（3 次）
- `invert_input_masks:BOOLEAN`（3 次）
- `ignore_first_mask:BOOLEAN`（3 次）
- `pooling_method:COMBO`（3 次）
- `grow_mask:INT`（3 次）
- `tapered_corners:BOOLEAN`（3 次）
- `clamp_min:FLOAT`（3 次）
- `clamp_max:FLOAT`（3 次）

## 输出

- `MASK:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, true, "max", 0, true, 0.5, 1]`（2 次）
- `[false, false, "max", 0, true, 0.5, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
