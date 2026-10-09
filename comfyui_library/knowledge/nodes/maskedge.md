# MaskEdge

## 节点类型

`MaskEdge`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mask:MASK`（1 次）
- `dilation:INT`（1 次）
- `mode:COMBO`（1 次）
- `internal:FLOAT`（1 次）
- `external:FLOAT`（1 次）

## 输出

- `edge_mask:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, "percent", 1.2500000000000002, 1.2500000000000002]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
