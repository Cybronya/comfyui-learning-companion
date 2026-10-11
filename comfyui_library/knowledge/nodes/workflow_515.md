# workflow>515

## 节点类型

`workflow>515`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `vae:VAE`（1 次）
- `model:MODEL`（1 次）
- `LTXVLatentUpsampler vae:VAE`（1 次）
- `LTXVImgToVideoConditionOnly vae:VAE`（1 次）
- `LTXVLatentUpsampler 2 vae:VAE`（1 次）
- `LTXVImgToVideoConditionOnly 2 vae:VAE`（1 次）
- `VAEDecodeTiled vae:VAE`（1 次）

## 输出

- `CLIP:CLIP`（1 次）
- `denoised_output:LATENT`（1 次）
- `SamplerCustomAdvanced denoised_output:LATENT`（1 次）
- `SamplerCustomAdvanced 35 denoised_output:LATENT`（1 次）
- `VIDEO:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["euler_ancestral_cfg_pp", "1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0", "euler_cfg_pp", "0.85`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
