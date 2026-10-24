---
key: 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 加强了一致性 林耀3.6_2029755418074947585.json
name: Flux2 Klein9B 图像编辑工作流 加强了一致性 林耀3.6_2029755418074947585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein9B 图像编辑工作流 加强了一致性 林耀3.6_2029755418074947585.json
hash: e71432858ca5ab6f
coverage: 0.888889
learned_at: 2026-10-23 10:59:29
nodes: [ReferenceLatent, ConditioningZeroOut, ReferenceLatent, SamplerCustomAdvanced, VAEEncode, CFGGuider, PreviewImage, EmptyFlux2LatentImage, GetImageSize, VAELoader, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, SamplerCustomAdvanced, VAEEncode, CFGGuider, PreviewImage, EmptyFlux2LatentImage, GetImageSize, VAELoader, Flux2Scheduler, CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, CLIPLoader, VAEDecode, VAEDecode, RandomNoise, PreviewImage, Image Comparer (rgthree), KSamplerSelect, KSamplerSelect, LoraLoaderModelOnly, Image Comparer (rgthree), LayerUtility: ImageReelComposit, LayerUtility: ImageReel, LoraLoaderModelOnly, CR Text, UNETLoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Flux2Scheduler, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 加强了一致性 林耀3.6_2029755418074947585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein9B 图像编辑工作流 加强了一致性 林耀3.6_2029755418074947585.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `PreviewImage`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `VAELoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `PreviewImage`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `VAELoader`
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `Flux2Scheduler`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **89%**（40/45）

**有卡**：`ReferenceLatent`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`VAEEncode`、`CFGGuider`、`EmptyFlux2LatentImage`、`GetImageSize`、`VAELoader`、`Flux2Scheduler`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`RandomNoise`、`KSamplerSelect`、`LoraLoaderModelOnly`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`CR Text`、`ImageScaleToTotalPixels`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
