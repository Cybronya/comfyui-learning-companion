# VideoCombineNode

## 节点类型

`VideoCombineNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（6 次）
- `audio:AUDIO`（6 次）
- `frame_rate:FLOAT`（6 次）
- `filename:STRING`（6 次）
- `pix_fmt:COMBO`（6 次）
- `crf:INT`（6 次）
- `save_metadata:BOOLEAN`（6 次）
- `trim_to_audio:BOOLEAN`（6 次）
- `last_frames_count:INT`（6 次）
- `pingpong:BOOLEAN`（6 次）

## 输出

- `video_path:STRING`（6 次）
- `filename:STRING`（6 次）
- `last_frames_images:IMAGE`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, "video_output", "yuv420p", 19, true, false, 0, false]`（5 次）
- `[17.540000000000003, "video_output", "yuv420p", 19, true, false, 0, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
