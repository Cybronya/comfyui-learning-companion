---
key: 图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2001999132841656322.json
name: sdxl+controlnet+instantid+放大人像写真工作流_2001999132841656322
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2001999132841656322.json
hash: 8a7c843f10aadd01
coverage: 0.790323
learned_at: 2026-10-23 11:44:53
nodes: [FaceBoundingBox, FaceAnalysisModels, MaskBlur+, GrowMask, LayerUtility: CropBoxResolve, ImageResize+, Reroute, InpaintModelConditioning, VAEDecode, ImageResize+, CropMask, CLIPTextEncode, InstantIDFaceAnalysis, RepeatLatentBatch, LayerMask: MaskPreview, KSampler, Image Comparer (rgthree), ApplyInstantID, CLIPTextEncode, LayerMask: PersonMaskUltra V2, LayerUtility: RestoreCropBox, LayerUtility: CropByMask V2, Reroute, ImageUpscaleWithModel, ImageScaleBy, ColorMatch, Reroute, UpscaleModelLoader, SaveImage, Reroute, Reroute, Note, CR Text, CR Text Concatenate, CLIPTextEncode, CLIPTextEncode, Image Comparer (rgthree), ShowText|pysssss, TextInputBasic, Note, easy imageSize, EmptyLatentImage, LoraLoader, KSampler, SaveImage, ControlNetApplySD3, Reroute, OpenposePreprocessor, CannyEdgePreprocessor, DepthAnythingPreprocessor, VAEDecode, SaveImage, CR Text, Image Comparer (rgthree), CheckpointLoaderSimple, PreviewImage, ControlNetLoader, CheckpointLoaderSimple, InstantIDModelLoader, ControlNetLoader, LoadImage, LoadImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 5, "checkpoint": "真境写真XL Apex _ 商业电商场景摄影真实写实大师_XL_V8.safetensors", "controlnet_strength": 0.7000000000000002, "denoise": 1, "height": 1024, "lora_name": "SDXL\\富士胶片怀旧感风格摄影_v1.0.safetensors", "sampler_name": "euler", "scheduler": "karras", "seed": 830497523509932, "steps": 20, "strength_clip": 1, "strength_model": 0.8, "width": 768}
---

# 图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2001999132841656322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/sdxl+controlnet+instantid+放大人像写真工作流_2001999132841656322.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `MaskBlur+`
- `GrowMask`
- `LayerUtility: CropBoxResolve`
- `ImageResize+`
- `Reroute`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `ImageResize+`
- `CropMask`
- `CLIPTextEncode` ★核心
- `InstantIDFaceAnalysis`
- `RepeatLatentBatch`
- `LayerMask: MaskPreview`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `ApplyInstantID`
- `CLIPTextEncode` ★核心
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: CropByMask V2`
- `Reroute`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `ColorMatch`
- `Reroute`
- `UpscaleModelLoader`
- `SaveImage`
- `Reroute`
- `Reroute`
- `Note`
- `CR Text`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `ShowText|pysssss`
- `TextInputBasic`
- `Note`
- `easy imageSize`
- `EmptyLatentImage` ★核心
- `LoraLoader` ★核心
- `KSampler` ★核心
- `SaveImage`
- `ControlNetApplySD3` ★核心
- `Reroute`
- `OpenposePreprocessor`
- `CannyEdgePreprocessor`
- `DepthAnythingPreprocessor`
- `VAEDecode` ★核心
- `SaveImage`
- `CR Text`
- `Image Comparer (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `InstantIDModelLoader`
- `ControlNetLoader`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `830497523509932`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `SDXL\富士胶片怀旧感风格摄影_v1.0.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `controlnet_strength` = `0.7000000000000002`
- `checkpoint` = `真境写真XL Apex _ 商业电商场景摄影真实写实大师_XL_V8.safetensors`

## 知识

覆盖率 **79%**（49/62）

**有卡**：`FaceBoundingBox`、`FaceAnalysisModels`、`MaskBlur+`、`GrowMask`、`LayerUtility: CropBoxResolve`、`ImageResize+`、`InpaintModelConditioning`、`VAEDecode`、`CropMask`、`CLIPTextEncode`、`InstantIDFaceAnalysis`、`RepeatLatentBatch`、`LayerMask: MaskPreview`、`KSampler`、`ApplyInstantID`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: RestoreCropBox`、`LayerUtility: CropByMask V2`、`ImageUpscaleWithModel`、`ImageScaleBy`、`ColorMatch`、`UpscaleModelLoader`、`SaveImage`、`CR Text`、`CR Text Concatenate`、`TextInputBasic`、`easy imageSize`、`EmptyLatentImage`、`LoraLoader`、`ControlNetApplySD3`、`OpenposePreprocessor`、`CannyEdgePreprocessor`、`DepthAnythingPreprocessor`、`CheckpointLoaderSimple`、`ControlNetLoader`、`InstantIDModelLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、OpenposePreprocessor
