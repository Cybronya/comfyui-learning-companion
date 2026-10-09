# WanVideoAnimateEmbeds

## 节点类型

`WanVideoAnimateEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `clip_embeds:WANVIDIMAGE_CLIPEMBEDS`（1 次）
- `ref_images:IMAGE`（1 次）
- `pose_images:IMAGE`（1 次）
- `face_images:IMAGE`（1 次）
- `bg_images:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `start_ref_image:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 501, false, 77, "disabled", 1, 1, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
