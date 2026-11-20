---
key: 平台全量/😯Flux.1 Redux+Ace+IBM 换背景_参考背景-原图IBM打光-v1b_1948373222680068097.json
name: 😯Flux.1 Redux+Ace+IBM 换背景_参考背景-原图IBM打光-v1b_1948373222680068097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/😯Flux.1 Redux+Ace+IBM 换背景_参考背景-原图IBM打光-v1b_1948373222680068097.json
hash: bc5432f8c9f00712
coverage: 0.492857
learned_at: 2026-11-14 02:55:18
nodes: [PreviewImage, easy imageConcat, GetNode, GetNode, GetNode, RandomNoise, SetNode, VAEDecode, SetNode, ConditioningZeroOut, SetNode, GetNode, SetNode, DifferentialDiffusion, SetNode, BasicGuider, GetNode, RebatchLatents, RepeatLatentBatch, easy cleanGpuUsed, GetNode, SetNode, easy textSwitch, CLIPTextEncode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, InpaintModelConditioning, SamplerCustomAdvanced, GetNode, GetNode, SaveImage, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, easy imageConcat, GetNode, GetNode, GetNode, RH_LLMAPI_NODE, CR Text Concatenate, EmptyImage, SetNode, easy imageConcat, MaskToImage, ImageToMask, LayerMask: MaskPreview, BiRefNetRMBG, LayerUtility: ImageScaleByAspectRatio V2, GetNode, ImageCrop+, GetNode, LayerMask: MaskPreview, LayerMask: MaskPreview, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LoraLoaderModelOnly, GetNode, GetNode, GetNode, LayerMask: MaskPreview, SetNode, LayerMask: MaskGrow, SaveImage, GetNode, FluxGuidance, GetNode, StyleModelLoader, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, LayerMask: MaskGrow, GetNode, LoadLBMModel, LBMSampler, GetNode, ImageSmartSharpen+, GetNode, SetNode, SetNode, easy seed, ReduxAdvanced, ShowText|pysssss, LayerMask: MaskGrow, SetNode, VAELoader, LayerFilter: HDREffects, DetailTransfer, SaveImage, LoadImage, LoadImage, PreviewImage, INPAINT_MaskedFill, LayerMask: MaskGrow, BiRefNetRMBG, PreviewImage, GetNode, LayerMask: MaskGrow, GetNode, ImageSmartSharpen+, SaveImage, BiRefNetRMBG, PreviewImage, PreviewImage, ColorMatch, SaveImage, GetNode, GetNode, SaveImage, easy imageConcat, LoraLoaderModelOnly, TeaCache, DualCLIPLoader, GetNode, GetNode, RH_Translator, KSamplerSelect, BasicScheduler, LoraLoaderModelOnly, UNETLoader, UNETLoader]
patterns: []
missing: []
---

# 平台全量/😯Flux.1 Redux+Ace+IBM 换背景_参考背景-原图IBM打光-v1b_1948373222680068097.json

> 来源文件 `comfyui_library/workflows/平台全量/😯Flux.1 Redux+Ace+IBM 换背景_参考背景-原图IBM打光-v1b_1948373222680068097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（140 个）：
- `PreviewImage`
- `easy imageConcat`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `SetNode`
- `DifferentialDiffusion`
- `SetNode`
- `BasicGuider`
- `GetNode`
- `RebatchLatents`
- `RepeatLatentBatch`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `easy textSwitch`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InpaintModelConditioning`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SaveImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy imageConcat`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `CR Text Concatenate`
- `EmptyImage`
- `SetNode`
- `easy imageConcat`
- `MaskToImage`
- `ImageToMask`
- `LayerMask: MaskPreview`
- `BiRefNetRMBG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `ImageCrop+`
- `GetNode`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `LayerMask: MaskGrow`
- `SaveImage`
- `GetNode`
- `FluxGuidance`
- `GetNode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerMask: MaskGrow`
- `GetNode`
- `LoadLBMModel`
- `LBMSampler` ★核心
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy seed`
- `ReduxAdvanced`
- `ShowText|pysssss`
- `LayerMask: MaskGrow`
- `SetNode`
- `VAELoader`
- `LayerFilter: HDREffects`
- `DetailTransfer`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `INPAINT_MaskedFill`
- `LayerMask: MaskGrow`
- `BiRefNetRMBG`
- `PreviewImage`
- `GetNode`
- `LayerMask: MaskGrow`
- `GetNode`
- `ImageSmartSharpen+`
- `SaveImage`
- `BiRefNetRMBG`
- `PreviewImage`
- `PreviewImage`
- `ColorMatch`
- `SaveImage`
- `GetNode`
- `GetNode`
- `SaveImage`
- `easy imageConcat`
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `RH_Translator`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 知识

覆盖率 **49%**（69/140）

**有卡**：`easy imageConcat`、`RandomNoise`、`VAEDecode`、`ConditioningZeroOut`、`DifferentialDiffusion`、`BasicGuider`、`RebatchLatents`、`RepeatLatentBatch`、`easy cleanGpuUsed`、`easy textSwitch`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`InpaintModelConditioning`、`SamplerCustomAdvanced`、`SaveImage`、`RH_LLMAPI_NODE`、`CR Text Concatenate`、`EmptyImage`、`MaskToImage`、`ImageToMask`、`LayerMask: MaskPreview`、`BiRefNetRMBG`、`ImageCrop+`、`LoraLoaderModelOnly`、`LayerMask: MaskGrow`、`FluxGuidance`、`StyleModelLoader`、`CLIPVisionLoader`、`LoadLBMModel`、`LBMSampler`、`ImageSmartSharpen+`、`easy seed`、`ReduxAdvanced`、`VAELoader`、`LayerFilter: HDREffects`、`DetailTransfer`、`LoadImage`、`INPAINT_MaskedFill`、`ColorMatch`、`TeaCache`、`DualCLIPLoader`、`RH_Translator`、`KSamplerSelect`、`BasicScheduler`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、easy seed
