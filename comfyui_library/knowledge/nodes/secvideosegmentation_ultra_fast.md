# SeCVideoSegmentation_Ultra-Fast

## 节点类型

`SeCVideoSegmentation_Ultra-Fast`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:SEC_MODEL`（4 次）
- `frames:IMAGE`（4 次）
- `positive_points:STRING`（4 次）
- `negative_points:STRING`（4 次）
- `bbox:BBOX`（4 次）
- `input_mask:MASK`（4 次）
- `tracking_direction:COMBO`（4 次）
- `annotation_frame_idx:INT`（4 次）
- `object_id:INT`（4 次）
- `max_frames_to_track:INT`（4 次）

## 输出

- `masks:MASK`（4 次）
- `object_ids:INT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["forward", 0, 1, -1, 12, false, true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
