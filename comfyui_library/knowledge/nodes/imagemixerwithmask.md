# ImageMixerWithMask

## 节点类型

`ImageMixerWithMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `bg_img:IMAGE`（1 次）
- `fg_img:IMAGE`（1 次）
- `fg_mask:MASK`（1 次）
- `x_percent:FLOAT`（1 次）
- `y_percent:FLOAT`（1 次）
- `auto_scale:BOOLEAN`（1 次）
- `long_edge_percent:FLOAT`（1 次）

## 输出

- `output_img:IMAGE`（1 次）
- `output_mask:MASK`（1 次）
- `transform_data:TRANSFORM_DATA`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[50, 50, false, 50]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
