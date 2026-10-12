# VideoFromPathsAndAudio

## 节点类型

`VideoFromPathsAndAudio`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `audio:AUDIO`（3 次）
- `image_paths:STRING`（3 次）
- `frame_counts:STRING`（3 次）
- `fps:INT`（3 次）
- `filename_prefix:STRING`（3 次）
- `format:COMBO`（3 次）
- `enable_transition:BOOLEAN`（3 次）
- `transition_seconds:FLOAT`（3 次）
- `transition_type:COMBO`（3 次）

## 输出

- `video_path:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 25, "video_output", "mp4", true, 0.5, "crossfade"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
