# workflow>采样解码

## 节点类型

`workflow>采样解码`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `BasicGuider model:MODEL`（1 次）
- `conditioning:CONDITIONING`（1 次）
- `latent_image:LATENT`（1 次）
- `vae:VAE`（1 次）
- `VAEDecodeAudio vae:VAE`（1 次）
- `noise_seed:INT`（1 次）
- `sampler_name:COMBO`（1 次）
- `scheduler:COMBO`（1 次）
- `steps:INT`（1 次）

## 输出

- `denoised_output:LATENT`（1 次）
- `IMAGE:IMAGE`（1 次）
- `AUDIO:AUDIO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[870633737261100, "randomize", "res_multistep", "simple", 20, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
