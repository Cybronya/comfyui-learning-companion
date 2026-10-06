# LayerMask: SegformerUltraV3

## 节点类型

`LayerMask: SegformerUltraV3`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `segformer_model:LS_SEGFORMER_MODEL`（2 次）
- `segformer_setting:LS_SEGFORMER_SETTING`（2 次）
- `detail_method:COMBO`（2 次）
- `detail_erode:INT`（2 次）
- `detail_dilate:INT`（2 次）
- `black_point:FLOAT`（2 次）
- `white_point:FLOAT`（2 次）
- `process_detail:BOOLEAN`（2 次）
- `max_megapixels:FLOAT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["VITMatte", 2, 2, 0.01, 0.99, true, 2]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
