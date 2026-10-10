# WanVideoAddSteadyDancerEmbeds

## 节点类型

`WanVideoAddSteadyDancerEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `embeds:WANVIDIMAGE_EMBEDS`（4 次）
- `pose_latents_positive:LATENT`（4 次）
- `pose_latents_negative:LATENT`（4 次）
- `clip_vision_embeds:WANVIDIMAGE_CLIPEMBEDS`（4 次）
- `pose_strength_spatial:FLOAT`（4 次）
- `pose_strength_temporal:FLOAT`（4 次）
- `start_percent:FLOAT`（4 次）
- `end_percent:FLOAT`（4 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, 1, 0, 1]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
