---
key: 图片生成/文生图/Flux_Commercial_FaceLock_2004750671989665794.json
name: Flux_Commercial_FaceLock_2004750671989665794
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux_Commercial_FaceLock_2004750671989665794.json
hash: 339437b7269415a2
coverage: 1
learned_at: 2026-10-19 22:00:33
nodes: [KSampler, CheckpointLoaderSimple, CLIPTextEncode, IPAdapterAdvanced, IPAdapterUnifiedLoader, DualCLIPLoader, VAELoader, SaveImage, VAEDecode, CLIPTextEncode, EmptyLatentImage, LoadImageFromUrl]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "checkpoint": "flux1-dev.safetensors", "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 452061169184103, "steps": 25, "width": 1080}
---

# 图片生成/文生图/Flux_Commercial_FaceLock_2004750671989665794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux_Commercial_FaceLock_2004750671989665794.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `DualCLIPLoader`
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImageFromUrl`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `452061169184103`
- `steps` = `25`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `flux1-dev.safetensors`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`KSampler`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`IPAdapterAdvanced`、`IPAdapterUnifiedLoader`、`DualCLIPLoader`、`VAELoader`、`SaveImage`、`VAEDecode`、`EmptyLatentImage`、`LoadImageFromUrl`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、DualCLIPLoader、IPAdapterAdvanced
