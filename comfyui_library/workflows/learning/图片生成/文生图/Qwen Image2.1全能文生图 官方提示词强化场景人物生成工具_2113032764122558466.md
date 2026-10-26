---
key: 图片生成/文生图/Qwen Image2.1全能文生图 官方提示词强化场景人物生成工具_2113032764122558466.json
name: Qwen Image2.1全能文生图 官方提示词强化场景人物生成工具_2113032764122558466
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1全能文生图 官方提示词强化场景人物生成工具_2113032764122558466.json
hash: 981bfb87ab2e342e
coverage: 0.803571
learned_at: 2026-10-26 22:08:40
nodes: [PrimitiveStringMultiline, ResolutionSelector, KSampler, VAEDecode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, SeedVR2LoadDiTModel, ShowAnything|Mie, SaveImage, VAELoader, CLIPLoader, UNETLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), PrimitiveStringMultiline, CLIPLoader, TextGenerate, PrimitiveStringMultiline, StringFormat, RegexExtract, EmptyLatentImage, Fast Groups Bypasser (rgthree), ComfySwitchNode, TextEncodeQwenImage21, ShowAnything|Mie, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image2.1全能文生图 官方提示词强化场景人物生成工具_2113032764122558466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1全能文生图 官方提示词强化场景人物生成工具_2113032764122558466.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `ShowAnything|Mie`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `StringFormat`
- `RegexExtract`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowAnything|Mie`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（45/56）

**有卡**：`ResolutionSelector`、`KSampler`、`VAEDecode`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`ShowAnything|Mie`、`SaveImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TextGenerate`、`StringFormat`、`RegexExtract`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
