# Automatic CFG - Excellent attention

## 节点类型

`Automatic CFG - Excellent attention`

## 分类

Optimization

## 作用

注意力/加速优化节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `attn_mod_for_positive_operation:ATTNMOD`（6 次）
- `attn_mod_for_negative_operation:ATTNMOD`（6 次）

## 输出

- `Parameters as string:STRING`（6 次）
- `Model:MODEL`（4 次）
- `MODEL:MODEL`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 1, true, true, true, false, true, false, false, 1, false, false, ""]`（3 次）
- `[false, 2, true, true, false, false, false, false, false, 0.4, false, false, ""]`（1 次）
- `[true, 1, true, true, false, false, true, true, true, 1, false, false, ""]`（1 次）
- `[true, 2, true, true, false, false, false, true, false, 1, false, false, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
