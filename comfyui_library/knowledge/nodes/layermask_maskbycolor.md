# LayerMask: MaskByColor

## 节点类型

`LayerMask: MaskByColor`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image:IMAGE`（5 次）
- `mask:MASK`（5 次）
- `color:COLOR`（3 次）
- `color_in_HEX:STRING`（3 次）
- `threshold:INT`（3 次）
- `fix_gap:INT`（3 次）
- `fix_threshold:FLOAT`（3 次）
- `invert_mask:BOOLEAN`（3 次）

## 输出

- `mask:MASK`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#ca9c8c", "", 100, 2, 0.99, false]`（2 次）
- `["#FFFFFF", "#fe5500", 50, 2, 0.75, false]`（1 次）
- `["#fdcdaf", "", 50, 2, 0.99, false]`（1 次）
- `["#5b442a", "", 50, 2, 0.99, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
