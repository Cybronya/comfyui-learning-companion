# SegmDetectorSEGS

## 节点类型

`SegmDetectorSEGS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `segm_detector:SEGM_DETECTOR`（2 次）
- `image:IMAGE`（2 次）
- `detailer_hook:DETAILER_HOOK`（2 次）
- `threshold:FLOAT`（2 次）
- `dilation:INT`（2 次）
- `crop_factor:FLOAT`（2 次）
- `drop_size:INT`（2 次）
- `labels:STRING`（2 次）

## 输出

- `SEGS:SEGS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.5, 10, 3, 10, "all"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
