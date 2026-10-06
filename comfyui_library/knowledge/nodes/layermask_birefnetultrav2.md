# LayerMask: BiRefNetUltraV2

## 节点类型

`LayerMask: BiRefNetUltraV2`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `image:IMAGE`（10 次）
- `birefnet_model:BIREFNET_MODEL`（10 次）
- `detail_method:COMBO`（10 次）
- `detail_erode:INT`（10 次）
- `detail_dilate:INT`（10 次）
- `black_point:FLOAT`（10 次）
- `white_point:FLOAT`（10 次）
- `process_detail:BOOLEAN`（10 次）
- `device:COMBO`（10 次）
- `max_megapixels:FLOAT`（10 次）

## 输出

- `image:IMAGE`（10 次）
- `mask:MASK`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["VITMatte", 4, 2, 0.01, 0.99, false, "cuda", 2]`（6 次）
- `["VITMatte", 5, 2, 0.01, 0.99, false, "cuda", 2]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
