# BodySegment

## 节点类型

`BodySegment`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `Hair:BOOLEAN`（1 次）
- `Glasses:BOOLEAN`（1 次）
- `Top-clothes:BOOLEAN`（1 次）
- `Bottom-clothes:BOOLEAN`（1 次）
- `Torso-skin:BOOLEAN`（1 次）
- `Face:BOOLEAN`（1 次）
- `Left-arm:BOOLEAN`（1 次）
- `Right-arm:BOOLEAN`（1 次）
- `Left-leg:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）
- `MASK_IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, false, false, false, true, false, false, false, false, false, false, 0, 0, false, "Color", "#363636"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
