---
key: 图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1912846734618259458.json
name: 高清放大 Flux.1-dev-Controlnet-Upscaler_1912846734618259458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1912846734618259458.json
hash: ab4a9a575593eec0
coverage: 0.958333
learned_at: 2026-10-23 13:34:21
nodes: [ImageScaleBy, Image Comparer (rgthree), SaveImage, VAEDecode, CLIPTextEncode, Florence2Run, GetImageSize, DownloadAndLoadFlorence2Model, CheckpointLoaderSimple, KSampler, ControlNetApplySD3, FluxGuidance, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, ControlNetLoader, CLIPTextEncode, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, EmptySD3LatentImage, easy clearCacheAll, LoadImage, Float]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 319076850375923, "steps": 30}
---

# 图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1912846734618259458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1912846734618259458.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ImageScaleBy`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Florence2Run`
- `GetImageSize`
- `DownloadAndLoadFlorence2Model`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `ControlNetApplySD3` ★核心
- `FluxGuidance`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `EmptySD3LatentImage`
- `easy clearCacheAll`
- `LoadImage`
- `Float`

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`
- `seed` = `319076850375923`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.7000000000000001`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`ImageScaleBy`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`Florence2Run`、`GetImageSize`、`DownloadAndLoadFlorence2Model`、`CheckpointLoaderSimple`、`KSampler`、`ControlNetApplySD3`、`FluxGuidance`、`easy clearCacheAll`、`ControlNetLoader`、`EmptySD3LatentImage`、`LoadImage`、`Float`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、ControlNetApplySD3、FluxGuidance
