# Image Filter Adjustments

## 节点类型

`Image Filter Adjustments`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image:IMAGE`（10 次）
- `brightness:FLOAT`（10 次）
- `contrast:FLOAT`（10 次）
- `saturation:FLOAT`（10 次）
- `sharpness:FLOAT`（10 次）
- `blur:INT`（10 次）
- `gaussian_blur:FLOAT`（10 次）
- `edge_enhance:FLOAT`（10 次）
- `detail_enhance:COMBO`（10 次）

## 输出

- `IMAGE:IMAGE`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0.9800000000000002, 0, 1.0800000000000003, 0, 0, 0, "false"]`（10 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
