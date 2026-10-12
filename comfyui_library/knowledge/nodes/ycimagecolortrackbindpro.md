# YCImageColorTrackBindPro

## 节点类型

`YCImageColorTrackBindPro`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `video_frames:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `target_color:STRING`（1 次）
- `color_tolerance:INT`（1 次）
- `smoothing_factor:FLOAT`（1 次）
- `processing_width:INT`（1 次）
- `anchor_offset_x:INT`（1 次）
- `anchor_offset_y:INT`（1 次）
- `base_scale:FLOAT`（1 次）

## 输出

- `output_frames:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["#10ee49", 30, 0.23000000000000004, 640, 0, 0, 0.5, false, 0, false, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
