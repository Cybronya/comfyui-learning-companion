---
key: 图片生成/图生图/f2_klein_9b_胸部放大器2.0_2021777540951580673.json
name: f2_klein_9b_胸部放大器2.0_2021777540951580673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/f2_klein_9b_胸部放大器2.0_2021777540951580673.json
hash: 9825619f26bf05f5
coverage: 0.742857
learned_at: 2026-10-23 11:34:45
nodes: [LoadImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Comparer (rgthree), KSamplerSelect, SaveImage, Flux2Scheduler, RandomNoise, CR Text, SaveImage, easy cleanGpuUsed, SetNode, VAELoader, SetNode, SetNode, GetNode, easy imageScaleDownToSize, ConditioningZeroOut, GetNode, GetNode, GetNode, VAEEncode, ReferenceLatent, ReferenceLatent, CFGGuider, GetImageSize, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, Fast Groups Bypasser (rgthree), UNETLoader, CLIPLoader, CLIPTextEncode, JWInteger, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/f2_klein_9b_胸部放大器2.0_2021777540951580673.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/f2_klein_9b_胸部放大器2.0_2021777540951580673.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LoadImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `SaveImage`
- `Flux2Scheduler`
- `RandomNoise`
- `CR Text`
- `SaveImage`
- `easy cleanGpuUsed`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy imageScaleDownToSize`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CFGGuider`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **74%**（26/35）

**有卡**：`LoadImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`KSamplerSelect`、`SaveImage`、`Flux2Scheduler`、`RandomNoise`、`CR Text`、`easy cleanGpuUsed`、`VAELoader`、`easy imageScaleDownToSize`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`CFGGuider`、`GetImageSize`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`JWInteger`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
