# ImageCompositeMaskedWithSwitch

## 节点类型

`ImageCompositeMaskedWithSwitch`

## 分类

Control Flow

## 作用

分支类节点：按条件选择输入（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `destination:IMAGE`（7 次）
- `source:IMAGE`（7 次）
- `mask:MASK`（7 次）
- `x:INT`（7 次）
- `y:INT`（7 次）
- `resize_source:BOOLEAN`（7 次）
- `enabled:BOOLEAN`（7 次）
- `invert_mask:BOOLEAN`（7 次）

## 输出

- `IMAGE:IMAGE`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, false, true, false]`（7 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
