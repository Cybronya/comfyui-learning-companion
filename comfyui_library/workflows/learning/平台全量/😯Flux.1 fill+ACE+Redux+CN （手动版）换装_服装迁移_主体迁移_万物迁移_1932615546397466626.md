---
key: 平台全量/😯Flux.1 fill+ACE+Redux+CN （手动版）换装_服装迁移_主体迁移_万物迁移_1932615546397466626.json
name: 😯Flux.1 fill+ACE+Redux+CN （手动版）换装_服装迁移_主体迁移_万物迁移_1932615546397466626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Redux+CN （手动版）换装_服装迁移_主体迁移_万物迁移_1932615546397466626.json
hash: 432b05061fac4180
coverage: 0.441176
learned_at: 2026-11-14 02:55:24
nodes: [LayerMask: MaskPreview, SetNode, SetNode, EmptyImage, MaskToImage, easy imageConcat, ImageToMask, DifferentialDiffusion, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, InpaintModelConditioning, GetNode, VAEDecode, PreviewImage, GetNode, GetNode, ImageCrop+, GetNode, GetNode, GetNode, SaveImage, SetNode, SetNode, SetNode, SetNode, SetNode, ConditioningZeroOut, SetNode, SetNode, SetNode, PreviewImage, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, GetNode, StyleModelLoader, CLIPVisionLoader, SetNode, GetNode, SetNode, GetNode, SetNode, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, easy imageConcat, SetNode, SetNode, GetNode, SetNode, FluxGuidance, GetNode, ModelSamplingFlux, GetNode, CLIPTextEncodeFlux, GetNode, UNETLoader, SetNode, GetNode, SetNode, LayerMask: MaskPreview, RandomNoise, SetNode, LayerMask: MaskGrow, PreviewImage, DualCLIPLoaderGGUF, Mask Fill Holes, VAELoader, SetNode, GetNode, BasicGuider, SamplerCustomAdvanced, GetNode, CFGZeroStar, GetNode, GetNode, GetNode, RepeatLatentBatch, RebatchLatents, GetNode, GetNode, KSamplerSelect, GetNode, ReduxAdvanced, GetNode, SetUnionControlNetType, ControlNetLoader, SetNode, DWPreprocessor, PreviewImage, SetNode, AIO_Preprocessor, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: Brightness & Contrast, GetNode, LayerUtility: ImageScaleByAspectRatio V2, EmptyImage, GetNode, easy imageConcat, SetNode, PreviewImage, GetNode, GetNode, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, easy cleanGpuUsed, GetNode, SetNode, PreviewImage, easy imageRemBg, easy imageRemBg, BackgroundScaler, TeaCache, ShowText|pysssss, LoadImage, Mask Fill Holes, BasicScheduler, ControlNetApplySD3, PreviewImage, LayerMask: MaskGrow, LoraLoaderModelOnly, LoadImage, RH_Translator, SaveImage, easy seed, GetNode]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.8000000000000002}
---

# 平台全量/😯Flux.1 fill+ACE+Redux+CN （手动版）换装_服装迁移_主体迁移_万物迁移_1932615546397466626.json

> 来源文件 `comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Redux+CN （手动版）换装_服装迁移_主体迁移_万物迁移_1932615546397466626.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
- `LayerMask: MaskPreview`
- `SetNode`
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
- `SaveImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `GetNode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageConcat`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `FluxGuidance`
- `GetNode`
- `ModelSamplingFlux`
- `GetNode`
- `CLIPTextEncodeFlux` ★核心
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `RandomNoise`
- `SetNode`
- `LayerMask: MaskGrow`
- `PreviewImage`
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
- `GetNode`
- `GetNode`
- `RepeatLatentBatch`
- `RebatchLatents`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ReduxAdvanced`
- `GetNode`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `SetNode`
- `DWPreprocessor`
- `PreviewImage`
- `SetNode`
- `AIO_Preprocessor`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: Brightness & Contrast`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyImage`
- `GetNode`
- `easy imageConcat`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `easy imageRemBg`
- `easy imageRemBg`
- `BackgroundScaler`
- `TeaCache`
- `ShowText|pysssss`
- `LoadImage`
- `Mask Fill Holes`
- `BasicScheduler`
- `ControlNetApplySD3` ★核心
- `PreviewImage`
- `LayerMask: MaskGrow`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `RH_Translator`
- `SaveImage`
- `easy seed`
- `GetNode`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **44%**（60/136）

**有卡**：`LayerMask: MaskPreview`、`EmptyImage`、`MaskToImage`、`easy imageConcat`、`ImageToMask`、`DifferentialDiffusion`、`InpaintModelConditioning`、`VAEDecode`、`ImageCrop+`、`SaveImage`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`StyleModelLoader`、`CLIPVisionLoader`、`LayerUtility: CropByMask V2`、`FluxGuidance`、`ModelSamplingFlux`、`CLIPTextEncodeFlux`、`UNETLoader`、`RandomNoise`、`LayerMask: MaskGrow`、`DualCLIPLoaderGGUF`、`Mask Fill Holes`、`VAELoader`、`BasicGuider`、`SamplerCustomAdvanced`、`CFGZeroStar`、`RepeatLatentBatch`、`RebatchLatents`、`KSamplerSelect`、`ReduxAdvanced`、`SetUnionControlNetType`、`ControlNetLoader`、`DWPreprocessor`、`AIO_Preprocessor`、`LayerColor: Brightness & Contrast`、`easy cleanGpuUsed`、`easy imageRemBg`、`BackgroundScaler`、`TeaCache`、`LoadImage`、`BasicScheduler`、`ControlNetApplySD3`、`LoraLoaderModelOnly`、`RH_Translator`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、LoadImage、ControlNetApplySD3、ControlNetLoader
