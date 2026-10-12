# FaceSegment

## 节点类型

`FaceSegment`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `Skin:BOOLEAN`（2 次）
- `Nose:BOOLEAN`（2 次）
- `Eyeglasses:BOOLEAN`（2 次）
- `Left-eye:BOOLEAN`（2 次）
- `Right-eye:BOOLEAN`（2 次）
- `Left-eyebrow:BOOLEAN`（2 次）
- `Right-eyebrow:BOOLEAN`（2 次）
- `Left-ear:BOOLEAN`（2 次）
- `Right-ear:BOOLEAN`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `MASK:MASK`（2 次）
- `MASK_IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, 1024, 0, 0, false, "Alpha", "`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
