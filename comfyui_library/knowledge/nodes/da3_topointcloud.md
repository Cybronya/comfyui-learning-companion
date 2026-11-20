# DA3_ToPointCloud

## 节点类型

`DA3_ToPointCloud`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `depth_raw:IMAGE`（2 次）
- `confidence:IMAGE`（2 次）
- `intrinsics:STRING`（2 次）
- `sky_mask:MASK`（2 次）
- `source_image:IMAGE`（2 次）
- `confidence_threshold:FLOAT`（2 次）
- `downsample:INT`（2 次）
- `allow_around_1:BOOLEAN`（2 次）
- `filter_outliers:BOOLEAN`（2 次）
- `outlier_percentage:FLOAT`（2 次）

## 输出

- `pointcloud:POINTCLOUD`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.2, 1, 1, false, 5]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
