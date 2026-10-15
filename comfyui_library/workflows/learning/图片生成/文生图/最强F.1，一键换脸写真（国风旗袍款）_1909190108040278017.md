---
key: 图片生成/文生图/最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017.json
name: 最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017.json
hash: e21736ce9c5cbd13
coverage: 0.72549
learned_at: 2026-10-15 22:28:52
nodes: [DifferentialDiffusion, UNETLoader, DualCLIPLoader, LoraLoader, VAELoader, LoraLoader, LoraLoader, Anything Everywhere3, CLIPTextEncode, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, VAEDecode, Reroute, Reroute, Reroute, Reroute, easy clearCacheAll, Note, FaceDetailer, Reroute, Reroute, UltimateSDUpscale, KSampler //Inspire, Image Comparer (rgthree), EmptyLatentImage, UpscaleModelLoader, UltralyticsDetectorProvider, PulidFluxEvaClipLoader, ImageResize+, PulidFluxInsightFaceLoader, SAMLoader, PulidFluxModelLoader, LoadImage, FaceAnalysisModels, ApplyPulidFlux, Text Concatenate, LoadImage, Reroute, PreviewImage, DeepTranslatorTextNode, DeepTranslatorTextNode, Joy_extra_options, Joy_caption_two_load, PreviewImage, FaceBoundingBox, easy clearCacheAll, ShowText|pysssss, Joy_caption_two_advanced, Fast Groups Bypasser (rgthree), SaveImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1360, "lora_name": "AWPortrait CN_1.0", "sampler_name": "euler", "scheduler": "simple", "seed": 958736835959547, "steps": 28, "strength_clip": 1, "strength_model": 0.5, "width": 1024}
---

# 图片生成/文生图/最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `VAELoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Anything Everywhere3`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy clearCacheAll`
- `Note`
- `FaceDetailer`
- `Reroute`
- `Reroute`
- `UltimateSDUpscale`
- `KSampler //Inspire` ★核心
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `UpscaleModelLoader`
- `UltralyticsDetectorProvider`
- `PulidFluxEvaClipLoader`
- `ImageResize+`
- `PulidFluxInsightFaceLoader`
- `SAMLoader`
- `PulidFluxModelLoader`
- `LoadImage`
- `FaceAnalysisModels`
- `ApplyPulidFlux`
- `Text Concatenate`
- `LoadImage`
- `Reroute`
- `PreviewImage`
- `DeepTranslatorTextNode`
- `DeepTranslatorTextNode`
- `Joy_extra_options`
- `Joy_caption_two_load`
- `PreviewImage`
- `FaceBoundingBox`
- `easy clearCacheAll`
- `ShowText|pysssss`
- `Joy_caption_two_advanced`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `AWPortrait CN_1.0`
- `strength_model` = `0.5`
- `strength_clip` = `1`
- `seed` = `958736835959547`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1360`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（37/51）

**有卡**：`DifferentialDiffusion`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`VAELoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`easy clearCacheAll`、`FaceDetailer`、`UltimateSDUpscale`、`KSampler //Inspire`、`EmptyLatentImage`、`UpscaleModelLoader`、`UltralyticsDetectorProvider`、`PulidFluxEvaClipLoader`、`ImageResize+`、`PulidFluxInsightFaceLoader`、`SAMLoader`、`PulidFluxModelLoader`、`LoadImage`、`FaceAnalysisModels`、`ApplyPulidFlux`、`Text Concatenate`、`DeepTranslatorTextNode`、`Joy_extra_options`、`Joy_caption_two_load`、`FaceBoundingBox`、`Joy_caption_two_advanced`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、FluxGuidance
