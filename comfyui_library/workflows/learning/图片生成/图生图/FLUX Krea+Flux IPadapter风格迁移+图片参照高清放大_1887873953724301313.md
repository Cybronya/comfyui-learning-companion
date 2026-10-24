---
key: 图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json
name: FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json
hash: 5f87e6e71e1278b8
coverage: 0.964286
learned_at: 2026-10-23 10:53:29
nodes: [VAELoader, BasicScheduler, EmptyLatentImage, CLIPTextEncode, FluxGuidance, easy cleanGpuUsed, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, easy cleanGpuUsed, CLIPTextEncode, RandomNoise, PreviewImage, DualCLIPLoader, SaveImage, MirroredImage, CLIPTextEncode, UpscaleModelLoader, UltimateSDUpscale, SDXLPromptStyler, RH_Captioner, ApplyIPAdapterFlux, LoraLoader, LoadImage, UNETLoader, LoadImage, IPAdapterFluxLoader, VAEDecode]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "可爱治愈系绘本插画壁纸_v1.0.safetensors", "strength_clip": 1, "strength_model": 0.8, "width": 768}
---

# 图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX Krea+Flux IPadapter风格迁移+图片参照高清放大_1887873953724301313.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAELoader`
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `easy cleanGpuUsed`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `PreviewImage`
- `DualCLIPLoader`
- `SaveImage`
- `MirroredImage`
- `CLIPTextEncode` ★核心
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `SDXLPromptStyler`
- `RH_Captioner`
- `ApplyIPAdapterFlux`
- `LoraLoader` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `LoadImage`
- `IPAdapterFluxLoader`
- `VAEDecode` ★核心

**识别到的模式**：lora

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `可爱治愈系绘本插画壁纸_v1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`VAELoader`、`BasicScheduler`、`EmptyLatentImage`、`CLIPTextEncode`、`FluxGuidance`、`easy cleanGpuUsed`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`DualCLIPLoader`、`SaveImage`、`MirroredImage`、`UpscaleModelLoader`、`UltimateSDUpscale`、`SDXLPromptStyler`、`RH_Captioner`、`ApplyIPAdapterFlux`、`LoraLoader`、`LoadImage`、`UNETLoader`、`IPAdapterFluxLoader`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance、KSamplerSelect
