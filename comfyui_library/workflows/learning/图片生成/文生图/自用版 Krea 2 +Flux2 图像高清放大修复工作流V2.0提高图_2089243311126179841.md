---
key: 图片生成/文生图/自用版 Krea 2 +Flux2 图像高清放大修复工作流V2.0提高图_2089243311126179841.json
name: 自用版 Krea 2 +Flux2 图像高清放大修复工作流V2.0提高图_2089243311126179841
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/自用版 Krea 2 +Flux2 图像高清放大修复工作流V2.0提高图_2089243311126179841.json
hash: 93d178e6ed05b74d
coverage: 0.653465
learned_at: 2026-10-20 01:00:57
nodes: [SetNode, SetNode, SetNode, CR Seed, Int, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, ResolutionSelector, ConditioningZeroOut, 忽略多组孤海, MarkdownNote, ImageScaleToTotalPixels, CLIPTextEncode, ConditioningKrea2Rebalance, VAEDecode, EmptyLatentImage, KSampler, PreviewImage, CLIPTextEncode, LCSSharpnessIntervene, GetImageSize, VAEEncode, LCSSharpnessCalibrate, ReferenceLatent, LCSLoadData, LCSColorAnchor, ConditioningZeroOut, ReferenceLatent, EmptyFlux2LatentImage, CFGGuider, RandomNoise, VAEDecode, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), SaveImage, 忽略多组孤海, 孤海注释, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, VAELoader, VAELoader, CLIPLoader, LoraLoaderBypassModelOnly, UNETLoader, Flux2Scheduler, KSamplerSelect, SamplerCustomAdvanced, Note, VAELoader, easy sam3ImageSegmentation, VRAM_Debug, CLIPTextEncode, PreviewImage, GetImageSize+, ConditioningAverage, ResizeMask, CLIPTextEncode, VRAM_Debug, VRAM_Debug, CLIPTextEncode, CR Upscale Image, ImageScaleToTotalPixels, GetImageSize+, SetNode, CR Text Concatenate, LoraLoaderModelOnly, PrimitiveStringMultiline, ImageScaleToTotalPixels, Florence2ModelLoader, LGNoiseInjectionLatent, CR Upscale Image, easy sam3ModelLoader, GenerateNoise, MaskPreview+, Florence2Run, ImageScaleToTotalPixels, ImageCompositeMasked, PrimitiveStringMultiline, CheckpointLoaderSimple, UltimateSDUpscaleNoUpscale]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": 1, "height": 720, "sampler_name": "er_sde", "scheduler": "simple", "seed": 929628727452692, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/自用版 Krea 2 +Flux2 图像高清放大修复工作流V2.0提高图_2089243311126179841.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/自用版 Krea 2 +Flux2 图像高清放大修复工作流V2.0提高图_2089243311126179841.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Seed`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ResolutionSelector`
- `ConditioningZeroOut`
- `忽略多组孤海`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `ConditioningKrea2Rebalance`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LCSSharpnessIntervene`
- `GetImageSize`
- `VAEEncode` ★核心
- `LCSSharpnessCalibrate`
- `ReferenceLatent`
- `LCSLoadData`
- `LCSColorAnchor`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `忽略多组孤海`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderBypassModelOnly` ★核心
- `UNETLoader` ★核心
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Note`
- `VAELoader`
- `easy sam3ImageSegmentation`
- `VRAM_Debug`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `GetImageSize+`
- `ConditioningAverage`
- `ResizeMask`
- `CLIPTextEncode` ★核心
- `VRAM_Debug`
- `VRAM_Debug`
- `CLIPTextEncode` ★核心
- `CR Upscale Image`
- `ImageScaleToTotalPixels`
- `GetImageSize+`
- `SetNode`
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `ImageScaleToTotalPixels`
- `Florence2ModelLoader`
- `LGNoiseInjectionLatent`
- `CR Upscale Image`
- `easy sam3ModelLoader`
- `GenerateNoise`
- `MaskPreview+`
- `Florence2Run`
- `ImageScaleToTotalPixels`
- `ImageCompositeMasked`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `UltimateSDUpscaleNoUpscale`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `929628727452692`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`

## 知识

覆盖率 **65%**（66/101）

**有卡**：`CR Seed`、`Int`、`ResolutionSelector`、`ConditioningZeroOut`、`忽略多组孤海`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`ConditioningKrea2Rebalance`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`LCSSharpnessIntervene`、`GetImageSize`、`VAEEncode`、`LCSSharpnessCalibrate`、`ReferenceLatent`、`LCSLoadData`、`LCSColorAnchor`、`EmptyFlux2LatentImage`、`CFGGuider`、`RandomNoise`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderBypassModelOnly`、`Flux2Scheduler`、`KSamplerSelect`、`SamplerCustomAdvanced`、`easy sam3ImageSegmentation`、`VRAM_Debug`、`GetImageSize+`、`ConditioningAverage`、`ResizeMask`、`CR Upscale Image`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`Florence2ModelLoader`、`LGNoiseInjectionLatent`、`easy sam3ModelLoader`、`GenerateNoise`、`MaskPreview+`、`Florence2Run`、`ImageCompositeMasked`、`CheckpointLoaderSimple`、`UltimateSDUpscaleNoUpscale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
