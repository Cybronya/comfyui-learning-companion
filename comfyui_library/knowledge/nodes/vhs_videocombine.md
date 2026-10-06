# VHS_VideoCombine

## 节点类型

`VHS_VideoCombine`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 22 个 workflow 中。

## 输入

- `images:IMAGE`（30 次）
- `audio:AUDIO`（30 次）
- `meta_batch:VHS_BatchManager`（30 次）
- `vae:VAE`（30 次）
- `frame_rate:FLOAT`（30 次）
- `loop_count:INT`（30 次）
- `filename_prefix:STRING`（30 次）
- `format:COMBO`（30 次）
- `pingpong:BOOLEAN`（30 次）
- `save_output:BOOLEAN`（30 次）

## 输出

- `Filenames:VHS_FILENAMES`（30 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `{"crf": 19, "filename_prefix": "AnimateDiff", "format": "video/h264-mp4", "frame_rate": 24, "loop_count": 0, "no_preview`（8 次）
- `{"crf": 19, "filename_prefix": "YZ_H3_一采", "format": "video/h264-mp4", "frame_rate": 24, "loop_count": 0, "no_preview": `（4 次）
- `{"crf": 19, "filename_prefix": "YZ_H3_二采", "format": "video/h264-mp4", "frame_rate": 24, "loop_count": 0, "no_preview": `（4 次）
- `{"crf": 12, "filename_prefix": "selflift", "format": "video/h264-mp4", "frame_rate": 24, "loop_count": 0, "no_preview": `（3 次）
- `{"crf": 19, "filename_prefix": "AnimateDiff", "format": "video/h264-mp4", "frame_rate": 24, "loop_count": 0, "no_preview`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
