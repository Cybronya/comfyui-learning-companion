---
key: 图片生成/文生图/【遇见AI】SD1.5到FLUX基础工作流的演变_2039564955040616450.json
name: 【遇见AI】SD1.5到FLUX基础工作流的演变_2039564955040616450
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】SD1.5到FLUX基础工作流的演变_2039564955040616450.json
hash: 9fa5627da1f4d111
coverage: 0.887324
learned_at: 2026-10-21 02:58:07
nodes: [EmptyLatentImage, CLIPTextEncode, VAEDecode, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, LayerUtility: PurgeVRAM, KSampler, KSampler, KSampler, EmptyLatentImage, LayerUtility: PurgeVRAM, CLIPTextEncode, FluxGuidance, CLIPTextEncode, LayerUtility: PurgeVRAM, EmptyLatentImage, CLIPTextEncodeFlux, CLIPTextEncode, KSampler, EmptyLatentImage, LayerUtility: PurgeVRAM, CLIPTextEncodeFlux, KSampler, ConditioningZeroOut, LayerUtility: PurgeVRAM, BasicGuider, KSamplerSelect, EmptyLatentImage, CLIPTextEncodeFlux, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PrimitiveInt, BasicScheduler, SamplerCustomAdvanced, RandomNoise, Fast Groups Muter (rgthree), Note, LoadImage, LoadImage, Fast Groups Muter (rgthree), UnetLoaderGGUF, DualCLIPLoader, VAELoader, DualCLIPLoader, VAELoader, UnetLoaderGGUF, DualCLIPLoader, VAELoader, UnetLoaderGGUF, Fast Groups Muter (rgthree), DualCLIPLoader, VAELoader, UnetLoaderGGUF, DualCLIPLoader, VAELoader, UnetLoaderGGUF, Fast Groups Muter (rgthree), VAEDecode, VAEDecode, VAEDecode, VAEDecode, VAEDecode, CheckpointLoaderSimple, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Rel_realisticVisionV51_v51VAE.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 853436576931888, "steps": 20, "width": 1024}
---

# 图片生成/文生图/【遇见AI】SD1.5到FLUX基础工作流的演变_2039564955040616450.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】SD1.5到FLUX基础工作流的演变_2039564955040616450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（71 个）：
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `EmptyLatentImage` ★核心
- `CLIPTextEncodeFlux` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncodeFlux` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncodeFlux` ★核心
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `PrimitiveInt`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Fast Groups Muter (rgthree)`
- `Note`
- `LoadImage`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `DualCLIPLoader`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `Fast Groups Muter (rgthree)`
- `DualCLIPLoader`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `Fast Groups Muter (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `853436576931888`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `Rel_realisticVisionV51_v51VAE.safetensors`

## 知识

覆盖率 **89%**（63/71）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`KSampler`、`FluxGuidance`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`RandomNoise`、`LoadImage`、`UnetLoaderGGUF`、`DualCLIPLoader`、`VAELoader`、`CheckpointLoaderSimple`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
