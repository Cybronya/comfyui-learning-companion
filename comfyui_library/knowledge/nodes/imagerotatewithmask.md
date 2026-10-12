# ImageRotateWithMask

## 节点类型

`ImageRotateWithMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `angle:FLOAT`（4 次）
- `fill_mode:COMBO`（4 次）
- `fill_color:STRING`（4 次）
- `expand:BOOLEAN`（4 次）
- `use_mask_center:BOOLEAN`（4 次）

## 输出

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[13.500000000000002, "mirror", "0.0", false, false]`（2 次）
- `[0, "mirror", "0.0", false, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
