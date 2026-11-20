# TutuStreamUpscaleVideo

## 节点类型

`TutuStreamUpscaleVideo`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `upscale_model:UPSCALE_MODEL`（1 次）
- `audio:AUDIO`（1 次）
- `target_width:INT`（1 次）
- `target_height:INT`（1 次）
- `frame_rate:FLOAT`（1 次）
- `tile_size:INT`（1 次）
- `tile_overlap:INT`（1 次）
- `seam_padding:INT`（1 次）
- `filename_prefix:STRING`（1 次）

## 输出

- `video_path:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8640, 4320, 24, 512, 32, 32, "TUTU_8K_360VR_Outpaint", "h264_nvenc", 17, "fast"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
