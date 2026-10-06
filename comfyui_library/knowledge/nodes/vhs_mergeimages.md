# VHS_MergeImages

## 节点类型

`VHS_MergeImages`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images_A:IMAGE`（2 次）
- `images_B:IMAGE`（2 次）
- `merge_strategy:COMBO`（2 次）
- `scale_method:COMBO`（2 次）
- `crop:COMBO`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `count:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"crop": "disabled", "merge_strategy": "match A", "scale_method": "nearest-exact"}`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
