# workflow/模型

## 节点类型

`workflow/模型`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `引导:GUIDER`（1 次）
- `图像:IMAGE`（1 次）
- `正面条件:CONDITIONING`（1 次）
- `负面条件:CONDITIONING`（1 次）

## 输出

- `模型:MODEL`（3 次）
- `CLIP:CLIP`（3 次）
- `VAE:VAE`（2 次）
- `输出:LATENT`（1 次）
- `降噪输出:LATENT`（1 次）
- `图像:IMAGE`（1 次）
- `条件:CONDITIONING`（1 次）
- `VAEDecode 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["J_LandScape_风光大模型__V1_V1.0.safetensors", "SD1.5\\Illustration_COOLKIDS_MERGE_V2.5.safetensors", 1, 1, "DaLat-v1.0.safe`（1 次）
- `[1024, 1536, 1, "euler", "Flux1-Dev-DedistilledMixTuned-v3-fp8.safetensors", "fp8_e4m3fn_fast", "sd3/clip_l.safetensors"`（1 次）
- `["AWPainting_v1.5.safetensors", 1024, 1024, "nearest", "keep proportion", "always", 0, "flux_都市推文_二次元画风_V1.safetensors",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
