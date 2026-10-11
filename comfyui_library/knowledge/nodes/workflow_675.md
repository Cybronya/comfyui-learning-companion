# workflow>675

## 节点类型

`workflow>675`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `model:MODEL`（3 次）
- `vae:VAE`（3 次）
- `LTXVLatentUpsampler vae:VAE`（3 次）
- `LTXVImgToVideoConditionOnly vae:VAE`（3 次）
- `LTXVLatentUpsampler 2 vae:VAE`（3 次）
- `LTXVImgToVideoConditionOnly 2 vae:VAE`（3 次）
- `VAEDecodeTiled vae:VAE`（3 次）

## 输出

- `CLIP:CLIP`（3 次）
- `denoised_output:LATENT`（3 次）
- `SamplerCustomAdvanced denoised_output:LATENT`（3 次）
- `SamplerCustomAdvanced 37 denoised_output:LATENT`（3 次）
- `VIDEO:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, "euler_ancestral_cfg_pp", "1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0", "euler_cfg_pp", "`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
