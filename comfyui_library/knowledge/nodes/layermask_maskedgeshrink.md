# LayerMask: MaskEdgeShrink

## 节点类型

`LayerMask: MaskEdgeShrink`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `mask:MASK`（3 次）
- `invert_mask:BOOLEAN`（1 次）
- `shrink_level:INT`（1 次）
- `soft:INT`（1 次）
- `edge_shrink:INT`（1 次）
- `edge_reserve:INT`（1 次）

## 输出

- `mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 4, 6, 1, 25]`（1 次）
- `[false, 0, 0, 2, 100]`（1 次）
- `[false, 0, 0, 6, 100]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
