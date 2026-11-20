---
key: 平台全量/Flux.1+Removal+sam3自动分割主体与背景重绘-抠图背景_主体移除_分割背景_擦除前景_1930917577894375425.json
name: Flux.1+Removal+sam3自动分割主体与背景重绘-抠图背景_主体移除_分割背景_擦除前景_1930917577894375425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1+Removal+sam3自动分割主体与背景重绘-抠图背景_主体移除_分割背景_擦除前景_1930917577894375425.json
hash: c84a81af426e29d3
coverage: 0.556962
learned_at: 2026-11-14 00:28:48
nodes: [BasicGuider, SamplerCustomAdvanced, GetNode, GetNode, SetNode, easy cleanGpuUsed, SetNode, LoraLoaderModelOnly, TeaCache, DualCLIPLoader, GetNode, ModelSamplingFlux, CFGZeroStar, DifferentialDiffusion, Anything Everywhere, VAEDecode, Anything Everywhere, VAELoader, Anything Everywhere, InpaintModelConditioning, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, GetNode, GetNode, RandomNoise, UNETLoader, SetNode, GetNode, KSamplerSelect, BasicScheduler, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Int, GetNode, AddMask, SetNode, RH_Translator, easy imageRemBg, SetNode, PreviewImage, SetNode, SetNode, SaveImage, MaskPreview+, SAM3Segmentation, InpaintCropImproved, LoadJanusModel, JanusImage2Text, LoadSAM3Model, RH_Translator, easy showAnything, LayerUtility: TextJoin, ShowText|pysssss, SetNode, SetNode, JoinImageWithAlpha, SaveImage, SaveImage, InvertMask (segment anything), InpaintStitchImproved, AILab_LamaRemover, DrawMaskOnImage, ImpactSwitch, ToBinaryMask, GetNode, SetNode, LoadImage, MaskPreview+, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SaveImage]
patterns: []
missing: []
---

# 平台全量/Flux.1+Removal+sam3自动分割主体与背景重绘-抠图背景_主体移除_分割背景_擦除前景_1930917577894375425.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1+Removal+sam3自动分割主体与背景重绘-抠图背景_主体移除_分割背景_擦除前景_1930917577894375425.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `DualCLIPLoader`
- `GetNode`
- `ModelSamplingFlux`
- `CFGZeroStar`
- `DifferentialDiffusion`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `Anything Everywhere`
- `VAELoader`
- `Anything Everywhere`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `GetNode`
- `AddMask`
- `SetNode`
- `RH_Translator`
- `easy imageRemBg`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SaveImage`
- `MaskPreview+`
- `SAM3Segmentation`
- `InpaintCropImproved`
- `LoadJanusModel`
- `JanusImage2Text`
- `LoadSAM3Model`
- `RH_Translator`
- `easy showAnything`
- `LayerUtility: TextJoin`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `JoinImageWithAlpha`
- `SaveImage`
- `SaveImage`
- `InvertMask (segment anything)`
- `InpaintStitchImproved`
- `AILab_LamaRemover`
- `DrawMaskOnImage`
- `ImpactSwitch`
- `ToBinaryMask`
- `GetNode`
- `SetNode`
- `LoadImage`
- `MaskPreview+`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`

## 知识

覆盖率 **56%**（44/79）

**有卡**：`BasicGuider`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`TeaCache`、`DualCLIPLoader`、`ModelSamplingFlux`、`CFGZeroStar`、`DifferentialDiffusion`、`VAEDecode`、`VAELoader`、`InpaintModelConditioning`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`RandomNoise`、`UNETLoader`、`KSamplerSelect`、`BasicScheduler`、`Int`、`AddMask`、`RH_Translator`、`easy imageRemBg`、`SaveImage`、`MaskPreview+`、`SAM3Segmentation`、`InpaintCropImproved`、`LoadJanusModel`、`JanusImage2Text`、`LoadSAM3Model`、`LayerUtility: TextJoin`、`JoinImageWithAlpha`、`InvertMask (segment anything)`、`InpaintStitchImproved`、`AILab_LamaRemover`、`DrawMaskOnImage`、`ToBinaryMask`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGZeroStar
