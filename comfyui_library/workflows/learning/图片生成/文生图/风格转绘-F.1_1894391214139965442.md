---
key: 图片生成/文生图/风格转绘-F.1_1894391214139965442.json
name: 风格转绘-F.1_1894391214139965442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/风格转绘-F.1_1894391214139965442.json
hash: 3a14663dc2e9d85b
coverage: 0.883721
learned_at: 2026-10-15 22:29:08
nodes: [SetUnionControlNetType, ConditioningZeroOut, FluxGuidance, VAELoader, KSampler, ControlNetApplyAdvanced, KSampler, VAEEncode, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, FaceAnalysisModels, PreviewImage, preview_mask, PulidFluxModelLoader, CLIPTextEncode, Text Concatenate (JPS), Joy_caption_two, easy cleanGpuUsed, easy cleanGpuUsed, VAEDecode, VAEDecode, GrowMaskWithBlur, PreviewImage, FaceBoundingBox, easy cleanGpuUsed, ApplyPulidFlux, LatentUpscaleBy, LoadImage, OpenposePreprocessor, PreviewImage, PreviewImage, SaveImage, ShowText|pysssss, TextInput_, LayerMask: PersonMaskUltra V2, EmptyLatentImage, LoadImage, Joy_caption_two_load, DualCLIPLoader, ControlNetLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 2, "cfg": 1, "controlnet_strength": 0.75, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1035842958869884, "steps": 20, "width": 768}
---

# 图片生成/文生图/风格转绘-F.1_1894391214139965442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/风格转绘-F.1_1894391214139965442.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `SetUnionControlNetType`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAELoader`
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `FaceAnalysisModels`
- `PreviewImage`
- `preview_mask`
- `PulidFluxModelLoader`
- `CLIPTextEncode` ★核心
- `Text Concatenate (JPS)`
- `Joy_caption_two`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `GrowMaskWithBlur`
- `PreviewImage`
- `FaceBoundingBox`
- `easy cleanGpuUsed`
- `ApplyPulidFlux`
- `LatentUpscaleBy`
- `LoadImage`
- `OpenposePreprocessor`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `TextInput_`
- `LayerMask: PersonMaskUltra V2`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `Joy_caption_two_load`
- `DualCLIPLoader`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `1035842958869884`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.75`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `2`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`SetUnionControlNetType`、`ConditioningZeroOut`、`FluxGuidance`、`VAELoader`、`KSampler`、`ControlNetApplyAdvanced`、`VAEEncode`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`FaceAnalysisModels`、`preview_mask`、`PulidFluxModelLoader`、`CLIPTextEncode`、`Text Concatenate (JPS)`、`Joy_caption_two`、`easy cleanGpuUsed`、`VAEDecode`、`GrowMaskWithBlur`、`FaceBoundingBox`、`ApplyPulidFlux`、`LatentUpscaleBy`、`LoadImage`、`OpenposePreprocessor`、`SaveImage`、`TextInput_`、`LayerMask: PersonMaskUltra V2`、`EmptyLatentImage`、`Joy_caption_two_load`、`DualCLIPLoader`、`ControlNetLoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
