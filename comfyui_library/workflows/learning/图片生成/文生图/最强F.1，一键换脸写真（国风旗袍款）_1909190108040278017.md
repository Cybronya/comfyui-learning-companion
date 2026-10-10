---
key: 最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017.json
name: 最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017.json
hash: e21736ce9c5cbd13
coverage: 0.627451
learned_at: 2026-10-10 20:59:50
nodes: [DifferentialDiffusion, UNETLoader, DualCLIPLoader, LoraLoader, VAELoader, LoraLoader, LoraLoader, Anything Everywhere3, CLIPTextEncode, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, VAEDecode, Reroute, Reroute, Reroute, Reroute, easy clearCacheAll, Note, FaceDetailer, Reroute, Reroute, UltimateSDUpscale, KSampler //Inspire, Image Comparer (rgthree), EmptyLatentImage, UpscaleModelLoader, UltralyticsDetectorProvider, PulidFluxEvaClipLoader, ImageResize+, PulidFluxInsightFaceLoader, SAMLoader, PulidFluxModelLoader, LoadImage, FaceAnalysisModels, ApplyPulidFlux, Text Concatenate, LoadImage, Reroute, PreviewImage, DeepTranslatorTextNode, DeepTranslatorTextNode, Joy_extra_options, Joy_caption_two_load, PreviewImage, FaceBoundingBox, easy clearCacheAll, ShowText|pysssss, Joy_caption_two_advanced, Fast Groups Bypasser (rgthree), SaveImage]
patterns: [lora]
missing: [Text Concatenate, easy clearCacheAll, easy clearCacheAll, KSampler //Inspire, ImageResize+]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1360, "lora_name": "AWPortrait CN_1.0", "sampler_name": "euler", "scheduler": "simple", "seed": 958736835959547, "steps": 28, "strength_clip": 1, "strength_model": 0.5, "width": 1024}
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 核心节点 `KSampler //Inspire` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 最强F.1，一键换脸写真（国风旗袍款）_1909190108040278017.json

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

覆盖率 **63%**（32/51）

**有卡**：`DifferentialDiffusion`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`VAELoader`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`FaceDetailer`、`UltimateSDUpscale`、`EmptyLatentImage`、`UpscaleModelLoader`、`UltralyticsDetectorProvider`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`SAMLoader`、`PulidFluxModelLoader`、`LoadImage`、`FaceAnalysisModels`、`ApplyPulidFlux`、`DeepTranslatorTextNode`、`Joy_extra_options`、`Joy_caption_two_load`、`FaceBoundingBox`、`Joy_caption_two_advanced`、`SaveImage`

**缺卡**（5）：`Text Concatenate`、`easy clearCacheAll`、`easy clearCacheAll`、`KSampler //Inspire`、`ImageResize+`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、FluxGuidance

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 核心节点 `KSampler //Inspire` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
