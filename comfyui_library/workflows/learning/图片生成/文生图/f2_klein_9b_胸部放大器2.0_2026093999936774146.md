---
key: 图片生成/文生图/f2_klein_9b_胸部放大器2.0_2026093999936774146.json
name: f2_klein_9b_胸部放大器2.0_2026093999936774146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/f2_klein_9b_胸部放大器2.0_2026093999936774146.json
hash: af099f979b943887
coverage: 0.742857
learned_at: 2026-10-19 22:30:10
nodes: [LoadImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Comparer (rgthree), KSamplerSelect, Flux2Scheduler, RandomNoise, easy cleanGpuUsed, SetNode, VAELoader, SetNode, ConditioningZeroOut, GetNode, GetNode, VAEEncode, ReferenceLatent, ReferenceLatent, CFGGuider, GetImageSize, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, UNETLoader, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, SetNode, GetNode, GetNode, SaveImage, SaveImage, easy imageScaleDownToSize, JWInteger, CR Text, Note]
patterns: []
missing: []
---

# 图片生成/文生图/f2_klein_9b_胸部放大器2.0_2026093999936774146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/f2_klein_9b_胸部放大器2.0_2026093999936774146.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LoadImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `RandomNoise`
- `easy cleanGpuUsed`
- `SetNode`
- `VAELoader`
- `SetNode`
- `ConditioningZeroOut`
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
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `SaveImage`
- `easy imageScaleDownToSize`
- `JWInteger`
- `CR Text`
- `Note`

## 知识

覆盖率 **74%**（26/35）

**有卡**：`LoadImage`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`KSamplerSelect`、`Flux2Scheduler`、`RandomNoise`、`easy cleanGpuUsed`、`VAELoader`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`CFGGuider`、`GetImageSize`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SaveImage`、`easy imageScaleDownToSize`、`JWInteger`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
