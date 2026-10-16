---
key: 视频生成/图生视频/Wan2.2-Animate-动作迁移-720p-15s视频_2004411811057336321.json
name: Wan2.2-Animate-动作迁移-720p-15s视频_2004411811057336321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2004411811057336321.json
hash: 1873c505da3599e7
coverage: 0.666667
learned_at: 2026-10-15 22:33:54
nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, UNETLoader, VAELoader, ModelSamplingSD3, CLIPTextEncode, PoseAndFaceDetection, CLIPLoader, VHS_VideoCombine, OnnxDetectionModelLoader, SetNode, SetNode, GetNode, VHS_LoadVideo, PoseDetectionOneToAllAnimation, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, LoadImage, INTConstant, SetNode, SetNode, SetNode, Note, Note, SetNode, ImageResizeKJv2, Note, SetNode, SimpleMath+, SimpleMath+, SetNode, SetNode, SimpleMath+, INTConstant, INTConstant, FloatConstant, INTConstant, INTConstant, PreviewImage, GetNode, GetNode, Seed Generator, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, GetNode, TrimVideoLatent, SimpleMath+, GetNode, VAEDecode, easy forLoopStart, GetNode, WanAnimateToVideo, KSampler, GetImageRangeFromBatch, easy forLoopEnd, LatentColorMatchSimple, WanAnimateToVideo, VAEDecode, ImageBatchExtendWithOverlap, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, KSampler]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 23443174598678, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Animate-动作迁移-720p-15s视频_2004411811057336321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004411811057336321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `PoseAndFaceDetection`
- `CLIPLoader`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `PoseDetectionOneToAllAnimation`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `SetNode`
- `ImageResizeKJv2`
- `Note`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `FloatConstant`
- `INTConstant`
- `INTConstant`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `Seed Generator`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `GetNode`
- `TrimVideoLatent`
- `SimpleMath+`
- `GetNode`
- `VAEDecode` ★核心
- `easy forLoopStart`
- `GetNode`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `GetImageRangeFromBatch`
- `easy forLoopEnd`
- `LatentColorMatchSimple`
- `WanAnimateToVideo`
- `VAEDecode` ★核心
- `ImageBatchExtendWithOverlap`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `KSampler` ★核心

## 关键参数

- `seed` = `23443174598678`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（46/69）

**有卡**：`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`UNETLoader`、`VAELoader`、`ModelSamplingSD3`、`PoseAndFaceDetection`、`CLIPLoader`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`VHS_LoadVideo`、`PoseDetectionOneToAllAnimation`、`LoraLoaderModelOnly`、`INTConstant`、`LoadImage`、`ImageResizeKJv2`、`SimpleMath+`、`FloatConstant`、`Seed Generator`、`TrimVideoLatent`、`VAEDecode`、`easy forLoopStart`、`WanAnimateToVideo`、`KSampler`、`GetImageRangeFromBatch`、`easy forLoopEnd`、`LatentColorMatchSimple`、`ImageBatchExtendWithOverlap`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
