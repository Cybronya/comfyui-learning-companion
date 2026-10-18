# MinimaxH3LatentUpscaler3DRefineHandoff

## 节点类型

`MinimaxH3LatentUpscaler3DRefineHandoff`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `latent:LATENT`（1 次）
- `noise:NOISE`（1 次）
- `sampler:SAMPLER`（1 次）
- `sigmas:SIGMAS`（1 次）
- `audio_latent:LATENT`（1 次）
- `refine_state:H3_CONTINUUM_REFINE_STATE`（1 次）
- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `model_name:COMBO`（1 次）

## 输出

- `latent:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["minimax_h3_latent_upscaler_3d_fp16.safetensors", "target dimensions", 1.5, 1344, 768, 1, 32, true, true, 1, "cuda", "f`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
