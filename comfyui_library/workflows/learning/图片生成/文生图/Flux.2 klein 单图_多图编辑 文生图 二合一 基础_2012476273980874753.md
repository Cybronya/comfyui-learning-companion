---
key: 图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json
name: Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json
hash: e77163d38b2f6fcb
coverage: 0.525253
learned_at: 2026-10-19 22:15:01
nodes: [Anything Everywhere, VAELoader, Anything Everywhere, CLIPLoader, UNETLoader, CFGGuider, Anything Everywhere, VAEDecode, VAEEncode, GetNode, VAEEncode, ReferenceLatent, Int, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetImageSize, GetNode, ConditioningZeroOut, SetNode, Int, Int, SetNode, Flux2Scheduler, SetNode, GetNode, ImpactSwitch, Note, PreviewImage, UNETLoader, CLIPLoader, Note, SetNode, SetNode, Int, GetNode, EmptyFlux2LatentImage, GetNode, Note, RepeatLatentBatch, Int, Note, PreviewImage, FastCanvas, Note, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, 孤海-图像与遮罩描边, FastCanvasTool, SetNode, SetNode, LoadImage, Note, LoadImage, Qwen3_VQA, PreviewAny, LoadImage, DrawMaskOnImage, LoadImage, SetNode, SetNode, GetNode, KSamplerSelect, SamplerCustomAdvanced, RebatchLatents, ImpactSwitch, ImpactSwitch, AIO_Preprocessor, Note, JoinImageWithAlpha, easy imageRemBg, JoinImageWithAlpha, Note, PreviewImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, VAEEncode, ReferenceLatent, ReferenceLatent, ImpactSwitch, GetNode, GetNode, GetNode, LoadImage, Note, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, RandomNoise, CLIPTextEncode, easy seed, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2 klein 单图_多图编辑 文生图 二合一 基础_2012476273980874753.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `Anything Everywhere`
- `VAELoader`
- `Anything Everywhere`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CFGGuider`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `Int`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `Int`
- `Int`
- `SetNode`
- `Flux2Scheduler`
- `SetNode`
- `GetNode`
- `ImpactSwitch`
- `Note`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Note`
- `SetNode`
- `SetNode`
- `Int`
- `GetNode`
- `EmptyFlux2LatentImage`
- `GetNode`
- `Note`
- `RepeatLatentBatch`
- `Int`
- `Note`
- `PreviewImage`
- `FastCanvas`
- `Note`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `孤海-图像与遮罩描边`
- `FastCanvasTool`
- `SetNode`
- `SetNode`
- `LoadImage`
- `Note`
- `LoadImage`
- `Qwen3_VQA`
- `PreviewAny`
- `LoadImage`
- `DrawMaskOnImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RebatchLatents`
- `ImpactSwitch`
- `ImpactSwitch`
- `AIO_Preprocessor`
- `Note`
- `JoinImageWithAlpha`
- `easy imageRemBg`
- `JoinImageWithAlpha`
- `Note`
- `PreviewImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `easy seed`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **53%**（52/99）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`CFGGuider`、`VAEDecode`、`VAEEncode`、`ReferenceLatent`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`ConditioningZeroOut`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`RepeatLatentBatch`、`FastCanvas`、`LoadImage`、`孤海-图像与遮罩描边`、`FastCanvasTool`、`Qwen3_VQA`、`DrawMaskOnImage`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RebatchLatents`、`AIO_Preprocessor`、`JoinImageWithAlpha`、`easy imageRemBg`、`SaveImage`、`RandomNoise`、`CLIPTextEncode`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
