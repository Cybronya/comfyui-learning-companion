---
key: 平台全量/😯Flux.1 redux+Ace+CN-换背景_参考背景-主体重绘光影版v1a_1948098496208470017.json
name: 😯Flux.1 redux+Ace+CN-换背景_参考背景-主体重绘光影版v1a_1948098496208470017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/😯Flux.1 redux+Ace+CN-换背景_参考背景-主体重绘光影版v1a_1948098496208470017.json
hash: e961883adf5fa6d5
coverage: 0.478431
learned_at: 2026-11-14 02:55:25
nodes: [PreviewImage, easy imageConcat, GetNode, GetNode, GetNode, RandomNoise, SetNode, VAEDecode, SetNode, TeaCache, ConditioningZeroOut, GetNode, SetNode, GetNode, SetNode, DifferentialDiffusion, BasicGuider, GetNode, GetNode, ModelSamplingFlux, GetNode, GetNode, easy cleanGpuUsed, GetNode, RH_Translator, easy textSwitch, SetNode, KSamplerSelect, UNETLoader, VAELoader, CLIPTextEncode, SetNode, easy seed, InpaintModelConditioning, GetNode, GetNode, SaveImage, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, easy imageConcat, easy imageConcat, CR Text Concatenate, SetNode, easy imageConcat, MaskToImage, ImageToMask, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, ImageCrop+, GetNode, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, ColorMatch, GetNode, SetNode, BiRefNetRMBG, PreviewImage, GetNode, GetNode, GetNode, GetNode, BasicGuider, CLIPVisionLoader, CLIPVisionEncode, StyleModelLoader, GetNode, BasicScheduler, GetNode, FluxGuidance, RandomNoise, GetNode, GetNode, GetNode, ControlNetLoader, GetNode, ControlNetApplySD3, StyleModelApply, ControlNetApplySD3, KSamplerSelect, SetNode, SetNode, GetNode, VAEDecode, DWPreprocessor, PreviewImage, SetNode, PreviewImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerColor: Brightness & Contrast, LayerUtility: ImageScaleByAspectRatio V2, EmptyImage, GetNode, easy imageConcat, SetNode, PreviewImage, GetNode, GetNode, EmptyImage, GetNode, SaveImage, GetNode, GetNode, GetNode, RH_LLMAPI_NODE, LayerMask: MaskGrow, SetNode, ImageSmartSharpen+, GetNode, ImageSmartSharpen+, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LayerMask: MaskPreview, SetNode, SetNode, LayerMask: MaskGrow, SetNode, LayerMask: MaskGrow, BiRefNetRMBG, LayerMask: MaskPreview, SetNode, LayerMask: MaskPreview, BackgroundScaler, SetNode, PreviewImage, SetNode, PreviewImage, StyleModelLoader, CLIPVisionLoader, GetNode, ColorMatch, ImageSmartSharpen+, GetNode, GetNode, SetNode, GetNode, BasicScheduler, FluxGuidance, RebatchLatents, RepeatLatentBatch, GetNode, SetUnionControlNetType, SetUnionControlNetType, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, GetNode, AIO_Preprocessor, SetNode, GetNode, SetNode, ControlNetApplySD3, SetUnionControlNetType, GetNode, LoadImage, ShowText|pysssss, SetNode, PreviewImage, INPAINT_MaskedFill, SetNode, PreviewImage, SetNode, GetNode, GetNode, ReduxAdvanced, ReduxAdvanced, LoadImage, SetNode, BiRefNetRMBG, LayerMask: MaskGrow, LayerMask: MaskGrow, RebatchLatents, SaveImage, SamplerCustomAdvanced, SaveImage, RH_LLMAPI_NODE, GetNode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, DualCLIPLoader, LoraLoaderModelOnly, TeaCache, LoraLoaderModelOnly, SetNode, GetNode, SetNode, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, SetNode, CheckpointLoaderSimple, InstantIDModelLoader, DifferentialDiffusion, ApplyInstantID, GetNode, GetNode, CLIPTextEncode, easy cleanGpuUsed, PreviewImage, SetNode, GetNode, SetNode, SetNode, PreviewImage, GetNode, PreviewImage, SetNode, LayerMask: MaskPreview, CLIPTextEncode, SetNode, GetNode, GetNode, VAEDecode, GetNode, InpaintModelConditioning, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, KSampler, InpaintStitchImproved, InpaintCropImproved, InpaintCropImproved, GetNode, GetNode, PreviewImage, GetNode, GetNode, EmptyLatentImage, SaveImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "controlnet_strength": 0.8000000000000002, "denoise": 0.5000000000000001, "height": 512, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 857641914504686, "steps": 20, "width": 16}
---

# 平台全量/😯Flux.1 redux+Ace+CN-换背景_参考背景-主体重绘光影版v1a_1948098496208470017.json

> 来源文件 `comfyui_library/workflows/平台全量/😯Flux.1 redux+Ace+CN-换背景_参考背景-主体重绘光影版v1a_1948098496208470017.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（255 个）：
- `PreviewImage`
- `easy imageConcat`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `TeaCache`
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `DifferentialDiffusion`
- `BasicGuider`
- `GetNode`
- `GetNode`
- `ModelSamplingFlux`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `RH_Translator`
- `easy textSwitch`
- `SetNode`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `easy seed`
- `InpaintModelConditioning`
- `GetNode`
- `GetNode`
- `SaveImage`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy imageConcat`
- `easy imageConcat`
- `CR Text Concatenate`
- `SetNode`
- `easy imageConcat`
- `MaskToImage`
- `ImageToMask`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCrop+`
- `GetNode`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ColorMatch`
- `GetNode`
- `SetNode`
- `BiRefNetRMBG`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `FluxGuidance`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `ControlNetLoader`
- `GetNode`
- `ControlNetApplySD3` ★核心
- `StyleModelApply`
- `ControlNetApplySD3` ★核心
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `DWPreprocessor`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyImage`
- `GetNode`
- `easy imageConcat`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `GetNode`
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `LayerMask: MaskGrow`
- `SetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `ImageSmartSharpen+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `SetNode`
- `LayerMask: MaskGrow`
- `SetNode`
- `LayerMask: MaskGrow`
- `BiRefNetRMBG`
- `LayerMask: MaskPreview`
- `SetNode`
- `LayerMask: MaskPreview`
- `BackgroundScaler`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `GetNode`
- `ColorMatch`
- `ImageSmartSharpen+`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `BasicScheduler`
- `FluxGuidance`
- `RebatchLatents`
- `RepeatLatentBatch`
- `GetNode`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `GetNode`
- `AIO_Preprocessor`
- `SetNode`
- `GetNode`
- `SetNode`
- `ControlNetApplySD3` ★核心
- `SetUnionControlNetType`
- `GetNode`
- `LoadImage`
- `ShowText|pysssss`
- `SetNode`
- `PreviewImage`
- `INPAINT_MaskedFill`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `ReduxAdvanced`
- `ReduxAdvanced`
- `LoadImage`
- `SetNode`
- `BiRefNetRMBG`
- `LayerMask: MaskGrow`
- `LayerMask: MaskGrow`
- `RebatchLatents`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `RH_LLMAPI_NODE`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
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
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `controlnet_strength` = `0.8000000000000002`
- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `seed` = `857641914504686`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.5000000000000001`
- `width` = `16`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **48%**（122/255）

**有卡**：`easy imageConcat`、`RandomNoise`、`VAEDecode`、`TeaCache`、`ConditioningZeroOut`、`DifferentialDiffusion`、`BasicGuider`、`ModelSamplingFlux`、`easy cleanGpuUsed`、`RH_Translator`、`easy textSwitch`、`KSamplerSelect`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`easy seed`、`InpaintModelConditioning`、`SaveImage`、`CR Text Concatenate`、`MaskToImage`、`ImageToMask`、`LayerMask: MaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCrop+`、`ColorMatch`、`BiRefNetRMBG`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelLoader`、`BasicScheduler`、`FluxGuidance`、`ControlNetLoader`、`ControlNetApplySD3`、`StyleModelApply`、`DWPreprocessor`、`LayerColor: Brightness & Contrast`、`EmptyImage`、`RH_LLMAPI_NODE`、`LayerMask: MaskGrow`、`ImageSmartSharpen+`、`SamplerCustomAdvanced`、`BackgroundScaler`、`RebatchLatents`、`RepeatLatentBatch`、`SetUnionControlNetType`、`AIO_Preprocessor`、`LoadImage`、`INPAINT_MaskedFill`、`ReduxAdvanced`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`InstantIDFaceAnalysis`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`ApplyInstantID`、`LayerMask: PersonMaskUltra V2`、`KSampler`、`InpaintStitchImproved`、`InpaintCropImproved`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut
