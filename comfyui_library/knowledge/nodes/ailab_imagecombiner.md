# AILab_ImageCombiner

## 节点类型

`AILab_ImageCombiner`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `foreground:IMAGE`（3 次）
- `background:IMAGE`（3 次）
- `foreground_mask:MASK`（3 次）
- `mode:COMBO`（3 次）
- `foreground_opacity:FLOAT`（3 次）
- `foreground_scale:FLOAT`（3 次）
- `position_x:INT`（3 次）
- `position_y:INT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）
- `WIDTH:INT`（3 次）
- `HEIGHT:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["normal", 1, 1, 51, 35]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
