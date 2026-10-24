---
key: 图片生成/图生图/FLUX.2- klein单图图编辑_2012069959744098306.json
name: FLUX.2- klein单图图编辑_2012069959744098306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2- klein单图图编辑_2012069959744098306.json
hash: 66ebf1703acda894
coverage: 0.809524
learned_at: 2026-10-23 10:54:10
nodes: [Anything Everywhere3, UNETLoader, easy showAnything, CR Text, Any Switch (rgthree), CLIPTextEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Qwen3_VQA, MarkdownNote, MarkdownNote, VAELoader, CLIPLoader, LayerUtility: ImageReelComposit, easy imageSize, EmptyFlux2LatentImage, EmptyFlux2LatentImage, Note, FluxGuidance, ReferenceLatent, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, Flux2Scheduler, SaveImage, LayerUtility: ImageReel, CR Latent Input Switch, CR SDXL Aspect Ratio, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, Any Switch (rgthree), Fast Groups Bypasser (rgthree), SaveImage, CR Text]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2- klein单图图编辑_2012069959744098306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2- klein单图图编辑_2012069959744098306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `easy showAnything`
- `CR Text`
- `Any Switch (rgthree)`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Qwen3_VQA`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: ImageReelComposit`
- `easy imageSize`
- `EmptyFlux2LatentImage`
- `EmptyFlux2LatentImage`
- `Note`
- `FluxGuidance`
- `ReferenceLatent`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Flux2Scheduler`
- `SaveImage`
- `LayerUtility: ImageReel`
- `CR Latent Input Switch`
- `CR SDXL Aspect Ratio`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `CR Text`

## 知识

覆盖率 **81%**（34/42）

**有卡**：`UNETLoader`、`CR Text`、`CLIPTextEncode`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Qwen3_VQA`、`VAELoader`、`CLIPLoader`、`LayerUtility: ImageReelComposit`、`easy imageSize`、`EmptyFlux2LatentImage`、`FluxGuidance`、`ReferenceLatent`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`Flux2Scheduler`、`SaveImage`、`LayerUtility: ImageReel`、`CR Latent Input Switch`、`CR SDXL Aspect Ratio`、`CR Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
