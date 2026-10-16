# workflow>工作节点组

## 节点类型

`workflow>工作节点组`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `噪波生成:NOISE`（5 次）
- `Sigmas:SIGMAS`（5 次）
- `Latent:LATENT`（5 次）
- `条件:CONDITIONING`（5 次）
- `unet_name:COMBO`（5 次）
- `weight_dtype:COMBO`（5 次）
- `clip_name:COMBO`（5 次）
- `type:COMBO`（5 次）
- `device:COMBO`（5 次）
- `vae_name:COMBO`（5 次）

## 输出

- `模型:MODEL`（5 次）
- `CLIP:CLIP`（5 次）
- `VAE:VAE`（5 次）
- `音频:AUDIO`（5 次）
- `图像:IMAGE`（5 次）
- `降噪输出:LATENT`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_fl2va_pruned_int8_convrot.safetensors", "default", "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors", "minimax`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
