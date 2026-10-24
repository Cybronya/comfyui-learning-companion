---
key: 图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1839649528810000386.json
name: 高清放大 Flux.1-dev-Controlnet-Upscaler_1839649528810000386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1839649528810000386.json
hash: 8c9dfae9f5a3073d
coverage: 0.941176
learned_at: 2026-10-23 13:34:20
nodes: [FluxGuidance, CLIPTextEncode, GetImageSize, Float, KSampler, CLIPTextEncode, EmptySD3LatentImage, ImageScaleBy, CheckpointLoaderSimple, DownloadAndLoadFlorence2Model, Florence2Run, ControlNetLoader, LoadImage, VAEDecode, SaveImage, Image Comparer (rgthree), ControlNetApplySD3]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "controlnet_strength": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 16458016261158, "steps": 20}
---

# 图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1839649528810000386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高清放大 Flux.1-dev-Controlnet-Upscaler_1839649528810000386.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `Float`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `ImageScaleBy`
- `CheckpointLoaderSimple` ★核心
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `ControlNetLoader`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `ControlNetApplySD3` ★核心

## 关键参数

- `seed` = `16458016261158`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `flux1-dev-fp8.safetensors`
- `controlnet_strength` = `0.7000000000000001`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`FluxGuidance`、`CLIPTextEncode`、`GetImageSize`、`Float`、`KSampler`、`EmptySD3LatentImage`、`ImageScaleBy`、`CheckpointLoaderSimple`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`ControlNetLoader`、`LoadImage`、`VAEDecode`、`SaveImage`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、ControlNetApplySD3、FluxGuidance
