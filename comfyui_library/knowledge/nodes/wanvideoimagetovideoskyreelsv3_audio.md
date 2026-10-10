# WanVideoImageToVideoSkyreelsv3_audio

## 节点类型

`WanVideoImageToVideoSkyreelsv3_audio`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `start_image:IMAGE`（1 次）
- `reference_video:IMAGE`（1 次）
- `clip_embeds:WANVIDIMAGE_CLIPEMBEDS`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `frame_window_size:INT`（1 次）
- `motion_frame:INT`（1 次）
- `drop_frames:INT`（1 次）
- `tiled_vae:BOOLEAN`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `output_path:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[720, 720, 81, 5, 12, false, true, "reinhard_torch", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
