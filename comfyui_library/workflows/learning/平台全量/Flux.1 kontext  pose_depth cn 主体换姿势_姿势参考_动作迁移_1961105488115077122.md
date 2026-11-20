---
key: 平台全量/Flux.1 kontext  pose_depth cn 主体换姿势_姿势参考_动作迁移_1961105488115077122.json
name: Flux.1 kontext  pose_depth cn 主体换姿势_姿势参考_动作迁移_1961105488115077122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1 kontext  pose_depth cn 主体换姿势_姿势参考_动作迁移_1961105488115077122.json
hash: 216817511fb04763
coverage: 0.530201
learned_at: 2026-11-14 00:28:48
nodes: [CLIPTextEncode, GetNode, SetNode, BasicGuider, KSamplerSelect, RebatchLatents, GetNode, SetNode, InjectLatentNoise+, LatentPixelScale, RandomNoise, BasicGuider, GetNode, SamplerCustomAdvanced, VAEDecode, GetNode, SetNode, SetNode, GetImageSize, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, VAELoader, SetNode, KSamplerSelect, RandomNoise, AIO_Preprocessor, ModelPassThrough, SetNode, AIO_Preprocessor, GetNode, easy imageRemBg, GetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, FluxGuidance, SetNode, PreviewImage, easy cleanGpuUsed, GetNode, SetNode, InstantIDFaceAnalysis, ControlNetLoader, SetNode, SetNode, SetNode, CheckpointLoaderSimple, InstantIDModelLoader, DifferentialDiffusion, ApplyInstantID, GetNode, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, GetNode, VAEDecode, GetNode, InpaintModelConditioning, GetNode, GetNode, GetNode, SetNode, PreviewImage, SetNode, LayerMask: MaskPreview, ImageSmartSharpen+, LayerMask: PersonMaskUltra V2, GetNode, SetNode, PreviewImage, GetNode, SetNode, GetNode, ConditioningZeroOut, SetNode, SamplerCustomAdvanced, SetNode, GetNode, UpscaleModelLoader, InjectLatentNoise+, BasicGuider, GetNode, KSamplerSelect, GetNode, RandomNoise, BasicScheduler, SamplerCustomAdvanced, BasicScheduler, VAEEncode, BasicScheduler, LoraLoaderModelOnly, RepeatLatentBatch, easy seed, RH_LLMAPI_NODE, SaveImage, SaveImage, SaveImage, GetNode, GetNode, GetNode, GetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, RH_Translator, easy textSwitch, LoadImage, ShowText|pysssss, ttN concat, ImageBlend, PreviewImage, PreviewImage, SetNode, PreviewImage, PreviewImage, SetNode, RH_LLMAPI_NODE, GetNode, UNETLoader, LoraLoaderModelOnly, SetNode, DualCLIPLoader, InpaintStitchImproved, InpaintCropImproved, InpaintCropImproved, LayerMask: PersonMaskUltra V2, easy imageRemBg, EmptyLatentImage, GetNode, KSampler, SetNode, ReferenceLatent, GetNode, GetNode, SetUnionControlNetType, ControlNetLoader, PreviewImage, GetNode, ControlNetApplySD3]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "checkpoint": "realvisxlV50_v50Bakedvae.safetensors", "controlnet_strength": 1.6000000000000003, "denoise": 0.5000000000000001, "height": 512, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1066586958186744, "steps": 20, "width": 512}
---

# 平台全量/Flux.1 kontext  pose_depth cn 主体换姿势_姿势参考_动作迁移_1961105488115077122.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1 kontext  pose_depth cn 主体换姿势_姿势参考_动作迁移_1961105488115077122.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（149 个）：
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `RebatchLatents`
- `GetNode`
- `SetNode`
- `InjectLatentNoise+`
- `LatentPixelScale`
- `RandomNoise`
- `BasicGuider`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `AIO_Preprocessor`
- `ModelPassThrough`
- `SetNode`
- `AIO_Preprocessor`
- `GetNode`
- `easy imageRemBg`
- `GetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FluxGuidance`
- `SetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
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
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `InpaintModelConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `LayerMask: MaskPreview`
- `ImageSmartSharpen+`
- `LayerMask: PersonMaskUltra V2`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `UpscaleModelLoader`
- `InjectLatentNoise+`
- `BasicGuider`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `RandomNoise`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `VAEEncode` ★核心
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `RepeatLatentBatch`
- `easy seed`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_Translator`
- `easy textSwitch`
- `LoadImage`
- `ShowText|pysssss`
- `ttN concat`
- `ImageBlend`
- `PreviewImage`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `SetNode`
- `RH_LLMAPI_NODE`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `DualCLIPLoader`
- `InpaintStitchImproved`
- `InpaintCropImproved`
- `InpaintCropImproved`
- `LayerMask: PersonMaskUltra V2`
- `easy imageRemBg`
- `EmptyLatentImage` ★核心
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `ReferenceLatent`
- `GetNode`
- `GetNode`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `PreviewImage`
- `GetNode`
- `ControlNetApplySD3` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `checkpoint` = `realvisxlV50_v50Bakedvae.safetensors`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `1066586958186744`
- `steps` = `20`
- `cfg` = `1.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.5000000000000001`
- `controlnet_strength` = `1.6000000000000003`

## 知识

覆盖率 **53%**（79/149）

**有卡**：`CLIPTextEncode`、`BasicGuider`、`KSamplerSelect`、`RebatchLatents`、`InjectLatentNoise+`、`LatentPixelScale`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`GetImageSize`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`AIO_Preprocessor`、`ModelPassThrough`、`easy imageRemBg`、`FluxGuidance`、`easy cleanGpuUsed`、`InstantIDFaceAnalysis`、`ControlNetLoader`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`DifferentialDiffusion`、`ApplyInstantID`、`InpaintModelConditioning`、`LayerMask: MaskPreview`、`ImageSmartSharpen+`、`LayerMask: PersonMaskUltra V2`、`ConditioningZeroOut`、`UpscaleModelLoader`、`BasicScheduler`、`VAEEncode`、`LoraLoaderModelOnly`、`RepeatLatentBatch`、`easy seed`、`RH_LLMAPI_NODE`、`SaveImage`、`LoadImage`、`RH_Translator`、`easy textSwitch`、`ttN concat`、`ImageBlend`、`UNETLoader`、`DualCLIPLoader`、`InpaintStitchImproved`、`InpaintCropImproved`、`EmptyLatentImage`、`KSampler`、`ReferenceLatent`、`SetUnionControlNetType`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut
