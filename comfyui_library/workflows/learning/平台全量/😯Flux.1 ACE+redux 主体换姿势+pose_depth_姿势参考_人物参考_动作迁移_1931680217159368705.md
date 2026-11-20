---
key: 平台全量/😯Flux.1 ACE+redux 主体换姿势+pose_depth_姿势参考_人物参考_动作迁移_1931680217159368705.json
name: 😯Flux.1 ACE+redux 主体换姿势+pose_depth_姿势参考_人物参考_动作迁移_1931680217159368705
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/😯Flux.1 ACE+redux 主体换姿势+pose_depth_姿势参考_人物参考_动作迁移_1931680217159368705.json
hash: e3782989b1cede81
coverage: 0.487705
learned_at: 2026-11-14 02:55:17
nodes: [StyleModelLoader, GetNode, GetNode, GetNode, GetNode, SetUnionControlNetType, GetNode, SetUnionControlNetType, CLIPVisionLoader, SetNode, PreviewImage, easy imageConcat, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, ImageCrop+, GetNode, GetNode, GetNode, GetNode, BasicGuider, RandomNoise, CLIPVisionLoader, CLIPVisionEncode, StyleModelLoader, GetNode, SetNode, VAEDecode, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, SetNode, CheckpointLoaderSimple, InstantIDModelLoader, DifferentialDiffusion, ApplyInstantID, GetNode, BasicScheduler, GetNode, SetNode, SetNode, GetNode, SetNode, ConditioningZeroOut, GetNode, GetNode, SetNode, GetNode, GetNode, DWPreprocessor, PreviewImage, SetNode, PreviewImage, AIO_Preprocessor, SetNode, SetNode, DifferentialDiffusion, SetNode, CLIPTextEncode, easy cleanGpuUsed, PreviewImage, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, SetNode, LayerUtility: CropByMask V2, PreviewImage, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, FluxGuidance, GetNode, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, GetNode, SetNode, GetNode, EmptyImage, BackgroundScaler, PreviewImage, SetNode, GetNode, ControlNetApplySD3, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: Brightness & Contrast, VAEEncode, BasicGuider, GetNode, GetNode, RebatchLatents, GetNode, GetNode, SetUnionControlNetType, GetNode, SetNode, ControlNetLoader, EmptyImage, GetNode, GetNode, GetNode, ControlNetApplySD3, RepeatLatentBatch, GetNode, VAEDecode, easy cleanGpuUsed, LayerMask: SegmentAnythingUltra, easy cleanGpuUsed, easy cleanGpuUsed, StyleModelApply, SetNode, GetNode, FluxGuidance, GetNode, CR Text Concatenate, SetNode, easy textSwitch, GetNode, GetNode, SetNode, SetNode, PreviewImage, GetNode, PreviewImage, SetNode, LayerMask: MaskPreview, SaveImage, SetNode, LoadImage, GetNode, BiRefNetRMBG, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, UNETLoader, VAELoader, CLIPTextEncode, GetNode, SetNode, PreviewImage, EmptyImage, easy seed, SetNode, ControlNetApplySD3, GetNode, ImageSmartSharpen+, GetNode, LayerUtility: ImageScaleByAspectRatio V2, InpaintModelConditioning, GetNode, GetNode, ShowText|pysssss, VAEDecode, GetNode, ReduxAdvanced, KSamplerSelect, RH_LLMAPI_NODE, GetNode, SamplerCustomAdvanced, SetNode, GetNode, GetNode, InpaintModelConditioning, SaveImage, ColorMatch, ImageSmartSharpen+, LayerMask: MaskPreview, LayerMask: MaskGrow, MaskToImage, LayerMask: MaskPreview, easy imageConcat, ImageToMask, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, GetNode, MaskToImage, Mask To Region, LayerMask: MaskPreview, GetNode, easy imageConcat, SetNode, PreviewImage, SetNode, LayerMask: PersonMaskUltra V2, LayerMask: MaskGrow, GetNode, GetNode, GetNode, GetNode, ImageBlend, easy imageConcat, easy imageConcat, GetNode, easy imageConcat, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, GetNode, BiRefNetRMBG, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_LLMAPI_NODE, GetNode, TeaCache, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, InpaintStitchImproved, InpaintCropImproved, InpaintCropImproved, DualCLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, BasicScheduler, SetNode, TeaCache, ModelSamplingFlux, GetNode, GetNode, SetNode, LoraLoaderModelOnly, GetNode, ImageSmartSharpen+, SaveImage, GetNode, SaveImage, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "controlnet_strength": 0.8000000000000002, "denoise": 0.5000000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 87398730312897, "steps": 20}
---

