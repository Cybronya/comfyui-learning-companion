# AILab_ICLoRAConcat

## 节点类型

`AILab_ICLoRAConcat`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `object_image:IMAGE`（1 次）
- `object_mask:MASK`（1 次）
- `base_image:IMAGE`（1 次）
- `base_mask:MASK`（1 次）
- `layout:COMBO`（1 次）
- `custom_size:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `OBJECT_MASK:MASK`（1 次）
- `BASE_MASK:MASK`（1 次）
- `WIDTH:INT`（1 次）
- `HEIGHT:INT`（1 次）
- `X:INT`（1 次）
- `Y:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["left-right", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
