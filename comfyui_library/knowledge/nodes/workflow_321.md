# workflow>321

## 节点类型

`workflow>321`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `ImageResizeKJv2 mask:MASK`（1 次）
- `sampler_name:COMBO`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `vae_name:COMBO`（1 次）

## 输出

- `mask:MASK`（1 次）
- `original_size:BOX`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `batch_size:INT`（1 次）
- `image_urls:STRING`（1 次）
- `LATENT:LATENT`（1 次）
- `denoised_output:LATENT`（1 次）
- `IMAGE:IMAGE`（1 次）
- `SamplerCustomAdvanced denoised_output:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler", "new_flux-2-klein-9b.safetensors", "default", "qwen_3_8b.safetensors", "qwen_image", "default", "flux2-vae.saf`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