# 平台全量/😯Flux.1 ACE+redux 主体换姿势+pose_depth_姿势参考_人物参考_动作迁移_1931680217159368705.json

> 来源文件 `comfyui_library/workflows/平台全量/😯Flux.1 ACE+redux 主体换姿势+pose_depth_姿势参考_人物参考_动作迁移_1931680217159368705.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（244 个）：
- `StyleModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetUnionControlNetType`
- `GetNode`
- `SetUnionControlNetType`
- `CLIPVisionLoader`
- `SetNode`
- `PreviewImage`
- `easy imageConcat`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageCrop+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `RandomNoise`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
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
- `BasicScheduler`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `AIO_Preprocessor`
- `SetNode`
- `SetNode`
- `DifferentialDiffusion`
- `SetNode`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `FluxGuidance`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `EmptyImage`
- `BackgroundScaler`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `ControlNetApplySD3` ★核心
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: Brightness & Contrast`
- `VAEEncode` ★核心
- `BasicGuider`
- `GetNode`
- `GetNode`
- `RebatchLatents`
- `GetNode`
- `GetNode`
- `SetUnionControlNetType`
- `GetNode`
- `SetNode`
- `ControlNetLoader`
- `EmptyImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `ControlNetApplySD3` ★核心
- `RepeatLatentBatch`
- `GetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LayerMask: SegmentAnythingUltra`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `StyleModelApply`
- `SetNode`
- `GetNode`
- `FluxGuidance`
- `GetNode`
- `CR Text Concatenate`
- `SetNode`
- `easy textSwitch`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `LayerMask: MaskPreview`
- `SaveImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `BiRefNetRMBG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `PreviewImage`
- `EmptyImage`
- `easy seed`
- `SetNode`
- `ControlNetApplySD3` ★核心
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InpaintModelConditioning`
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `GetNode`
- `ReduxAdvanced`
- `KSamplerSelect` ★核心
- `RH_LLMAPI_NODE`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `InpaintModelConditioning`
- `SaveImage`
- `ColorMatch`
- `ImageSmartSharpen+`
- `LayerMask: MaskPreview`
- `LayerMask: MaskGrow`
- `MaskToImage`
- `LayerMask: MaskPreview`
- `easy imageConcat`
- `ImageToMask`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `MaskToImage`
- `Mask To Region`
- `LayerMask: MaskPreview`
- `GetNode`
- `easy imageConcat`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: MaskGrow`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBlend`
- `easy imageConcat`
- `easy imageConcat`
- `GetNode`
- `easy imageConcat`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `BiRefNetRMBG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `GetNode`
- `TeaCache`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `InpaintStitchImproved`
- `InpaintCropImproved`
- `InpaintCropImproved`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SetNode`
- `TeaCache`
- `ModelSamplingFlux`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `ImageSmartSharpen+`
- `SaveImage`
- `GetNode`
- `SaveImage`
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `controlnet_strength` = `0.8000000000000002`
- `seed` = `87398730312897`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **49%**（119/244）

**有卡**：`StyleModelLoader`、`SetUnionControlNetType`、`CLIPVisionLoader`、`easy imageConcat`、`ImageCrop+`、`BasicGuider`、`RandomNoise`、`CLIPVisionEncode`、`VAEDecode`、`InstantIDFaceAnalysis`、`ControlNetLoader`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`DifferentialDiffusion`、`ApplyInstantID`、`BasicScheduler`、`ConditioningZeroOut`、`DWPreprocessor`、`AIO_Preprocessor`、`CLIPTextEncode`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: CropByMask V2`、`FluxGuidance`、`SamplerCustomAdvanced`、`EmptyImage`、`BackgroundScaler`、`ControlNetApplySD3`、`LayerColor: Brightness & Contrast`、`VAEEncode`、`RebatchLatents`、`RepeatLatentBatch`、`LayerMask: SegmentAnythingUltra`、`StyleModelApply`、`CR Text Concatenate`、`easy textSwitch`、`LayerMask: MaskPreview`、`SaveImage`、`LoadImage`、`BiRefNetRMBG`、`UNETLoader`、`VAELoader`、`easy seed`、`ImageSmartSharpen+`、`InpaintModelConditioning`、`ReduxAdvanced`、`KSamplerSelect`、`RH_LLMAPI_NODE`、`ColorMatch`、`LayerMask: MaskGrow`、`MaskToImage`、`ImageToMask`、`LayerMask: PersonMaskUltra V2`、`Mask To Region`、`ImageBlend`、`TeaCache`、`LoraLoaderModelOnly`、`KSampler`、`InpaintStitchImproved`、`InpaintCropImproved`、`DualCLIPLoader`、`ModelSamplingFlux`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut
