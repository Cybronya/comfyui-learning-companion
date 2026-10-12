# APersonMaskGenerator

## 节点类型

`APersonMaskGenerator`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `images:IMAGE`（6 次）
- `face_mask:BOOLEAN`（3 次）
- `background_mask:BOOLEAN`（3 次）
- `hair_mask:BOOLEAN`（3 次）
- `body_mask:BOOLEAN`（3 次）
- `clothes_mask:BOOLEAN`（3 次）
- `confidence:FLOAT`（3 次）

## 输出

- `masks:MASK`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, false, false, false, 0.30000000000000004]`（3 次）
- `[true, false, false, false, false, 0.4000000000000001]`（1 次）
- `[false, false, false, true, true, 0.4000000000000001]`（1 次）
- `[true, false, true, false, false, 0.4000000000000001]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
