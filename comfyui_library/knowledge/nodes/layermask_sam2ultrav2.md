# LayerMask: SAM2UltraV2

## 节点类型

`LayerMask: SAM2UltraV2`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `sam2_model:LS_SAM2_MODEL`（4 次）
- `image:IMAGE`（4 次）
- `bboxes:BBOXES`（4 次）
- `bbox_select:COMBO`（4 次）
- `select_index:STRING`（4 次）
- `detail_method:COMBO`（4 次）
- `detail_erode:INT`（4 次）
- `detail_dilate:INT`（4 次）
- `black_point:FLOAT`（4 次）
- `white_point:FLOAT`（4 次）

## 输出

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["all", "0,", "VITMatte", 6, 4, 0.15, 0.99, true, 2]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
