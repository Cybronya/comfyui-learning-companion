---
key: 图片生成/图生图/flux.1-lite-8B-alpha VS Flux Fp8_1849765335124824065.json
name: flux.1-lite-8B-alpha VS Flux Fp8_1849765335124824065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.1-lite-8B-alpha VS Flux Fp8_1849765335124824065.json
hash: ca1bab32686e19a4
coverage: 0.868421
learned_at: 2026-10-23 11:35:50
nodes: [Fast Groups Bypasser (rgthree), CLIPTextEncode, FluxGuidance, ConditioningZeroOut, LayerUtility: PurgeVRAM, CLIPTextEncode, FluxGuidance, LayerUtility: PurgeVRAM, EmptySD3LatentImage, SDXLAspectRatioSelector, Note, SaveImage, Note, ConditioningZeroOut, DisplayText_Zho, SeargePromptText, RH_Prompter, VAEDecode, VAEDecode, SaveImage, SaveImage, PreviewImage, PreviewImage, CheckpointLoaderSimple, UNETLoader, DualCLIPLoader, DualCLIPLoader, DualCLIPLoader, DualCLIPLoader, DualCLIPLoader, DualCLIPLoader, VAELoader, VAELoader, VAELoader, VAELoader, CR Simple Image Compare, KSampler, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "flux1-dev-fp8.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 757502867902916, "steps": 28}
---

# 图片生成/图生图/flux.1-lite-8B-alpha VS Flux Fp8_1849765335124824065.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.1-lite-8B-alpha VS Flux Fp8_1849765335124824065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `LayerUtility: PurgeVRAM`
- `EmptySD3LatentImage`
- `SDXLAspectRatioSelector`
- `Note`
- `SaveImage`
- `Note`
- `ConditioningZeroOut`
- `DisplayText_Zho`
- `SeargePromptText`
- `RH_Prompter`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `VAELoader`
- `VAELoader`
- `CR Simple Image Compare`
- `KSampler` ★核心
- `KSampler` ★核心

## 关键参数

- `checkpoint` = `flux1-dev-fp8.safetensors`
- `seed` = `757502867902916`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM`、`EmptySD3LatentImage`、`SDXLAspectRatioSelector`、`SaveImage`、`DisplayText_Zho`、`SeargePromptText`、`RH_Prompter`、`VAEDecode`、`CheckpointLoaderSimple`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CR Simple Image Compare`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance
