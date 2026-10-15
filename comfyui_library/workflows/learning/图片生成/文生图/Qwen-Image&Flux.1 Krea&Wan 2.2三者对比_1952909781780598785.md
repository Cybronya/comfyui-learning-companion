---
key: 图片生成/文生图/Qwen-Image&Flux.1 Krea&Wan 2.2三者对比_1952909781780598785.json
name: Qwen-Image&Flux.1 Krea&Wan 2.2三者对比_1952909781780598785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image&Flux.1 Krea&Wan 2.2三者对比_1952909781780598785.json
hash: d4df9d025ddea1f3
coverage: 0.954545
learned_at: 2026-10-15 22:27:09
nodes: [CLIPTextEncode, FluxGuidance, ModelSamplingFlux, KSamplerSelect, BasicScheduler, RandomNoise, LayerUtility: PurgeVRAM V2, SaveImage, AddLabel, String Literal, BasicGuider, SamplerCustomAdvanced, VAELoader, DualCLIPLoader, CLIPLoader, VAELoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSampler, KSampler, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SaveImage, AddLabel, VAEDecode, String Literal, String Literal, AddLabel, CLIPTextEncode, UNETLoader, UNETLoader, VAEDecode, PreviewImage, QwenImageModelLoader, String Literal, SDXLEmptyLatentSizePicker+, easy seed, RH_QwenImageGenerator, SaveImage, UNETLoader, ImageConcanate, ImageConcanate, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 0, "cfg": 3.5, "denoise": 0.5000000000000001, "height": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 75543360141822, "steps": 20, "width": "1280x768 (1.67)"}
---

# 图片生成/文生图/Qwen-Image&Flux.1 Krea&Wan 2.2三者对比_1952909781780598785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image&Flux.1 Krea&Wan 2.2三者对比_1952909781780598785.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ModelSamplingFlux`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `AddLabel`
- `String Literal`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `AddLabel`
- `VAEDecode` ★核心
- `String Literal`
- `String Literal`
- `AddLabel`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `QwenImageModelLoader`
- `String Literal`
- `SDXLEmptyLatentSizePicker+` ★核心
- `easy seed`
- `RH_QwenImageGenerator`
- `SaveImage`
- `UNETLoader` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `PreviewImage`

## 关键参数

- `seed` = `75543360141822`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`
- `width` = `1280x768 (1.67)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ModelSamplingFlux`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`LayerUtility: PurgeVRAM V2`、`SaveImage`、`AddLabel`、`String Literal`、`BasicGuider`、`SamplerCustomAdvanced`、`VAELoader`、`DualCLIPLoader`、`CLIPLoader`、`ModelSamplingSD3`、`KSampler`、`VAEDecode`、`UNETLoader`、`QwenImageModelLoader`、`SDXLEmptyLatentSizePicker+`、`easy seed`、`RH_QwenImageGenerator`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect
