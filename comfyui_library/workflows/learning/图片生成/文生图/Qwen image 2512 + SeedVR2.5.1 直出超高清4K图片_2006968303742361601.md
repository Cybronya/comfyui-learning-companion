---
key: 图片生成/文生图/Qwen image 2512 + SeedVR2.5.1 直出超高清4K图片_2006968303742361601.json
name: Qwen image 2512 + SeedVR2.5.1 直出超高清4K图片_2006968303742361601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2512 + SeedVR2.5.1 直出超高清4K图片_2006968303742361601.json
hash: 1cdc0452befebdff
coverage: 0.458333
learned_at: 2026-10-19 22:00:42
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, LayerUtility: PurgeVRAM, SetNode, GetNode, SetNode, GetNode, ModelSamplingAuraFlow, GetNode, PreviewImage, ImpactInt, GetNode, SeedVR2LoadVAEModel, Image Comparer (rgthree), MarkdownNote, SeedVR2VideoUpscaler, PreviewImage, SeedVR2LoadDiTModel, CLIPTextEncode, ImageScaleToTotalPixels, SaveImage, CR SDXL Aspect Ratio, Text Concatenate, Seed (rgthree), SetNode, SetNode, SetNode, VAEDecode, SetNode, GetNode, SetNode, GetNode, SetNode, CLIPTextEncode, Lora Loader Stack (rgthree), SaveImage, VAELoader, UNETLoader, CLIPLoader, CR Text, KSampler, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "ddim_uniform", "seed": 866841931764725, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen image 2512 + SeedVR2.5.1 直出超高清4K图片_2006968303742361601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2512 + SeedVR2.5.1 直出超高清4K图片_2006968303742361601.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `GetNode`
- `PreviewImage`
- `ImpactInt`
- `GetNode`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `SaveImage`
- `CR SDXL Aspect Ratio`
- `Text Concatenate`
- `Seed (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `Lora Loader Stack (rgthree)`
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CR Text`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `866841931764725`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `ddim_uniform`
- `denoise` = `1`

## 知识

覆盖率 **46%**（22/48）

**有卡**：`LayerUtility: PurgeVRAM`、`ModelSamplingAuraFlow`、`ImpactInt`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`SaveImage`、`CR SDXL Aspect Ratio`、`Text Concatenate`、`Seed (rgthree)`、`VAEDecode`、`Lora Loader Stack (rgthree)`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`CR Text`、`KSampler`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
