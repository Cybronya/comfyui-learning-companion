# WanVideoAddOneToAllExtendEmbeds

## 节点类型

`WanVideoAddOneToAllExtendEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `prev_latents:LATENT`（1 次）
- `pose_images:IMAGE`（1 次）
- `window_size:INT`（1 次）
- `overlap:INT`（1 次）
- `frames_processed:INT`（1 次）
- `if_not_enough_frames:COMBO`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `pose_slice:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 5, 0, "pad_with_last"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
