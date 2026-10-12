# AdaptiveWanVideoAnimateEmbeds

## 节点类型

`AdaptiveWanVideoAnimateEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `vae:WANVAE`（2 次）
- `clip_embeds:WANVIDIMAGE_CLIPEMBEDS`（2 次）
- `ref_images:IMAGE`（2 次）
- `pose_images:IMAGE`（2 次）
- `face_images:IMAGE`（2 次）
- `bg_images:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `num_frames:INT`（2 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, true, 77, "optimal_fit", "mkl", 1, 1, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
