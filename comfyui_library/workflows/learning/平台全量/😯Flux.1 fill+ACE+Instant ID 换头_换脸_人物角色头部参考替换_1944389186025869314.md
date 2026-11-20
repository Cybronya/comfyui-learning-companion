---
key: 平台全量/😯Flux.1 fill+ACE+Instant ID 换头_换脸_人物角色头部参考替换_1944389186025869314.json
name: 😯Flux.1 fill+ACE+Instant ID 换头_换脸_人物角色头部参考替换_1944389186025869314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Instant ID 换头_换脸_人物角色头部参考替换_1944389186025869314.json
hash: 064925d0e9e211cc
coverage: 0.469388
learned_at: 2026-11-14 02:55:20
nodes: [SetNode, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, ApplyInstantID, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, VAEDecode, GetNode, LayerMask: PersonMaskUltra V2, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, DualCLIPLoader, GetImageSize, SetNode, SetNode, GetNode, easy imageRemBg, Anything Everywhere, Anything Everywhere, DifferentialDiffusion, TeaCache, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, FluxGuidance, ConditioningZeroOut, SetNode, CLIPTextEncode, GetNode, SetNode, PreviewImage, EmptyImage, GetNode, easy imageConcat, GetNode, SetNode, PulidFluxModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, GetNode, GetNode, SetNode, Int, GetNode, Anything Everywhere, LayerMask: PersonMaskUltra V2, InpaintCropImproved, SetNode, PreviewImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ControlNetApplySD3, SetNode, DifferentialDiffusion, InpaintModelConditioning, InpaintCropImproved, InpaintStitchImproved, CheckpointLoaderSimple, GetNode, InstantIDModelLoader, SetNode, GetNode, GetNode, OnnxDetectionModelLoader, SetNode, SetNode, SetNode, PreviewImage, easy makeImageForICLora, RepeatLatentBatch, RebatchLatents, GetNode, VAEDecode, SetNode, SetNode, GetNode, GetNode, ImageCrop+, InpaintCropImproved, GetNode, SetNode, ImageAndMaskPreview, SetNode, SetNode, LayerMask: PersonMaskUltra V2, SegsToCombinedMask, SetUnionControlNetType, ControlNetLoader, GetNode, ImageAndMaskPreview, SetNode, SetNode, GetNode, GetNode, Reroute, GetNode, PoseDetectionOneToAllAnimation, ReduxAdvanced, ApplyPulidFlux, GetNode, SetNode, GetNode, LayerMask: PersonMaskUltra V2, easy imageRemBg, GetNode, Reroute, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, ImpactSwitch, Reroute, InpaintStitchImproved, GetNode, GetNode, LayerMask: MaskGrow, LayerMask: MaskGrow, ImpactSwitch, SetNode, InpaintStitchImproved, GetNode, GetNode, ImageAndMaskPreview, InpaintCropImproved, SetNode, ImageAndMaskPreview, LoraLoaderModelOnly, easy seed, UNETLoader, Int, LoadImage, KSampler, PreviewImage, InvertMask (segment anything), InvertMask (segment anything), MaskToSEGS, LoadImage, LayerMask: PersonMaskUltra V2, GetNode, BlockifyMask, ImpactConditionalBranch, ImpactSwitch, easy boolean, ImageCompositeMasked, ImageCompositeMasked, GetNode, GetNode, LayerMask: MaskGrow, LayerMask: MaskGrow, LayerMask: MaskGrow, InpaintModelConditioning, ImageSmartSharpen+, PreviewImage, CR Text, StyleModelLoader, CLIPVisionLoader, VAELoader, PreviewImage, SaveImage, SaveImage, GetNode, workflow>mask mover, GetNode, UNETLoader, GetNode, GetNode, GetNode, GetNode, GetNode, PIP_图像联结, SaveImage, PIP_图像联结]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "controlnet_strength": 0.8000000000000002, "denoise": 0.9000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 10}
---

# 平台全量/😯Flux.1 fill+ACE+Instant ID 换头_换脸_人物角色头部参考替换_1944389186025869314.json

