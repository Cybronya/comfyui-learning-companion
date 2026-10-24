# LayerMask: ImageToMask

## 节点类型

`LayerMask: ImageToMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `channel:COMBO`（2 次）
- `black_point:INT`（2 次）
- `white_point:INT`（2 次）
- `gray_point:FLOAT`（2 次）
- `invert_output_mask:BOOLEAN`（2 次）

## 输出

- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["L(LAB)", 0, 255, 1, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
