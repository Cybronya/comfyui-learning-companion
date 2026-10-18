---
key: 视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2031640030707458050.json
name: Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2031640030707458050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2031640030707458050.json
hash: fec1a856f22e8cfa
coverage: 0.640351
learned_at: 2026-10-15 22:35:32
nodes: [TrimVideoLatent, GetNode, GetNode, GetNode, KSampler, GetNode, easy seed, GetNode, GetImageRangeFromBatch, VAEDecode, VAEDecode, GetNode, ImageBatchMulti, TrimVideoLatent, GetNode, GetNode, Display Int (rgthree), GetNode, TrimVideoLatent, CLIPVisionEncode, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, DrawViTPose, easy mathInt, easy mathInt, easy mathInt, BatchCount+, ImageBatch, SetNode, SetNode, SetNode, Int, Note, PoseAndFaceDetection, Note, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, CLIPLoader, CLIPVisionLoader, VAELoader, GetNode, KSampler, SetNode, SetNode, GetNode, GetNode, SimpleMath+, KSampler, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, VHS_VideoCombine, VAEDecode, VHS_GetImageCount, Display Int (rgthree), VHS_GetImageCount, Display Int (rgthree), VHS_GetImageCount, Display Int (rgthree), ImageScale, Int, Int, Int, RepeatImageBatch, SimpleMath+, CM_IntToFloat, SetNode, SetNode, VHS_VideoInfoLoaded, SetNode, Display Int (rgthree), SetNode, SetNode, ImageResizeKJv2, PreviewImage, SetNode, SimpleMath+, BatchCount+, ImageFromBatch, easy mathInt, SetNode, Display Int (rgthree), easy float, SetNode, GetNode, OnnxDetectionModelLoader, GetNode, GetNode, CLIPVisionLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, GetNode, Primitive integer [Crystools], easy mathInt, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 925237404252599, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Animate-动作迁移 （长视频）表情+抖动+一致性+手部_2031640030707458050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031640030707458050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `easy seed`
- `GetNode`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `ImageBatchMulti`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `Display Int (rgthree)`
- `GetNode`
- `TrimVideoLatent`
- `CLIPVisionEncode`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `DrawViTPose`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `BatchCount+`
- `ImageBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `Note`
- `PoseAndFaceDetection`
- `Note`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `KSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `Display Int (rgthree)`
- `VHS_GetImageCount`
- `Display Int (rgthree)`
- `VHS_GetImageCount`
- `Display Int (rgthree)`
- `ImageScale`
- `Int`
- `Int`
- `Int`
- `RepeatImageBatch`
- `SimpleMath+`
- `CM_IntToFloat`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `Display Int (rgthree)`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `BatchCount+`
- `ImageFromBatch`
- `easy mathInt`
- `SetNode`
- `Display Int (rgthree)`
- `easy float`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `Primitive integer [Crystools]`
- `easy mathInt`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `seed` = `925237404252599`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（73/114）

**有卡**：`TrimVideoLatent`、`KSampler`、`easy seed`、`GetImageRangeFromBatch`、`VAEDecode`、`ImageBatchMulti`、`Display Int (rgthree)`、`CLIPVisionEncode`、`CLIPTextEncode`、`DrawViTPose`、`easy mathInt`、`BatchCount+`、`ImageBatch`、`Int`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`SimpleMath+`、`WanAnimateToVideo`、`VHS_GetImageCount`、`ImageScale`、`RepeatImageBatch`、`CM_IntToFloat`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`ImageFromBatch`、`easy float`、`OnnxDetectionModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`Primitive integer [Crystools]`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
