# SAM3PropagateVideo

## 节点类型

`SAM3PropagateVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `session:SAM3_VIDEO_SESSION`（2 次）
- `propagation_direction:COMBO`（2 次）
- `start_frame_index:INT`（2 次）
- `max_frames:INT`（2 次）

## 输出

- `video_masks:SAM3_VIDEO_MASKS`（2 次）
- `session:SAM3_VIDEO_SESSION`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["both", 0, -1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
