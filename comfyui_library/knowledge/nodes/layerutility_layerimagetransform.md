# LayerUtility: LayerImageTransform

## 节点类型

`LayerUtility: LayerImageTransform`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `x:INT`（2 次）
- `y:INT`（2 次）
- `mirror:COMBO`（2 次）
- `scale:FLOAT`（2 次）
- `aspect_ratio:FLOAT`（2 次）
- `rotate:FLOAT`（2 次）
- `transform_method:COMBO`（2 次）
- `anti_aliasing:INT`（2 次）

## 输出

- `image:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, 0, "None", 1.41, 1, -15, "lanczos", 0]`（1 次）
- `[0, 0, "None", 0.71, 1, 15, "lanczos", 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
