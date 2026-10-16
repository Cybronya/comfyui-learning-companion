---
key: 视频生成/图生视频/可用动作迁移（一致性、表情、手部、抖动）Wan2.2-Animate-V5_2064595503089807361.json
name: 可用动作迁移（一致性、表情、手部、抖动）Wan2.2-Animate-V5_2064595503089807361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064595503089807361.json
hash: b91bdb7ef67459c9
coverage: 0.640351
learned_at: 2026-10-15 22:39:26
nodes: [TrimVideoLatent, GetNode, GetNode, GetNode, KSampler, GetNode, easy seed, GetImageRangeFromBatch, VAEDecode, VAEDecode, GetNode, ImageBatchMulti, TrimVideoLatent, GetNode, GetNode, Display Int (rgthree), GetNode, TrimVideoLatent, CLIPVisionEncode, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, DrawViTPose, easy mathInt, BatchCount+, ImageBatch, SetNode, SetNode, SetNode, PoseAndFaceDetection, SetNode, SetNode, SetNode, CLIPLoader, CLIPVisionLoader, VAELoader, GetNode, KSampler, SetNode, SetNode, GetNode, GetNode, SimpleMath+, KSampler, GetNode, VHS_VideoCombine, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, VAEDecode, VHS_GetImageCount, Display Int (rgthree), VHS_GetImageCount, Display Int (rgthree), VHS_GetImageCount, Display Int (rgthree), ImageScale, SetNode, VHS_VideoInfoLoaded, SetNode, Display Int (rgthree), SimpleMath+, ImageFromBatch, SetNode, Display Int (rgthree), SetNode, GetNode, GetNode, CLIPVisionLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, GetNode, Int, ImageResizeKJv2, Int, Int, CM_IntToFloat, SetNode, SetNode, SetNode, easy float, RepeatImageBatch, BatchCount+, easy mathInt, easy mathInt, easy mathInt, easy mathInt, VHS_VideoCombine, GetNode, OnnxDetectionModelLoader, PreviewImage, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, VHS_VideoCombine, Int, Primitive integer [Crystools], SimpleMath+, Note, Note, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 184646195208153, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/可用动作迁移（一致性、表情、手部、抖动）Wan2.2-Animate-V5_2064595503089807361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064595503089807361.json`

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
- `BatchCount+`
- `ImageBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
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
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `Display Int (rgthree)`
- `VHS_GetImageCount`
- `Display Int (rgthree)`
- `VHS_GetImageCount`
- `Display Int (rgthree)`
- `ImageScale`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `Display Int (rgthree)`
- `SimpleMath+`
- `ImageFromBatch`
- `SetNode`
- `Display Int (rgthree)`
- `SetNode`
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
- `Int`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `CM_IntToFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy float`
- `RepeatImageBatch`
- `BatchCount+`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `VHS_VideoCombine`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `seed` = `184646195208153`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（73/114）

**有卡**：`TrimVideoLatent`、`KSampler`、`easy seed`、`GetImageRangeFromBatch`、`VAEDecode`、`ImageBatchMulti`、`Display Int (rgthree)`、`CLIPVisionEncode`、`CLIPTextEncode`、`DrawViTPose`、`easy mathInt`、`BatchCount+`、`ImageBatch`、`PoseAndFaceDetection`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`SimpleMath+`、`VHS_VideoCombine`、`WanAnimateToVideo`、`VHS_GetImageCount`、`ImageScale`、`VHS_VideoInfoLoaded`、`ImageFromBatch`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`Int`、`ImageResizeKJv2`、`CM_IntToFloat`、`easy float`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`Primitive integer [Crystools]`、`VHS_LoadVideo`、`LoadImage`

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
