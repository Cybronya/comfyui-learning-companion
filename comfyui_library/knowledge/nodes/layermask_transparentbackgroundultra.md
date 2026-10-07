# LayerMask: TransparentBackgroundUltra

## 节点类型

`LayerMask: TransparentBackgroundUltra`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（7 次）
- `model:COMBO`（7 次）
- `detail_method:COMBO`（7 次）
- `detail_erode:INT`（7 次）
- `detail_dilate:INT`（7 次）
- `black_point:FLOAT`（7 次）
- `white_point:FLOAT`（7 次）
- `process_detail:BOOLEAN`（7 次）
- `device:COMBO`（7 次）
- `max_megapixels:FLOAT`（7 次）

## 输出

- `image:IMAGE`（7 次）
- `mask:MASK`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["InSPyReNet_SwinB_Plus_Ultra.pth", "GuidedFilter", 6, 6, 0.01, 0.99, true, "cuda", 2]`（7 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
