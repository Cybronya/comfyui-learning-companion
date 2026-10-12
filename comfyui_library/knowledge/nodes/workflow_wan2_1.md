# workflow>Wan2.1采样器

## 节点类型

`workflow>Wan2.1采样器`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `model:WANVIDEOMODEL`（1 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `text_embeds:WANVIDEOTEXTEMBEDS`（1 次）
- `samples:LATENT`（1 次）
- `context_options:WANVIDCONTEXT`（1 次）
- `uni3c_embeds:UNI3C_EMBEDS`（1 次）
- `multitalk_embeds:MULTITALK_EMBEDS`（1 次）
- `enable_vae_tiling:BOOLEAN`（1 次）
- `tile_x:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, 272, 272, 144, 128, "default", 4, 1.0000000000000002, 5, 3, "fixed", true, "dpm++_sde", 0, 1, false, "comfy", 0,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
