# ImageResize

## 节点类型

`ImageResize`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pixels:IMAGE`（1 次）
- `mask_optional:MASK`（1 次）
- `action:COMBO`（1 次）
- `smaller_side:INT`（1 次）
- `larger_side:INT`（1 次）
- `scale_factor:FLOAT`（1 次）
- `resize_mode:COMBO`（1 次）
- `side_ratio:STRING`（1 次）
- `crop_pad_position:FLOAT`（1 次）
- `pad_feathering:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `MASK:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["crop to ratio", 0, 0, 0, "reduce size only", "9:16", 0.5, 20]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
