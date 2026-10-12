# ConcatVideos

## 节点类型

`ConcatVideos`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `video_path1:STRING`（4 次）
- `video_path2:STRING`（4 次）
- `video_path3:STRING`（4 次）
- `video_path4:STRING`（4 次）
- `external_audio_path:STRING`（4 次）
- `mode:COMBO`（4 次）
- `target_width:INT`（4 次）
- `target_height:INT`（4 次）
- `target_fps:INT`（4 次）
- `filename_prefix:STRING`（4 次）

## 输出

- `output_path:STRING`（4 次）
- `video:VIDEO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["reencode", 0, 0, 0, "concat_", "mp4", true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
