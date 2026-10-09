# LayerMask: BiRefNetUltra

## 节点类型

`LayerMask: BiRefNetUltra`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `detail_method:COMBO`（3 次）
- `detail_erode:INT`（3 次）
- `detail_dilate:INT`（3 次）
- `black_point:FLOAT`（3 次）
- `white_point:FLOAT`（3 次）
- `process_detail:BOOLEAN`（3 次）
- `device:COMBO`（3 次）
- `max_megapixels:FLOAT`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["VITMatte", 3, 3, 0.01, 0.99, false, "cuda", 2]`（1 次）
- `["VITMatte", 5, 5, 0.01, 0.9591439856663623, true, "cuda", 2]`（1 次）
- `["VITMatte", 6, 6, 0.01, 0.99, true, "cuda", 2]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
