---
key: 图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json
name: Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json
hash: a99a97c9bef98b89
coverage: 0.875
learned_at: 2026-10-19 22:29:54
nodes: [ReferenceLatent, ConditioningZeroOut, ReferenceLatent, RandomNoise, SamplerCustomAdvanced, VAEEncode, CFGGuider, VAEDecode, GetImageSize, EmptyFlux2LatentImage, VAELoader, CLIPLoader, KSamplerSelect, Flux2Scheduler, ImageScaleToTotalPixels, LoraLoaderModelOnly, UNETLoader, Image Comparer (rgthree), SaveImage, PrimitiveNode, EmptyLatentImage, UNETLoader, KSampler, VAEDecode, PrimitiveInt, PrimitiveInt, CLIPTextEncode, CR Prompt Text, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 367927011836138, "steps": 15, "width": 1080}
---

# 图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Super Z-image 3.0+真实感Lora文生图批量跑 浮云2.9_2020686279058399234.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `PrimitiveNode`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `367927011836138`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`ReferenceLatent`、`ConditioningZeroOut`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEEncode`、`CFGGuider`、`VAEDecode`、`GetImageSize`、`EmptyFlux2LatentImage`、`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`Flux2Scheduler`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImage`、`EmptyLatentImage`、`KSampler`、`CLIPTextEncode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
