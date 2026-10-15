# VideoFrameSelector

## 节点类型

`VideoFrameSelector`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_frames:IMAGE`（1 次）
- `video_info:VHS_VIDEOINFO`（1 次）
- `output_fps:FLOAT`（1 次）
- `target_video_speedup_factor:FLOAT`（1 次）
- `min_source_sampling_fps:INT`（1 次）
- `max_source_sampling_fps:INT`（1 次）
- `frame_load_cap:INT`（1 次）

## 输出

- `Selected_frames:IMAGE`（1 次）
- `multiplier:INT`（1 次）
- `frame_rate:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 1, 8, 12, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
