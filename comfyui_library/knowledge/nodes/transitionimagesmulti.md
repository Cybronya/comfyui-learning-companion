# TransitionImagesMulti

## 节点类型

`TransitionImagesMulti`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `interpolation:COMBO`（1 次）
- `transitioning_frames:INT`（1 次）
- `transition_type:COMBO`（1 次）
- `reverse:BOOLEAN`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, "linear", "horizontal slide", 72, 16, false, "GPU", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
