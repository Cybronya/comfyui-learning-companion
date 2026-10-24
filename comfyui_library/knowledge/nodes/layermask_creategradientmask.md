# LayerMask: CreateGradientMask

## 节点类型

`LayerMask: CreateGradientMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `size_as:*`（7 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `gradient_side:COMBO`（1 次）
- `gradient_scale:INT`（1 次）
- `gradient_offset:INT`（1 次）
- `opacity:INT`（1 次）

## 输出

- `mask:MASK`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 512, "center", 3, 2, 100]`（3 次）
- `[512, 512, "bottom", 100, 0, 100]`（2 次）
- `[568, 512, "center", 10, 2, 100]`（1 次）
- `[512, 512, "center", 10, 0, 100]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
