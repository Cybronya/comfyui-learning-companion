# VideoCombineV2

## 节点类型

`VideoCombineV2`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `meta_batch:VHS_BatchManager`（2 次）
- `vae:VAE`（2 次）
- `frame_rate:FLOAT`（2 次）
- `loop_count:INT`（2 次）
- `filename_prefix:STRING`（2 次）
- `format:COMBO`（2 次）
- `pingpong:BOOLEAN`（2 次）
- `save_output:BOOLEAN`（2 次）

## 输出

- `video:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 0, "AnimateDiff", "video/h264-mp4", "yuv420p", 19, true, false, false, true, ""]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
