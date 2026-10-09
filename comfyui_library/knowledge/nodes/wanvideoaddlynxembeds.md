# WanVideoAddLynxEmbeds

## 节点类型

`WanVideoAddLynxEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `vae:WANVAE`（1 次）
- `lynx_ip_embeds:LYNXIP`（1 次）
- `ref_image:IMAGE`（1 次）
- `ref_text_embed:WANVIDEOTEXTEMBEDS`（1 次）
- `ref_blocks_to_use:STRING`（1 次）
- `ip_scale:FLOAT`（1 次）
- `ref_scale:FLOAT`（1 次）
- `lynx_cfg_scale:FLOAT`（1 次）
- `start_percent:FLOAT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.7, 0.6, 2, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
