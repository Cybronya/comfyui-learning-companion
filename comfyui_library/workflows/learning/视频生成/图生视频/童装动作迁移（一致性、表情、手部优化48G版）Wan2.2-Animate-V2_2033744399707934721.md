---
key: 视频生成/图生视频/童装动作迁移（一致性、表情、手部优化48G版）Wan2.2-Animate-V2_2033744399707934721.json
name: 童装动作迁移（一致性、表情、手部优化48G版）Wan2.2-Animate-V2_2033744399707934721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033744399707934721.json
hash: 14aa0b61f16e7a31
coverage: 0.636364
learned_at: 2026-10-15 22:35:41
nodes: [CLIPVisionLoader, SetNode, KSampler, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, TrimVideoLatent, GetNode, GetNode, KSampler, easy seed, GetNode, GetNode, VAEDecode, VAEDecode, TrimVideoLatent, VHS_GetImageCount, GetNode, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Int, CLIPLoader, CLIPVisionEncode, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, VHS_GetImageCount, GetNode, Int, Int, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, GetImageRangeFromBatch, UNETLoader, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, Float, ModelSamplingSD3, Note, SetNode, PathchSageAttentionKJ, SetNode, CM_IntToFloat, SimpleMath+, VHS_VideoInfoLoaded, SimpleMath+, SetNode, SetNode, GetImageRangeFromBatch, VHS_GetImageCount, SimpleMath+, LoraLoaderModelOnly, SetNode, GetNode, GetNode, LoraLoaderModelOnly, easy cleanGpuUsed, SetNode, PoseDetectionVitPoseToDWPose, Int, Int, OnnxDetectionModelLoader, SetNode, SetNode, PreviewImage, ImageResizeKJv2, ImageBatchMulti, GetImageRangeFromBatch, GetNode, GetNode, PoseDetectionVitPoseToDWPose, PoseAndFaceDetection, GetNode, GetNode, LoadImage, LoraLoaderModelOnly, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, VHS_LoadVideo, DownloadAndLoadNLFModel, SetNode, RenderNLFPoses, NLFPredict, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 850834747290907, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/童装动作迁移（一致性、表情、手部优化48G版）Wan2.2-Animate-V2_2033744399707934721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033744399707934721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `CLIPVisionLoader`
- `SetNode`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `easy seed`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VHS_GetImageCount`
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `CLIPLoader`
- `CLIPVisionEncode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_GetImageCount`
- `GetNode`
- `Int`
- `Int`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `GetImageRangeFromBatch`
- `UNETLoader` ★核心
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `Float`
- `ModelSamplingSD3`
- `Note`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `CM_IntToFloat`
- `SimpleMath+`
- `VHS_VideoInfoLoaded`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `VHS_GetImageCount`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `PoseDetectionVitPoseToDWPose`
- `Int`
- `Int`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageBatchMulti`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `DownloadAndLoadNLFModel`
- `SetNode`
- `RenderNLFPoses`
- `NLFPredict`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `850834747290907`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（63/99）

**有卡**：`CLIPVisionLoader`、`KSampler`、`TrimVideoLatent`、`easy seed`、`VAEDecode`、`VHS_GetImageCount`、`VHS_VideoCombine`、`Int`、`CLIPLoader`、`CLIPVisionEncode`、`WanAnimateToVideo`、`GetImageRangeFromBatch`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`Float`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CM_IntToFloat`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`PoseDetectionVitPoseToDWPose`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`ImageBatchMulti`、`PoseAndFaceDetection`、`LoadImage`、`ImageConcatMulti`、`VHS_LoadVideo`、`DownloadAndLoadNLFModel`、`RenderNLFPoses`、`NLFPredict`

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
