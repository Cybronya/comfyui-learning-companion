---
key: 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json
name: Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json
hash: c56ad293944d2b32
coverage: 0.892857
learned_at: 2026-10-23 10:59:29
nodes: [KSamplerSelect, CLIPLoader, VAELoader, CFGGuider, ConditioningZeroOut, RandomNoise, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleBy, SeedVR2VideoUpscaler, Image Comparer (rgthree), SaveImage, SaveImage, UNETLoader, GetImageSize, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, SamplerCustomAdvanced, VAEDecode, ReferenceLatent, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, PreviewImage, LoadImage, CLIPTextEncode, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `ConditioningZeroOut`
- `RandomNoise`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`KSamplerSelect`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`ConditioningZeroOut`、`RandomNoise`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`SaveImage`、`UNETLoader`、`GetImageSize`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`ReferenceLatent`、`VAEEncode`、`ImageScaleToTotalPixels`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
