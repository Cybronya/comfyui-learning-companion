# ImpactSimpleDetectorSEGS

## 节点类型

`ImpactSimpleDetectorSEGS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `bbox_detector:BBOX_DETECTOR`（1 次）
- `image:IMAGE`（1 次）
- `sam_model_opt:SAM_MODEL`（1 次）
- `segm_detector_opt:SEGM_DETECTOR`（1 次）
- `bbox_threshold:FLOAT`（1 次）
- `bbox_dilation:INT`（1 次）
- `crop_factor:FLOAT`（1 次）
- `drop_size:INT`（1 次）
- `sub_threshold:FLOAT`（1 次）
- `sub_dilation:INT`（1 次）

## 输出

- `SEGS:SEGS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, 0, 3, 10, 0.5, 0, 0, 0.7, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
