---
key: 平台全量/😯Flux.1 fill+ACE+Redux+CN 主体置换到场景_替换人物_人物迁移_1931796829946445826.json
name: 😯Flux.1 fill+ACE+Redux+CN 主体置换到场景_替换人物_人物迁移_1931796829946445826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Redux+CN 主体置换到场景_替换人物_人物迁移_1931796829946445826.json
hash: ae1c0d492ddf4f56
coverage: 0.455556
learned_at: 2026-11-14 02:55:21
nodes: [PreviewImage, EmptyImage, easy imageConcat, ImageToMask, GetNode, GetNode, GetNode, ImageCrop+, GetNode, GetNode, SetNode, SetNode, SetNode, PreviewImage, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetUnionControlNetType, SetUnionControlNetType, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, ControlNetApplyAdvanced, GetNode, GetNode, LoadImage, LoadImage, GetNode, CR Text Concatenate, CR Text Concatenate, RH_Translator, SetNode, easy seed, SetNode, GetNode, GetNode, RH_LLMAPI_NODE, LoraLoaderModelOnly, TeaCache, DifferentialDiffusion, SetNode, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, SetNode, SetNode, SetNode, easy imageConcat, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, GetNode, LayerMask: MaskGrow, Mask Fill Holes, MaskToImage, GetNode, RandomNoise, GetNode, BasicScheduler, SamplerCustomAdvanced, GetNode, VAEDecode, GetNode, SetNode, InpaintModelConditioning, RepeatLatentBatch, RebatchLatents, BasicGuider, FluxGuidance, StyleModelLoader, CLIPVisionLoader, GetNode, GetNode, SetNode, GetNode, KSamplerSelect, GetNode, ShowText|pysssss, DWPreprocessor, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: Brightness & Contrast, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, SetNode, SetNode, SetNode, SetNode, PreviewImage, SetNode, SetNode, PreviewImage, easy imageConcat, EmptyImage, easy imageConcat, GetNode, GetNode, SetNode, LayerMask: MaskPreview, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, ReduxAdvanced, ReduxAdvanced, GetNode, LayerUtility: ImageScaleByAspectRatio V2, BiRefNetRMBG, SetNode, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, SetNode, CheckpointLoaderSimple, InstantIDModelLoader, DifferentialDiffusion, ApplyInstantID, GetNode, GetNode, CLIPTextEncode, easy cleanGpuUsed, PreviewImage, SetNode, GetNode, GetNode, SetNode, SetNode, PreviewImage, GetNode, PreviewImage, SetNode, LayerMask: MaskPreview, CLIPTextEncode, SetNode, GetNode, GetNode, VAEDecode, GetNode, InpaintModelConditioning, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, KSampler, InpaintStitchImproved, InpaintCropImproved, InpaintCropImproved, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, DualCLIPLoader, SetNode, SetNode, VAELoader, GetNode, CLIPTextEncode, SetNode, ConditioningZeroOut, SetNode, GetNode, RH_LLMAPI_NODE, PreviewImage, ControlNetApplyAdvanced, ControlNetLoader, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "controlnet_strength": 0.8000000000000002, "denoise": 0.5000000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 473412735909381, "steps": 20}
---

# 平台全量/😯Flux.1 fill+ACE+Redux+CN 主体置换到场景_替换人物_人物迁移_1931796829946445826.json

> 来源文件 `comfyui_library/workflows/平台全量/😯Flux.1 fill+ACE+Redux+CN 主体置换到场景_替换人物_人物迁移_1931796829946445826.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（180 个）：
- `PreviewImage`
- `EmptyImage`
- `easy imageConcat`
- `ImageToMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageCrop+`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `ControlNetApplyAdvanced` ★核心
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `RH_Translator`
- `SetNode`
- `easy seed`
- `SetNode`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `DifferentialDiffusion`
- `SetNode`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy imageConcat`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `GetNode`
- `LayerMask: MaskGrow`
- `Mask Fill Holes`
- `MaskToImage`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `InpaintModelConditioning`
- `RepeatLatentBatch`
- `RebatchLatents`
- `BasicGuider`
- `FluxGuidance`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ShowText|pysssss`
- `DWPreprocessor`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `easy imageConcat`
- `EmptyImage`
- `easy imageConcat`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ReduxAdvanced`
- `ReduxAdvanced`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BiRefNetRMBG`
- `SetNode`
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `InstantIDModelLoader`
- `DifferentialDiffusion`
- `ApplyInstantID`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `LayerMask: MaskPreview`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `InpaintModelConditioning`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `KSampler` ★核心
- `InpaintStitchImproved`
- `InpaintCropImproved`
- `InpaintCropImproved`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `SaveImage`
- `SaveImage`

## 关键参数

- `controlnet_strength` = `0.8000000000000002`
- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `seed` = `473412735909381`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **46%**（82/180）

**有卡**：`EmptyImage`、`easy imageConcat`、`ImageToMask`、`ImageCrop+`、`SetUnionControlNetType`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetApplyAdvanced`、`LoadImage`、`CR Text Concatenate`、`RH_Translator`、`easy seed`、`RH_LLMAPI_NODE`、`LoraLoaderModelOnly`、`TeaCache`、`DifferentialDiffusion`、`UNETLoader`、`LayerUtility: CropByMask V2`、`LayerMask: MaskPreview`、`LayerMask: SegmentAnythingUltra V2`、`LayerMask: MaskGrow`、`Mask Fill Holes`、`MaskToImage`、`RandomNoise`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`InpaintModelConditioning`、`RepeatLatentBatch`、`RebatchLatents`、`BasicGuider`、`FluxGuidance`、`StyleModelLoader`、`CLIPVisionLoader`、`KSamplerSelect`、`DWPreprocessor`、`LayerColor: Brightness & Contrast`、`AIO_Preprocessor`、`ReduxAdvanced`、`BiRefNetRMBG`、`InstantIDFaceAnalysis`、`ControlNetLoader`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`ApplyInstantID`、`CLIPTextEncode`、`easy cleanGpuUsed`、`LayerMask: PersonMaskUltra V2`、`KSampler`、`InpaintStitchImproved`、`InpaintCropImproved`、`DualCLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut
