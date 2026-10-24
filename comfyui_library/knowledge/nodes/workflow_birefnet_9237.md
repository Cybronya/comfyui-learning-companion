# workflow>birefnet

## 节点类型

`workflow>birefnet`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像:IMAGE`（1 次）
- `version:COMBO`（1 次）
- `detail_method:COMBO`（1 次）
- `detail_erode:INT`（1 次）
- `detail_dilate:INT`（1 次）
- `black_point:FLOAT`（1 次）
- `white_point:FLOAT`（1 次）
- `process_detail:BOOLEAN`（1 次）
- `device:COMBO`（1 次）
- `max_megapixels:FLOAT`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `遮罩:MASK`（1 次）
- `LayerMask: SegmentAnythingUltra V2 图像:IMAGE`（1 次）
- `LayerMask: SegmentAnythingUltra V2 遮罩:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["BiRefNet-General", "VITMatte", 20, 1, 0.01, 0.05000000000000001, true, "cuda", 2, "sam_vit_h (2.56GB)", "clothes", "cu`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
