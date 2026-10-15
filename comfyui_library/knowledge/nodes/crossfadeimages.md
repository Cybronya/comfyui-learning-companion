# CrossFadeImages

## 节点类型

`CrossFadeImages`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images_1:IMAGE`（4 次）
- `images_2:IMAGE`（4 次）
- `interpolation:COMBO`（4 次）
- `transition_start_index:INT`（4 次）
- `transitioning_frames:INT`（4 次）
- `start_level:FLOAT`（4 次）
- `end_level:FLOAT`（4 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ease_in_out", 164, 24, 0, 1]`（2 次）
- `["glitchy", 164, 24, 0, 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
