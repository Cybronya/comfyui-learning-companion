# ImageBatchJoinWithTransition

## 节点类型

`ImageBatchJoinWithTransition`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images_1:IMAGE`（2 次）
- `images_2:IMAGE`（2 次）
- `start_index:INT`（2 次）
- `interpolation:COMBO`（2 次）
- `transition_type:COMBO`（2 次）
- `transitioning_frames:INT`（2 次）
- `blur_radius:FLOAT`（2 次）
- `reverse:BOOLEAN`（2 次）
- `device:COMBO`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "linear", "fade", 4, 0, false, "GPU"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
