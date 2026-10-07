# FaceSegmentation

## 节点类型

`FaceSegmentation`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `analysis_models:ANALYSIS_MODELS`（2 次）
- `image:IMAGE`（2 次）
- `area:COMBO`（1 次）
- `grow:INT`（1 次）
- `grow_tapered:BOOLEAN`（1 次）
- `blur:INT`（1 次）

## 输出

- `mask:MASK`（2 次）
- `image:IMAGE`（2 次）
- `seg_mask:MASK`（2 次）
- `seg_image:IMAGE`（2 次）
- `x:INT`（2 次）
- `y:INT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["face", 3, false, 13]`（1 次）
- `["face+forehead (if available)", 48, false, 13]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
