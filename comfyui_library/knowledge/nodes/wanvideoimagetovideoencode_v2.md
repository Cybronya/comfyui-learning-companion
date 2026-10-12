# WanVideoImageToVideoEncode_v2

## 节点类型

`WanVideoImageToVideoEncode_v2`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `clip_embeds:WANVIDIMAGE_CLIPEMBEDS`（1 次）
- `start_image:IMAGE`（1 次）
- `mid_image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `control_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `temporal_mask:MASK`（1 次）
- `extra_latents:LATENT`（1 次）
- `add_cond_latents:ADD_COND_LATENTS`（1 次）
- `width:INT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 81, 0, 1, 1, 1, 0.8, 0.5, 1, true, true, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
