# workflow>02

## 节点类型

`workflow>02`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `CLIPTextEncode clip:CLIP`（1 次）
- `图像:IMAGE`（1 次）
- `VAE:VAE`（1 次）
- `VAEDecode vae:VAE`（1 次）
- `遮罩:MASK`（1 次）
- `VAEEncode vae:VAE`（1 次）
- `VAEDecode 2 vae:VAE`（1 次）
- `value:INT`（1 次）
- `prompt:STRING`（1 次）

## 输出

- `show_help:STRING`（1 次）
- `batch_size:INT`（1 次）
- `降噪输出:LATENT`（1 次）
- `遮罩:MASK`（1 次）
- `原始大小:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `GetImageSize batch_size:INT`（1 次）
- `图像:IMAGE`（1 次）
- `output:*`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2048, "Fujifilm GFX，4k，富士胶片,增加柔和的细节，不要改变人物的面部特征，和表情", "euler", 1076413573596477, "randomize", "z_image_turbo-vae.safete`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
