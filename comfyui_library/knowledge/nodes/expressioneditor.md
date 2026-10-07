# ExpressionEditor

## 节点类型

`ExpressionEditor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `src_image:IMAGE`（13 次）
- `motion_link:EDITOR_LINK`（13 次）
- `sample_image:IMAGE`（13 次）
- `add_exp:EXP_DATA`（13 次）

## 输出

- `image:IMAGE`（13 次）
- `motion_link:EDITOR_LINK`（13 次）
- `save_exp:EXP_DATA`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, 0, 0, 0, 23.5, 0, 0, 0, 0, 0, 0, 1, 1, "OnlyExpression", 1.7000000000000002, ""]`（2 次）
- `[-8, -8, 4, 0, 0, 0, 0, 0, 0, 8.1, 0, 1, 1, 1, "OnlyExpression", 1.7000000000000002, ""]`（2 次）
- `[14.600000000000001, 0, 0, 5, 15, 0, 0, 0, 0, 0, 0, 0, 1, 1, "OnlyExpression", 1.7000000000000002, ""]`（2 次）
- `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, "OnlyExpression", 1.7]`（2 次）
- `[0, 12.8, 0, 5, 0, 0, 0, 0, 120, 0, 15, -0.3, 1, 1, "OnlyExpression", 1.7000000000000002, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
