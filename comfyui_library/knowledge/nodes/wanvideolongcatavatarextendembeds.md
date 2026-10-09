# WanVideoLongCatAvatarExtendEmbeds

## 节点类型

`WanVideoLongCatAvatarExtendEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prev_latents:LATENT`（5 次）
- `audio_embeds:MULTITALK_EMBEDS`（5 次）
- `ref_latent:LATENT`（5 次）
- `samples:LATENT`（5 次）
- `num_frames:INT`（5 次）
- `overlap:INT`（5 次）
- `frames_processed:INT`（5 次）
- `if_not_enough_audio:COMBO`（5 次）
- `ref_frame_index:INT`（5 次）
- `ref_mask_frame_range:INT`（5 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（5 次）
- `samples_slice:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[93, 13, 93, "pad_with_start", 10, 3]`（4 次）
- `[93, 0, 0, "pad_with_start", 10, 3]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
