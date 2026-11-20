---
key: 平台全量/F.1 首饰项链万物迁移（小物件，保留原尺寸大小）_1913216109074444290.json
name: F.1 首饰项链万物迁移（小物件，保留原尺寸大小）_1913216109074444290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1 首饰项链万物迁移（小物件，保留原尺寸大小）_1913216109074444290.json
hash: c7a50023cee4da26
coverage: 0.68254
learned_at: 2026-11-14 00:24:01
nodes: [Joy_caption_load, CLIPTextEncode, Reroute, Joy_caption, CLIPTextEncode, ConditioningZeroOut, Reroute, Reroute, Reroute, Reroute, easy showAnything, StringFunction|pysssss, Reroute, Reroute, SolidMask, Reroute, Reroute, Reroute, easy clearCacheAll, easy cleanGpuUsed, ImageConcanate, ImageToMask, MaskToImage, MaskToImage, ImageConcanate, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, FluxGuidance, LayerUtility: ImageScaleByAspectRatio V2, easy imageInsetCrop, ReduxAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskPreview, KSampler, InpaintModelConditioning, GrowMaskWithBlur, InpaintCrop, Note, Fast Groups Bypasser (rgthree), LoadImage, InpaintStitch, Note, SaveImage, PreviewImage, VAELoader, UNETLoader, DualCLIPLoader, LoraLoader, Anything Everywhere3, DifferentialDiffusion, DeepTranslatorTextNode, Text Concatenate (JPS), StyleModelLoader, CLIPVisionLoader, ModelSamplingFlux, GetImageSize+, easy cleanGpuUsed, easy clearCacheAll, VAEDecode, LoadImage]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "comfyui_subject_lora16.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 204804804366626, "steps": 28, "strength_clip": 1, "strength_model": 1}
---

# 平台全量/F.1 首饰项链万物迁移（小物件，保留原尺寸大小）_1913216109074444290.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1 首饰项链万物迁移（小物件，保留原尺寸大小）_1913216109074444290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `Joy_caption_load`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Joy_caption`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `StringFunction|pysssss`
- `Reroute`
- `Reroute`
- `SolidMask`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `ImageToMask`
- `MaskToImage`
- `MaskToImage`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `FluxGuidance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageInsetCrop`
- `ReduxAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskPreview`
- `KSampler` ★核心
- `InpaintModelConditioning`
- `GrowMaskWithBlur`
- `InpaintCrop`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `InpaintStitch`
- `Note`
- `SaveImage`
- `PreviewImage`
- `VAELoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `Anything Everywhere3`
- `DifferentialDiffusion`
- `DeepTranslatorTextNode`
- `Text Concatenate (JPS)`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `ModelSamplingFlux`
- `GetImageSize+`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `204804804366626`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `comfyui_subject_lora16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **68%**（43/63）

**有卡**：`Joy_caption_load`、`CLIPTextEncode`、`Joy_caption`、`ConditioningZeroOut`、`StringFunction|pysssss`、`SolidMask`、`easy clearCacheAll`、`easy cleanGpuUsed`、`ImageConcanate`、`ImageToMask`、`MaskToImage`、`FluxGuidance`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageInsetCrop`、`ReduxAdvanced`、`LayerMask: MaskPreview`、`KSampler`、`InpaintModelConditioning`、`GrowMaskWithBlur`、`InpaintCrop`、`LoadImage`、`InpaintStitch`、`SaveImage`、`VAELoader`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`DifferentialDiffusion`、`DeepTranslatorTextNode`、`Text Concatenate (JPS)`、`StyleModelLoader`、`CLIPVisionLoader`、`ModelSamplingFlux`、`GetImageSize+`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
