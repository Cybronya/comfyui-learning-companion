# MiniMaxH3LongVideoSampler-solarL

## 节点类型

`MiniMaxH3LongVideoSampler-solarL`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `sampler_1:SAMPLER`（1 次）
- `sigmas_1:SIGMAS`（1 次）
- `negative:CONDITIONING`（1 次）
- `model_2:MODEL`（1 次）
- `sampler_2:SAMPLER`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `audio:AUDIO`（1 次）
- `fps:FLOAT`（1 次）
- `frame_count:INT`（1 次）
- `last_first_pass_latent:LATENT`（1 次）
- `report:STRING`（1 次）
- `output:LATENT`（1 次）
- `denoised_output:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[403591693415286, "randomize", 1, 0, 124, 22, "official_image_guide", "minimax_h3_latent_upscaler_3d_bf16.safetensors", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
