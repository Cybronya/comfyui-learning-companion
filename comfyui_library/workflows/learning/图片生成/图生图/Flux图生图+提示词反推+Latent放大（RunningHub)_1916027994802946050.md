---
key: 图片生成/图生图/Flux图生图+提示词反推+Latent放大（RunningHub)_1916027994802946050.json
name: Flux图生图+提示词反推+Latent放大（RunningHub)_1916027994802946050
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux图生图+提示词反推+Latent放大（RunningHub)_1916027994802946050.json
hash: 5c24a8bbdcca2969
coverage: 0.85
learned_at: 2026-10-23 11:02:01
nodes: [DualCLIPLoader, VAEEncode, LoadImage, Image Comparer (rgthree), JWImageResizeByLongerSide, CLIPTextEncodeFlux, KSampler, VAELoader, VAEEncode, VAEDecode, Joy_caption_two, Joy_caption_two_load, LatentUpscaleBy, SaveImage, VAEDecode, PreviewImage, ShowText|pysssss, UNETLoader, CLIPTextEncode, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 410411433941510, "steps": 30}
---

# 图片生成/图生图/Flux图生图+提示词反推+Latent放大（RunningHub)_1916027994802946050.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux图生图+提示词反推+Latent放大（RunningHub)_1916027994802946050.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `DualCLIPLoader`
- `VAEEncode` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `JWImageResizeByLongerSide`
- `CLIPTextEncodeFlux` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Joy_caption_two`
- `Joy_caption_two_load`
- `LatentUpscaleBy`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `410411433941510`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`DualCLIPLoader`、`VAEEncode`、`LoadImage`、`JWImageResizeByLongerSide`、`CLIPTextEncodeFlux`、`KSampler`、`VAELoader`、`VAEDecode`、`Joy_caption_two`、`Joy_caption_two_load`、`LatentUpscaleBy`、`SaveImage`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、CLIPTextEncodeFlux、LatentUpscaleBy
