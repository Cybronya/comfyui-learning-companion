# workflow>H3-4S

## 节点类型

`workflow>H3-4S`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `first_frame:IMAGE`（1 次）
- `last_frame:IMAGE`（1 次）
- `vae_name:COMBO`（1 次）
- `VAELoader vae_name:COMBO`（1 次）
- `clip_name:COMBO`（1 次）
- `type:COMBO`（1 次）
- `device:COMBO`（1 次）
- `value:FLOAT`（1 次）
- `unet_name:COMBO`（1 次）
- `weight_dtype:COMBO`（1 次）

## 输出

- `FLOAT:FLOAT`（1 次）
- `BOOL:BOOLEAN`（1 次）
- `denoised_output:LATENT`（1 次）
- `VIDEO:VIDEO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_video_vae_fp16.safetensors", "minimax_h3_audio_vae_fp32.safetensors", "qwen3vl_32b_minimax_h3_nvfp4_awq.saf`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
