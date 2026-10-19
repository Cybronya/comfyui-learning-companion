---
key: 图片生成/文生图/Qwen-Image 2512+SeedVR2.5高清修复，自动优化提示词_2007414963136106497.json
name: Qwen-Image 2512+SeedVR2.5高清修复，自动优化提示词_2007414963136106497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image 2512+SeedVR2.5高清修复，自动优化提示词_2007414963136106497.json
hash: 5816ff75a8076536
coverage: 0.769231
learned_at: 2026-10-19 22:00:44
nodes: [LayerUtility: PurgeVRAM V2, ImageScaleToTotalPixels, Image Comparer (rgthree), SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Int, Note, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM V2, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, CLIPLoader, QwenImageLatentAspectRatio, Qwen2.5, easy showAnything, VAEDecode, Anything Everywhere, UNETLoader, CLIPTextEncode, PreviewImage, Text Multiline, LayerUtility: PurgeVRAM V2, Fast Groups Bypasser (rgthree), SaveImage, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 978132384737030, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image 2512+SeedVR2.5高清修复，自动优化提示词_2007414963136106497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image 2512+SeedVR2.5高清修复，自动优化提示词_2007414963136106497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Int`
- `Note`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `QwenImageLatentAspectRatio`
- `Qwen2.5`
- `easy showAnything`
- `VAEDecode` ★核心
- `Anything Everywhere`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Text Multiline`
- `LayerUtility: PurgeVRAM V2`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `978132384737030`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`LayerUtility: PurgeVRAM V2`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`Int`、`SeedVR2VideoUpscaler`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`QwenImageLatentAspectRatio`、`Qwen2.5`、`VAEDecode`、`UNETLoader`、`Text Multiline`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
