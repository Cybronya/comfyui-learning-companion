# ACN_ReferenceControlNet

## 节点类型

`ACN_ReferenceControlNet`

## 分类

Conditioning

## 作用

ControlNet 控制类节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `reference_type:COMBO`（1 次）
- `style_fidelity:FLOAT`（1 次）
- `ref_weight:FLOAT`（1 次）

## 输出

- `CONTROL_NET:CONTROL_NET`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["reference_attn", 0.9500000000000001, 1]`（1 次）
- `["reference_attn", 0.9, 0.9]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
