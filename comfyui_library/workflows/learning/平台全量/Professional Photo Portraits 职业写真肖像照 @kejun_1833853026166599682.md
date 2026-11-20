---
key: 平台全量/Professional Photo Portraits 职业写真肖像照 @kejun_1833853026166599682.json
name: Professional Photo Portraits 职业写真肖像照 @kejun_1833853026166599682
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Professional Photo Portraits 职业写真肖像照 @kejun_1833853026166599682.json
hash: 0ed7863f5e4f289e
coverage: 0.704545
learned_at: 2026-11-14 00:48:37
nodes: [ImpactSimpleDetectorSEGS, ImpactIsNotEmptySEGS, Primitive string [Crystools], Text Input Switch, ImageBatchMultiple+, FaceEmbedDistance, PreviewImage, ImpactSEGSClassify, IPAdapterAdvanced, Note, SAMLoader, Note, Note, Note, PulidEvaClipLoader, Note, StringFunction|pysssss, VAEDecode, Note, FaceBoundingBox, Note, Reroute, Note, Note, UltralyticsDetectorProvider, Note, PulidInsightFaceLoader, PulidModelLoader, FaceBoundingBox, Automatic CFG, ApplyPulidAdvanced, CheckpointLoaderSimple, KSampler, CLIPTextEncode, IPAdapterUnifiedLoader, FaceAnalysisModels, ImpactHFTransformersClassifierProvider, PreviewImage, FaceDetailer, EmptyLatentImage, CLIPTextEncode, Primitive string [Crystools], LoadImage, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 2, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "denoise": 1, "height": 1024, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 1075612738088384, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Professional Photo Portraits 职业写真肖像照 @kejun_1833853026166599682.json

> 来源文件 `comfyui_library/workflows/平台全量/Professional Photo Portraits 职业写真肖像照 @kejun_1833853026166599682.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `ImpactSimpleDetectorSEGS`
- `ImpactIsNotEmptySEGS`
- `Primitive string [Crystools]`
- `Text Input Switch`
- `ImageBatchMultiple+`
- `FaceEmbedDistance`
- `PreviewImage`
- `ImpactSEGSClassify`
- `IPAdapterAdvanced`
- `Note`
- `SAMLoader`
- `Note`
- `Note`
- `Note`
- `PulidEvaClipLoader`
- `Note`
- `StringFunction|pysssss`
- `VAEDecode` ★核心
- `Note`
- `FaceBoundingBox`
- `Note`
- `Reroute`
- `Note`
- `Note`
- `UltralyticsDetectorProvider`
- `Note`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `FaceBoundingBox`
- `Automatic CFG`
- `ApplyPulidAdvanced`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `IPAdapterUnifiedLoader`
- `FaceAnalysisModels`
- `ImpactHFTransformersClassifierProvider`
- `PreviewImage`
- `FaceDetailer`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `Primitive string [Crystools]`
- `LoadImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`
- `seed` = `1075612738088384`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（31/44）

**有卡**：`ImpactSimpleDetectorSEGS`、`ImpactIsNotEmptySEGS`、`Primitive string [Crystools]`、`Text Input Switch`、`ImageBatchMultiple+`、`FaceEmbedDistance`、`ImpactSEGSClassify`、`IPAdapterAdvanced`、`SAMLoader`、`PulidEvaClipLoader`、`StringFunction|pysssss`、`VAEDecode`、`FaceBoundingBox`、`UltralyticsDetectorProvider`、`PulidInsightFaceLoader`、`PulidModelLoader`、`Automatic CFG`、`ApplyPulidAdvanced`、`CheckpointLoaderSimple`、`KSampler`、`CLIPTextEncode`、`IPAdapterUnifiedLoader`、`FaceAnalysisModels`、`ImpactHFTransformersClassifierProvider`、`FaceDetailer`、`EmptyLatentImage`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、Automatic CFG、IPAdapterAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
