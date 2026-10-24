---
key: 图片生成/图生图/flux_AI摄影人像换服装背景(参考图版)V3.2_1956598460248150017.json
name: flux_AI摄影人像换服装背景(参考图版)V3.2_1956598460248150017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux_AI摄影人像换服装背景(参考图版)V3.2_1956598460248150017.json
hash: b40670d4aebe3c04
coverage: 0.843373
learned_at: 2026-10-23 11:36:51
nodes: [ApplyPulidFlux, PulidFluxEvaClipLoader, ModelSamplingFlux, LoraLoaderModelOnly, BasicGuider, VAELoader, KSamplerSelect, BasicScheduler, RandomNoise, CLIPVisionEncode, CLIPVisionLoader, StyleModelApply, StyleModelLoader, Joy_caption_two, CR Text, Joy_caption_two_load, CLIPTextEncode, PulidFluxInsightFaceLoader, PulidFluxModelLoader, Florence2Run, Florence2ModelLoader, MaskToSEGS, SEGSPreview, CLIPTextEncode, AIO_Preprocessor, ConditioningZeroOut, LoraLoaderModelOnly, InstructPixToPixConditioning, ConditioningCombine, Reroute, PreviewTextNode, PreviewImage, UNETLoader, DualCLIPLoader, FluxGuidance, VAEDecode, EmptyLatentImage, ImageColorTransfer, PreviewImage, LayerColor: ColorAdapter, LoraLoaderModelOnly, StringFunction|pysssss, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, AIO_Preprocessor, ControlNetApplyAdvanced, ControlNetLoader, VAEDecode, InstantIDModelLoader, InstantIDFaceAnalysis, ControlNetLoader, ApplyInstantID, InpaintModelConditioning, RepeatLatentBatch, LayerMask: PersonMaskUltra V2, GrowMask, LayerUtility: CropByMask V2, LayerColor: ColorAdapter, ImageColorMatch+, ImageColorTransfer, Reroute, ImageResize+, LayerUtility: RestoreCropBox, MaskBlur+, LayerUtility: CropBoxResolve, PreviewImage, CropMask, Reroute, Reroute, Reroute, LoadImage, LoadImage, ImageResize+, PrimitiveFloat, PreviewImage, PreviewImage, SamplerCustomAdvanced, KSampler, LayerMask: MaskPreview, SaveImage, Image Comparer (rgthree), Note]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "controlnet_strength": 0.45, "denoise": 0.6, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 92332524608602, "steps": 15, "width": 1024}
---

# 图片生成/图生图/flux_AI摄影人像换服装背景(参考图版)V3.2_1956598460248150017.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux_AI摄影人像换服装背景(参考图版)V3.2_1956598460248150017.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `ApplyPulidFlux`
- `PulidFluxEvaClipLoader`
- `ModelSamplingFlux`
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `VAELoader`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `RandomNoise`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `StyleModelApply`
- `StyleModelLoader`
- `Joy_caption_two`
- `CR Text`
- `Joy_caption_two_load`
- `CLIPTextEncode` ★核心
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `Florence2Run`
- `Florence2ModelLoader`
- `MaskToSEGS`
- `SEGSPreview`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `InstructPixToPixConditioning`
- `ConditioningCombine`
- `Reroute`
- `PreviewTextNode`
- `PreviewImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `FluxGuidance`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `ImageColorTransfer`
- `PreviewImage`
- `LayerColor: ColorAdapter`
- `LoraLoaderModelOnly` ★核心
- `StringFunction|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `VAEDecode` ★核心
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `ApplyInstantID`
- `InpaintModelConditioning`
- `RepeatLatentBatch`
- `LayerMask: PersonMaskUltra V2`
- `GrowMask`
- `LayerUtility: CropByMask V2`
- `LayerColor: ColorAdapter`
- `ImageColorMatch+`
- `ImageColorTransfer`
- `Reroute`
- `ImageResize+`
- `LayerUtility: RestoreCropBox`
- `MaskBlur+`
- `LayerUtility: CropBoxResolve`
- `PreviewImage`
- `CropMask`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `ImageResize+`
- `PrimitiveFloat`
- `PreviewImage`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `KSampler` ★核心
- `LayerMask: MaskPreview`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`
- `controlnet_strength` = `0.45`
- `seed` = `92332524608602`
- `steps` = `15`
- `cfg` = `1.5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.6`

## 知识

覆盖率 **84%**（70/83）

**有卡**：`ApplyPulidFlux`、`PulidFluxEvaClipLoader`、`ModelSamplingFlux`、`LoraLoaderModelOnly`、`BasicGuider`、`VAELoader`、`KSamplerSelect`、`BasicScheduler`、`RandomNoise`、`CLIPVisionEncode`、`CLIPVisionLoader`、`StyleModelApply`、`StyleModelLoader`、`Joy_caption_two`、`CR Text`、`Joy_caption_two_load`、`CLIPTextEncode`、`PulidFluxInsightFaceLoader`、`PulidFluxModelLoader`、`Florence2Run`、`Florence2ModelLoader`、`MaskToSEGS`、`SEGSPreview`、`AIO_Preprocessor`、`ConditioningZeroOut`、`InstructPixToPixConditioning`、`ConditioningCombine`、`PreviewTextNode`、`UNETLoader`、`DualCLIPLoader`、`FluxGuidance`、`VAEDecode`、`EmptyLatentImage`、`ImageColorTransfer`、`LayerColor: ColorAdapter`、`StringFunction|pysssss`、`CheckpointLoaderSimple`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`InstantIDModelLoader`、`InstantIDFaceAnalysis`、`ApplyInstantID`、`InpaintModelConditioning`、`RepeatLatentBatch`、`LayerMask: PersonMaskUltra V2`、`GrowMask`、`LayerUtility: CropByMask V2`、`ImageColorMatch+`、`ImageResize+`、`LayerUtility: RestoreCropBox`、`MaskBlur+`、`LayerUtility: CropBoxResolve`、`CropMask`、`LoadImage`、`SamplerCustomAdvanced`、`KSampler`、`LayerMask: MaskPreview`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut
