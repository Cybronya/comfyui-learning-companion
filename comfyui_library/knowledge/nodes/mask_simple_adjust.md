# Mask_simple_adjust

## 节点类型

`Mask_simple_adjust`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_mask:MASK`（1 次）
- `smoothness:INT`（1 次）
- `mask_expand:INT`（1 次）
- `is_fill:BOOLEAN`（1 次）
- `is_invert:BOOLEAN`（1 次）
- `mask_min:FLOAT`（1 次）
- `mask_max:FLOAT`（1 次）

## 输出

- `processed_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, false, false, 0, 1.0000000000000002]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
