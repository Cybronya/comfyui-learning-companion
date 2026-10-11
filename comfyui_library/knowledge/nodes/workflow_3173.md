# workflow>工作组

## 节点类型

`workflow>工作组`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `条件:CONDITIONING`（2 次）
- `Latent:LATENT`（2 次）
- `clip_name:COMBO`（2 次）
- `type:COMBO`（2 次）
- `device:COMBO`（2 次）
- `vae_name:COMBO`（2 次）
- `VAELoader vae_name:COMBO`（2 次）
- `sampler_name:COMBO`（2 次）
- `unet_name:COMBO`（2 次）
- `weight_dtype:COMBO`（2 次）

## 输出

- `CLIP:CLIP`（2 次）
- `VAE:VAE`（2 次）
- `降噪输出:LATENT`（2 次）
- `VIDEO:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "minimax", "default", "minimax_h3_video_vae_fp16.safetensors", "minimax`（1 次）
- `["qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "minimax", "default", "minimax_h3_video_vae_fp16.safetensors", "minimax`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
