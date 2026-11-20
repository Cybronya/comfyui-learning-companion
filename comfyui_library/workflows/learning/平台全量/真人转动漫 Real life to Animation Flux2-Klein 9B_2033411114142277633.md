---
key: 平台全量/真人转动漫 Real life to Animation Flux2-Klein 9B_2033411114142277633.json
name: 真人转动漫 Real life to Animation Flux2-Klein 9B_2033411114142277633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/真人转动漫 Real life to Animation Flux2-Klein 9B_2033411114142277633.json
hash: 716a0be5fc5057fb
coverage: 0.764706
learned_at: 2026-11-14 02:26:32
nodes: [LayerUtility: ImageReelComposit, KSamplerSelect, RandomNoise, easy cleanGpuUsed, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, CFGGuider, SamplerCustomAdvanced, VAEDecode, EmptyFlux2LatentImage, GetImageSize, GetNode, VAEEncode, ReferenceLatent, ConditioningZeroOut, GetNode, CLIPTextEncode, ReferenceLatent, SetNode, Flux2Scheduler, easy imageScaleDownToSize, LoraLoaderModelOnly, GetNode, Image Comparer (rgthree), SaveImage, SaveImage, LayerUtility: ImageReel, UNETLoader, Int, CR Text, LoadImage]
patterns: []
missing: []
---

# 平台全量/真人转动漫 Real life to Animation Flux2-Klein 9B_2033411114142277633.json

> 来源文件 `comfyui_library/workflows/平台全量/真人转动漫 Real life to Animation Flux2-Klein 9B_2033411114142277633.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `LayerUtility: ImageReelComposit`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `GetNode`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `SetNode`
- `Flux2Scheduler`
- `easy imageScaleDownToSize`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `Int`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`LayerUtility: ImageReelComposit`、`KSamplerSelect`、`RandomNoise`、`easy cleanGpuUsed`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`EmptyFlux2LatentImage`、`GetImageSize`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`CLIPTextEncode`、`Flux2Scheduler`、`easy imageScaleDownToSize`、`LoraLoaderModelOnly`、`SaveImage`、`LayerUtility: ImageReel`、`UNETLoader`、`Int`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
