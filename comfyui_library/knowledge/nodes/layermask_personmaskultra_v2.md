# LayerMask: PersonMaskUltra V2

## 节点类型

`LayerMask: PersonMaskUltra V2`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `face:BOOLEAN`（1 次）
- `hair:BOOLEAN`（1 次）
- `body:BOOLEAN`（1 次）
- `clothes:BOOLEAN`（1 次）
- `accessories:BOOLEAN`（1 次）
- `background:BOOLEAN`（1 次）
- `confidence:FLOAT`（1 次）
- `detail_method:COMBO`（1 次）
- `detail_erode:INT`（1 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, true, false, false, false, false, 0.4, "VITMatte", 6, 6, 0.01, 0.99, true, "cuda", 2]`（1 次）
- `[true, false, false, false, false, false, 0.4, "VITMatte", 6, 6, 0.01, 0.99, true, "cuda", 2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
