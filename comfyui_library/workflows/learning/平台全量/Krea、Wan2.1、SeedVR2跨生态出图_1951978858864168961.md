---
key: 平台全量/Krea、Wan2.1、SeedVR2跨生态出图_1951978858864168961.json
name: Krea、Wan2.1、SeedVR2跨生态出图_1951978858864168961
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Krea、Wan2.1、SeedVR2跨生态出图_1951978858864168961.json
hash: 98833ccae210774a
coverage: 0.729167
learned_at: 2026-11-14 00:36:33
nodes: [SetNode, PulidFluxEvaClipLoader, CLIPTextEncode, GetNode, FluxGuidance, ConditioningZeroOut, LayerUtility: PurgeVRAM, ImpactSwitch, ImpactSwitch, PreviewImage, DWPreprocessor, KSamplerSelect, EmptyLatentImage, GetNode, easy imagePixelPerfect, PathchSageAttentionKJ, CFGZeroStar, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ACN_AdvancedControlNetApply_v2, ApplyPulidFlux, SplitSigmas, ApplyPulidFlux, GetNode, CLIPTextEncode, SamplerCustom, SamplerCustom, easy seed, CLIPTextEncode, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, GetNode, PathchSageAttentionKJ, CFGZeroStar, PulidFluxModelLoader, PulidFluxInsightFaceLoader, PulidFluxOptions, ControlNetLoader, UNETLoader, UNETLoader, LoraLoaderModelOnly, Anything Everywhere3, VAELoader, CLIPLoader, RunningHub SeedXPro Translator, LoadImage, LoadImage, ShowText|pysssss, ShowText|pysssss, LoadImage, Image Comparer (rgthree), PreviewBridge, SeedVR2, SeedVR2BlockSwap, Note, Note, easy string, GLM_Vision_ImageToPrompt, Note, WanVaceToVideo, SimpleMath+, ImpactInt, ImpactMinMax, LayerUtility: ImageScaleByAspectRatio V2, RepeatImageBatch, DepthAnythingPreprocessor, DWPreprocessor, ImpactSwitch, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, Note, KSampler, TrimVideoLatent, VAEDecode, GetImageRangeFromBatch, LayerUtility: PurgeVRAM, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, LoadImage, SetNode, Note, UNETLoader, BasicScheduler, VAELoader, Anything Everywhere3, SetUnionControlNetType, SetUnionControlNetType, DepthAnythingV2Preprocessor, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, DualCLIPLoader, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 190309711577795, "steps": 6, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Krea、Wan2.1、SeedVR2跨生态出图_1951978858864168961.json

> 来源文件 `comfyui_library/workflows/平台全量/Krea、Wan2.1、SeedVR2跨生态出图_1951978858864168961.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
- `SetNode`
- `PulidFluxEvaClipLoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `FluxGuidance`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `ImpactSwitch`
- `ImpactSwitch`
- `PreviewImage`
- `DWPreprocessor`
- `KSamplerSelect` ★核心
- `EmptyLatentImage` ★核心
- `GetNode`
- `easy imagePixelPerfect`
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ACN_AdvancedControlNetApply_v2` ★核心
- `ApplyPulidFlux`
- `SplitSigmas`
- `ApplyPulidFlux`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `easy seed`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxOptions`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `VAELoader`
- `CLIPLoader`
- `RunningHub SeedXPro Translator`
- `LoadImage`
- `LoadImage`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewBridge`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `Note`
- `Note`
- `easy string`
- `GLM_Vision_ImageToPrompt`
- `Note`
- `WanVaceToVideo`
- `SimpleMath+`
- `ImpactInt`
- `ImpactMinMax`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatImageBatch`
- `DepthAnythingPreprocessor`
- `DWPreprocessor`
- `ImpactSwitch`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `SetNode`
- `Note`
- `UNETLoader` ★核心
- `BasicScheduler`
- `VAELoader`
- `Anything Everywhere3`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `DepthAnythingV2Preprocessor`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `1`
- `seed` = `190309711577795`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（70/96）

**有卡**：`PulidFluxEvaClipLoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM`、`DWPreprocessor`、`KSamplerSelect`、`EmptyLatentImage`、`easy imagePixelPerfect`、`PathchSageAttentionKJ`、`CFGZeroStar`、`LayerUtility: ImageScaleByAspectRatio V2`、`ACN_AdvancedControlNetApply_v2`、`ApplyPulidFlux`、`SplitSigmas`、`SamplerCustom`、`easy seed`、`ModelSamplingSD3`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`PulidFluxOptions`、`ControlNetLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`RunningHub SeedXPro Translator`、`LoadImage`、`PreviewBridge`、`SeedVR2`、`SeedVR2BlockSwap`、`easy string`、`GLM_Vision_ImageToPrompt`、`WanVaceToVideo`、`SimpleMath+`、`ImpactInt`、`ImpactMinMax`、`RepeatImageBatch`、`DepthAnythingPreprocessor`、`KSampler`、`TrimVideoLatent`、`VAEDecode`、`GetImageRangeFromBatch`、`BasicScheduler`、`SetUnionControlNetType`、`DepthAnythingV2Preprocessor`、`DualCLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
