---
key: 平台全量/FLUX.2 Klein 9B一致性LoRA V2_2046213911669641218.json
name: FLUX.2 Klein 9B一致性LoRA V2_2046213911669641218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.2 Klein 9B一致性LoRA V2_2046213911669641218.json
hash: 31a4a7227082ca4f
coverage: 0.864407
learned_at: 2026-11-14 00:25:09
nodes: [ReferenceLatent, ReferenceLatent, VAEEncode, GetImageSize, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, Image Comparer (rgthree), GetImageSize, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, VAEEncode, PreviewImage, GetImageSize, Image Comparer (rgthree), Image Comparer (rgthree), PreviewImage, ImageScaleToTotalPixels, CLIPTextEncode, LoraLoaderModelOnly, ImageScaleToTotalPixels, CLIPTextEncode, CLIPTextEncode, CR Text, LoraLoaderModelOnly, LoadImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Note, VAEDecode, UNETLoader, CLIPLoader, ImageScaleToTotalPixels, ConditioningZeroOut, VAEDecode, VAEDecode, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CFGGuider, KSamplerSelect, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CFGGuider, SamplerCustomAdvanced, SamplerCustomAdvanced, RandomNoise, JWFloat, VAELoader, SaveImage, PreviewImage, PreviewImage]
patterns: []
missing: []
---

# 平台全量/FLUX.2 Klein 9B一致性LoRA V2_2046213911669641218.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.2 Klein 9B一致性LoRA V2_2046213911669641218.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `GetImageSize`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `GetImageSize`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `PreviewImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Note`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `JWFloat`
- `VAELoader`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`

## 知识

覆盖率 **86%**（51/59）

**有卡**：`ReferenceLatent`、`VAEEncode`、`GetImageSize`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CR Text`、`LoadImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`JWFloat`、`VAELoader`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
