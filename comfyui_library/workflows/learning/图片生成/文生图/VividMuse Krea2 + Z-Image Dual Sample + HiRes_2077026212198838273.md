---
key: 图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json
name: VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json
hash: 2f1947da7e74f5e9
coverage: 0.930233
learned_at: 2026-10-20 00:20:10
nodes: [ImageScaleBy, ConditioningZeroOut, ImageResize+, GetImageSize+, SeedVR2LoadVAEModel, ImageScaleBy, TTP_Image_Tile_Batch, GetImageSize+, TTP_Tile_image_size, ImageResize+, EmptyLatentImage, SeedVR2VideoUpscaler, VAELoader, CLIPLoader, CLIPLoader, VAELoader, ConditioningZeroOut, VAEEncode, SeedVR2LoadDiTModel, TTP_Image_Assy, Image Comparer (rgthree), SaveImage, easy loraStackApply, VAEDecode, CLIPTextEncode, UNETLoader, CLIPTextEncode, easy promptList, KSamplerAdvanced, KSamplerAdvanced, UNETLoader, KSampler, easy promptList, ResolutionSelector, Seed (rgthree), VAEDecode, SaveImage, SaveImage, easy promptList, easy loraStack, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), easy promptList]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.3500000000000001, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 289635289365, "steps": 5, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Krea2 + Z-Image Dual Sample + HiRes_2077026212198838273.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `ImageScaleBy`
- `ConditioningZeroOut`
- `ImageResize+`
- `GetImageSize+`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `TTP_Image_Tile_Batch`
- `GetImageSize+`
- `TTP_Tile_image_size`
- `ImageResize+`
- `EmptyLatentImage` ★核心
- `SeedVR2VideoUpscaler`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `SeedVR2LoadDiTModel`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `SaveImage`
- `easy loraStackApply`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `easy promptList`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `easy promptList`
- `ResolutionSelector`
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `easy promptList`
- `easy loraStack`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `289635289365`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **93%**（40/43）

**有卡**：`ImageScaleBy`、`ConditioningZeroOut`、`ImageResize+`、`GetImageSize+`、`SeedVR2LoadVAEModel`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`EmptyLatentImage`、`SeedVR2VideoUpscaler`、`VAELoader`、`CLIPLoader`、`VAEEncode`、`SeedVR2LoadDiTModel`、`TTP_Image_Assy`、`SaveImage`、`easy loraStackApply`、`VAEDecode`、`CLIPTextEncode`、`UNETLoader`、`easy promptList`、`KSamplerAdvanced`、`KSampler`、`ResolutionSelector`、`Seed (rgthree)`、`easy loraStack`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
