# ConditioningKrea2Rebalance

## 节点类型

`ConditioningKrea2Rebalance`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `conditioning:CONDITIONING`（7 次）
- `preset:COMBO`（7 次）
- `per_layer_weights:STRING`（7 次）
- `multiplier:FLOAT`（7 次）
- `renormalize:BOOLEAN`（7 次）

## 输出

- `conditioning:CONDITIONING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["subtle", "1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.5, 5.0, 1.1, 4.0, 1.0", 1.5000000000000002, true]`（6 次）
- `["detail", "1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0", 1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
