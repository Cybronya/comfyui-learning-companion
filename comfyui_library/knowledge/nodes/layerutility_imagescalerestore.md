# LayerUtility: ImageScaleRestore

## 节点类型

`LayerUtility: ImageScaleRestore`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `original_size:BOX`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `mask:MASK`（3 次）
- `original_size:BOX`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "lanczos", true, 1344]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
