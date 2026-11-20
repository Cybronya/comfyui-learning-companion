---
key: 平台全量/😯Flux.1 fill+ACE+Redux （自动抠图版）换装_服装迁移_1953165783826370561.json
name: 😯Flux.1 fill+ACE+Redux （自动抠图版）换装_服装迁移_1953165783826370561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Redux （自动抠图版）换装_服装迁移_1953165783826370561.json
hash: 40c79b05720aa243
coverage: 0.471831
learned_at: 2026-11-14 02:55:20
nodes: [LayerMask: MaskPreview, SetNode, PreviewImage, SetNode, EmptyImage, MaskToImage, easy imageConcat, ImageToMask, DifferentialDiffusion, GetNode, SetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, InpaintModelConditioning, GetNode, VAEDecode, PreviewImage, GetNode, GetNode, ImageCrop+, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ConditioningZeroOut, SetNode, SetNode, PreviewImage, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, StyleModelLoader, CLIPVisionLoader, SetNode, GetNode, SetNode, BasicScheduler, GetNode, SetNode, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, easy imageConcat, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, ShowText|pysssss, PrimitiveInt, FluxGuidance, GetNode, ModelSamplingFlux, GetNode, CLIPTextEncodeFlux, GetNode, SetNode, LayerMask: MaskPreview, RandomNoise, SetNode, LayerMask: MaskGrow, DualCLIPLoaderGGUF, Mask Fill Holes, VAELoader, SetNode, GetNode, BasicGuider, SamplerCustomAdvanced, GetNode, CFGZeroStar, GetNode, ReduxAdvanced, LoadImage, SetNode, SetNode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, RepeatLatentBatch, RebatchLatents, easy imageRemBg, easy cleanGpuUsed, ImageAndMaskPreview, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: SegformerB2ClothesUltra, LoadImage, RH_Translator, LayerMask: PersonMaskUltra V2, DWPreprocessor, PreviewImage, SetNode, AIO_Preprocessor, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: Brightness & Contrast, GetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, GetNode, GetNode, SetUnionControlNetType, ControlNetLoader, SetNode, ControlNetApplySD3, GetNode, EmptyImage, GetNode, easy imageConcat, SetNode, PreviewImage, GetNode, GetNode, GetNode, SetNode, easy imageRemBg, easy cleanGpuUsed, GetNode, GetNode, SetNode, easy imageRemBg, PreviewImage, SetNode, TeaCache, SaveImage, BackgroundScaler, SaveImage, LayerMask: MaskGrow, SubtractMask, Masks Combine Regions, LayerMask: SegmentAnythingUltra V2]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.8000000000000002}
---

# 平台全量/😯Flux.1 fill+ACE+Redux （自动抠图版）换装_服装迁移_1953165783826370561.json

> 来源文件 `comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Redux （自动抠图版）换装_服装迁移_1953165783826370561.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（142 个）：
- `LayerMask: MaskPreview`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `EmptyImage`
- `MaskToImage`
- `easy imageConcat`
- `ImageToMask`
- `DifferentialDiffusion`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `InpaintModelConditioning`
- `GetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetNode`
- `GetNode`
- `ImageCrop+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `BasicScheduler`
- `GetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageConcat`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ShowText|pysssss`
- `PrimitiveInt`
- `FluxGuidance`
- `GetNode`
- `ModelSamplingFlux`
- `GetNode`
- `CLIPTextEncodeFlux` ★核心
- `GetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `RandomNoise`
- `SetNode`
- `LayerMask: MaskGrow`
- `DualCLIPLoaderGGUF`
- `Mask Fill Holes`
- `VAELoader`
- `SetNode`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGZeroStar`
- `GetNode`
- `ReduxAdvanced`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RepeatLatentBatch`
- `RebatchLatents`
- `easy imageRemBg`
- `easy cleanGpuUsed`
- `ImageAndMaskPreview`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: SegformerB2ClothesUltra`
- `LoadImage`
- `RH_Translator`
- `LayerMask: PersonMaskUltra V2`
- `DWPreprocessor`
- `PreviewImage`
- `SetNode`
- `AIO_Preprocessor`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: Brightness & Contrast`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `SetNode`
- `ControlNetApplySD3` ★核心
- `GetNode`
- `EmptyImage`
- `GetNode`
- `easy imageConcat`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy imageRemBg`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy imageRemBg`
- `PreviewImage`
- `SetNode`
- `TeaCache`
- `SaveImage`
- `BackgroundScaler`
- `SaveImage`
- `LayerMask: MaskGrow`
- `SubtractMask`
- `Masks Combine Regions`
- `LayerMask: SegmentAnythingUltra V2`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **47%**（67/142）

**有卡**：`LayerMask: MaskPreview`、`EmptyImage`、`MaskToImage`、`easy imageConcat`、`ImageToMask`、`DifferentialDiffusion`、`KSamplerSelect`、`InpaintModelConditioning`、`VAEDecode`、`ImageCrop+`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`StyleModelLoader`、`CLIPVisionLoader`、`BasicScheduler`、`LayerUtility: CropByMask V2`、`FluxGuidance`、`ModelSamplingFlux`、`CLIPTextEncodeFlux`、`RandomNoise`、`LayerMask: MaskGrow`、`DualCLIPLoaderGGUF`、`Mask Fill Holes`、`VAELoader`、`BasicGuider`、`SamplerCustomAdvanced`、`CFGZeroStar`、`ReduxAdvanced`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`RepeatLatentBatch`、`RebatchLatents`、`easy imageRemBg`、`easy cleanGpuUsed`、`ImageAndMaskPreview`、`LayerMask: SegformerB2ClothesUltra`、`RH_Translator`、`LayerMask: PersonMaskUltra V2`、`DWPreprocessor`、`AIO_Preprocessor`、`LayerColor: Brightness & Contrast`、`SetUnionControlNetType`、`ControlNetLoader`、`ControlNetApplySD3`、`TeaCache`、`SaveImage`、`BackgroundScaler`、`SubtractMask`、`Masks Combine Regions`、`LayerMask: SegmentAnythingUltra V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、ControlNetApplySD3、ControlNetLoader
