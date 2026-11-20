# MaskColorReplaceAdvanced

## 节点类型

`MaskColorReplaceAdvanced`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mask:MASK`（1 次）
- `background_image:IMAGE`（1 次）
- `color_hex:STRING`（1 次）
- `blend_mode:COMBO`（1 次）
- `opacity:FLOAT`（1 次）
- `feather:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#FF0000", "replace", 0.30000000000000004, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
