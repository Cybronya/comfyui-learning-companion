# segformer_b2_clothes

## 节点类型

`segformer_b2_clothes`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `Face:BOOLEAN`（1 次）
- `Hat:BOOLEAN`（1 次）
- `Hair:BOOLEAN`（1 次）
- `Upper_clothes:BOOLEAN`（1 次）
- `Skirt:BOOLEAN`（1 次）
- `Pants:BOOLEAN`（1 次）
- `Dress:BOOLEAN`（1 次）
- `Belt:BOOLEAN`（1 次）
- `shoe:BOOLEAN`（1 次）

## 输出

- `mask_image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, true, true, true, true, true, true, true, true, true, true, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
