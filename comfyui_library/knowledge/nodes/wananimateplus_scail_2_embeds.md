# WanAnimatePlus SCAIL_2 Embeds

## 节点类型

`WanAnimatePlus SCAIL_2 Embeds`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `clip_embeds:WANVIDIMAGE_CLIPEMBEDS`（1 次）
- `ref_image:IMAGE`（1 次）
- `bg_image:IMAGE`（1 次）
- `pose_images:IMAGE`（1 次）
- `prefix_frames:IMAGE`（1 次）
- `prefix_mask:IMAGE`（1 次）
- `transition_video:IMAGE`（1 次）
- `pose_image_mask:IMAGE`（1 次）
- `reference_image_mask:IMAGE`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 121, true, 1, 1, false, true, "disabled", "previous_matched_frame", false, true, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