> 来源文件 `comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Instant ID 换头_换脸_人物角色头部参考替换_1944389186025869314.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（196 个）：
- `SetNode`
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `SetNode`
- `SetNode`
- `ApplyInstantID`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `GetImageSize`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy imageRemBg`
- `Anything Everywhere`
- `Anything Everywhere`
- `DifferentialDiffusion`
- `TeaCache`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FluxGuidance`
- `ConditioningZeroOut`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `PreviewImage`
- `EmptyImage`
- `GetNode`
- `easy imageConcat`
- `GetNode`
- `SetNode`
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `Int`
- `GetNode`
- `Anything Everywhere`
- `LayerMask: PersonMaskUltra V2`
- `InpaintCropImproved`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ControlNetApplySD3` ★核心
- `SetNode`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `InstantIDModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `easy makeImageForICLora`
- `RepeatLatentBatch`
- `RebatchLatents`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageCrop+`
- `InpaintCropImproved`
- `GetNode`
- `SetNode`
- `ImageAndMaskPreview`
- `SetNode`
- `SetNode`
- `LayerMask: PersonMaskUltra V2`
- `SegsToCombinedMask`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `GetNode`
- `ImageAndMaskPreview`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `PoseDetectionOneToAllAnimation`
- `ReduxAdvanced`
- `ApplyPulidFlux`
- `GetNode`
- `SetNode`
- `GetNode`
- `LayerMask: PersonMaskUltra V2`
- `easy imageRemBg`
- `GetNode`
- `Reroute`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImpactSwitch`
- `Reroute`
- `InpaintStitchImproved`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `ImpactSwitch`
- `SetNode`
- `InpaintStitchImproved`
- `GetNode`
- `GetNode`
- `ImageAndMaskPreview`
- `InpaintCropImproved`
- `SetNode`
- `ImageAndMaskPreview`
- `LoraLoaderModelOnly` ★核心
- `easy seed`
- `UNETLoader` ★核心
- `Int`
- `LoadImage`
- `KSampler` ★核心
- `PreviewImage`
- `InvertMask (segment anything)`
- `InvertMask (segment anything)`
- `MaskToSEGS`
- `LoadImage`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `BlockifyMask`
- `ImpactConditionalBranch`
- `ImpactSwitch`
- `easy boolean`
- `ImageCompositeMasked`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `InpaintModelConditioning`
- `ImageSmartSharpen+`
- `PreviewImage`
- `CR Text`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `workflow>mask mover`
- `GetNode`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PIP_图像联结`
- `SaveImage`
- `PIP_图像联结`

## 关键参数

- `seed` = `0`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.9000000000000001`
- `controlnet_strength` = `0.8000000000000002`
- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`

## 知识

覆盖率 **47%**（92/196）

**有卡**：`InstantIDFaceAnalysis`、`ControlNetLoader`、`ApplyInstantID`、`CLIPTextEncode`、`easy cleanGpuUsed`、`VAEDecode`、`LayerMask: PersonMaskUltra V2`、`LoraLoaderModelOnly`、`KSampler`、`DualCLIPLoader`、`GetImageSize`、`easy imageRemBg`、`DifferentialDiffusion`、`TeaCache`、`FluxGuidance`、`ConditioningZeroOut`、`EmptyImage`、`easy imageConcat`、`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`Int`、`InpaintCropImproved`、`ControlNetApplySD3`、`InpaintModelConditioning`、`InpaintStitchImproved`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`OnnxDetectionModelLoader`、`easy makeImageForICLora`、`RepeatLatentBatch`、`RebatchLatents`、`ImageCrop+`、`ImageAndMaskPreview`、`SegsToCombinedMask`、`SetUnionControlNetType`、`PoseDetectionOneToAllAnimation`、`ReduxAdvanced`、`ApplyPulidFlux`、`LayerMask: MaskGrow`、`easy seed`、`UNETLoader`、`LoadImage`、`InvertMask (segment anything)`、`MaskToSEGS`、`BlockifyMask`、`ImpactConditionalBranch`、`easy boolean`、`ImageCompositeMasked`、`ImageSmartSharpen+`、`CR Text`、`StyleModelLoader`、`CLIPVisionLoader`、`VAELoader`、`SaveImage`、`workflow>mask mover`、`PIP_图像联结`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut
