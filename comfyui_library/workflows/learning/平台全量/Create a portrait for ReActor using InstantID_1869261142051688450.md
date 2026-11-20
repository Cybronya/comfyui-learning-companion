---
key: 平台全量/Create a portrait for ReActor using InstantID_1869261142051688450.json
name: Create a portrait for ReActor using InstantID_1869261142051688450
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Create a portrait for ReActor using InstantID_1869261142051688450.json
hash: 2088296787c80754
coverage: 0.897436
learned_at: 2026-11-14 00:23:01
nodes: [SelfAttentionGuidance, Reroute, Automatic CFG, ImpactSEGSOrderedFilter, CLIPTextEncode, ConditioningCombine, LoadImage, LoadImage, PreviewImage, PreviewImage, SEGSPreview, ImageListToImageBatch, ViewText, CheckpointLoaderSimple, CLIPTextEncode, InstantIDModelLoader, InstantIDFaceAnalysis, VAEDecode, RH_Captioner, UltralyticsDetectorProvider, SAMLoader, ImpactMakeImageList, LoadImage, LoadImage, LoadImage, ImpactSimpleDetectorSEGS, ControlNetLoader, EmptyLatentImage, ApplyInstantID, CLIPTextEncode, LoraLoader, LoraLoader, LoadImage, KSampler, PreviewImage, ReActorFaceSwap, SaveImage, ReActorFaceSwap, SaveImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "realismBYSTABLEYOGI_sdxlV2.safetensors", "denoise": 1, "height": 1024, "lora_name": "faces_v3.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 612037490910981, "steps": 20, "strength_clip": 0.8, "strength_model": 0.8, "width": 1024}
---

# 平台全量/Create a portrait for ReActor using InstantID_1869261142051688450.json

> 来源文件 `comfyui_library/workflows/平台全量/Create a portrait for ReActor using InstantID_1869261142051688450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `SelfAttentionGuidance`
- `Reroute`
- `Automatic CFG`
- `ImpactSEGSOrderedFilter`
- `CLIPTextEncode` ★核心
- `ConditioningCombine`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `SEGSPreview`
- `ImageListToImageBatch`
- `ViewText`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `VAEDecode` ★核心
- `RH_Captioner`
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `ImpactMakeImageList`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImpactSimpleDetectorSEGS`
- `ControlNetLoader`
- `EmptyLatentImage` ★核心
- `ApplyInstantID`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoadImage`
- `KSampler` ★核心
- `PreviewImage`
- `ReActorFaceSwap`
- `SaveImage`
- `ReActorFaceSwap`
- `SaveImage`

**识别到的模式**：text_to_image、lora

## 关键参数

- `checkpoint` = `realismBYSTABLEYOGI_sdxlV2.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `faces_v3.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `0.8`
- `seed` = `612037490910981`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`SelfAttentionGuidance`、`Automatic CFG`、`ImpactSEGSOrderedFilter`、`CLIPTextEncode`、`ConditioningCombine`、`LoadImage`、`SEGSPreview`、`ImageListToImageBatch`、`ViewText`、`CheckpointLoaderSimple`、`InstantIDModelLoader`、`InstantIDFaceAnalysis`、`VAEDecode`、`RH_Captioner`、`UltralyticsDetectorProvider`、`SAMLoader`、`ImpactMakeImageList`、`ImpactSimpleDetectorSEGS`、`ControlNetLoader`、`EmptyLatentImage`、`ApplyInstantID`、`LoraLoader`、`KSampler`、`ReActorFaceSwap`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetLoader、Automatic CFG
