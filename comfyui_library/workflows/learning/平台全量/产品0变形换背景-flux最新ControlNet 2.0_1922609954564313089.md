---
key: 平台全量/产品0变形换背景-flux最新ControlNet 2.0_1922609954564313089.json
name: 产品0变形换背景-flux最新ControlNet 2.0_1922609954564313089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/产品0变形换背景-flux最新ControlNet 2.0_1922609954564313089.json
hash: 1cd805957517c758
coverage: 0.788732
learned_at: 2026-11-14 01:34:31
nodes: [VAELoader, PreviewImage, AIO_Preprocessor, ACN_AdvancedControlNetApplySingle_v2, ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, SetUnionControlNetType, DifferentialDiffusion, ControlNetLoader, LoadImage, ImageResizeKJ, easy cleanGpuUsed, Image Comparer (rgthree), CLIPTextEncode, PreviewImage, MaskToImage, InpaintModelConditioning, PreviewImage, DualCLIPLoader, ConditioningZeroOut, ModelSamplingFlux, SamplerCustomAdvanced, Note, BasicGuider, KSamplerSelect, BasicScheduler, ApplyFBCacheOnModel, LoadFluxIPAdapter, ApplyFluxIPAdapter, Note, PreviewImage, PreviewImage, SetUnionControlNetType, SetUnionControlNetType, AIO_Preprocessor, AIO_Preprocessor, LayerMask: ObjectDetectorFL2, SetUnionControlNetType, FluxGuidance, RandomNoise, GetImageSize+, UNETLoader, LoraLoaderModelOnly, Int, LoraLoaderModelOnly, Note, Note, VAEDecode, ImageConcanate, ImageConcanate, CR Text, ACN_AdvancedControlNetApplySingle_v2, DeepTranslatorTextNode, RH_Translator, Switch any [Crystools], ShowText|pysssss, PreviewImage, PreviewImage, PreviewImage, ShowText|pysssss, RH_Captioner, RH_Translator, GrowMaskWithBlur, ImageResizeKJ, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LoadImage, ACN_AdvancedControlNetApplySingle_v2, SaveImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.7500000000000001}
---

# 平台全量/产品0变形换背景-flux最新ControlNet 2.0_1922609954564313089.json

> 来源文件 `comfyui_library/workflows/平台全量/产品0变形换背景-flux最新ControlNet 2.0_1922609954564313089.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `VAELoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `AIO_Preprocessor`
- `SetUnionControlNetType`
- `DifferentialDiffusion`
- `ControlNetLoader`
- `LoadImage`
- `ImageResizeKJ`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `MaskToImage`
- `InpaintModelConditioning`
- `PreviewImage`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ApplyFBCacheOnModel`
- `LoadFluxIPAdapter`
- `ApplyFluxIPAdapter`
- `Note`
- `PreviewImage`
- `PreviewImage`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `LayerMask: ObjectDetectorFL2`
- `SetUnionControlNetType`
- `FluxGuidance`
- `RandomNoise`
- `GetImageSize+`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CR Text`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `DeepTranslatorTextNode`
- `RH_Translator`
- `Switch any [Crystools]`
- `ShowText|pysssss`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ShowText|pysssss`
- `RH_Captioner`
- `RH_Translator`
- `GrowMaskWithBlur`
- `ImageResizeKJ`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LoadImage`
- `ACN_AdvancedControlNetApplySingle_v2` ★核心
- `SaveImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `controlnet_strength` = `0.7500000000000001`

## 知识

覆盖率 **79%**（56/71）

**有卡**：`VAELoader`、`AIO_Preprocessor`、`ACN_AdvancedControlNetApplySingle_v2`、`SetUnionControlNetType`、`DifferentialDiffusion`、`ControlNetLoader`、`LoadImage`、`ImageResizeKJ`、`easy cleanGpuUsed`、`CLIPTextEncode`、`MaskToImage`、`InpaintModelConditioning`、`DualCLIPLoader`、`ConditioningZeroOut`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`ApplyFBCacheOnModel`、`LoadFluxIPAdapter`、`ApplyFluxIPAdapter`、`LayerMask: ObjectDetectorFL2`、`FluxGuidance`、`RandomNoise`、`GetImageSize+`、`UNETLoader`、`LoraLoaderModelOnly`、`Int`、`VAEDecode`、`ImageConcanate`、`CR Text`、`DeepTranslatorTextNode`、`RH_Translator`、`Switch any [Crystools]`、`RH_Captioner`、`GrowMaskWithBlur`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、ACN_AdvancedControlNetApplySingle_v2
