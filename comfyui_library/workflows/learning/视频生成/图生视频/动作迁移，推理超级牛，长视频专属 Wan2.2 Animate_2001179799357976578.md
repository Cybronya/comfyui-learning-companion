---
key: 视频生成/图生视频/动作迁移，推理超级牛，长视频专属 Wan2.2 Animate_2001179799357976578.json
name: 动作迁移，推理超级牛，长视频专属 Wan2.2 Animate_2001179799357976578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移，推理超级牛，长视频专属 Wan2.2 Animate_2001179799357976578.json
hash: 67c4989280854e62
coverage: 0.634146
learned_at: 2026-10-15 22:33:44
nodes: [CLIPVisionLoader, SetNode, CLIPLoader, VAELoader, SetNode, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, SetNode, SetNode, DWPreprocessor, SetNode, TrimVideoLatent, KSampler, CLIPVisionEncode, ImageResizeKJv2, SetNode, PreviewImage, SetNode, VHS_VideoCombine, DWPreprocessor, RHHiddenNodes, LoraLoaderModelOnly, TrimVideoLatent, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanAnimateToVideo, KSampler, TrimVideoLatent, GetNode, GetNode, VHS_VideoCombine, ImageBatchMulti, GetNode, VHS_VideoCombine, Int, WanAnimateToVideo, KSampler, LoadImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, WanAnimateToVideo, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, SetNode, CM_IntToFloat, Int, SetNode, SetNode, Int, VHS_LoadVideo, VHS_VideoInfoLoaded, SetNode, SetNode, Int, Int, SetNode, CLIPTextEncode, CLIPTextEncode, SimpleMath+, easy seed, Note, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1084029223902319, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/动作迁移，推理超级牛，长视频专属 Wan2.2 Animate_2001179799357976578.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001179799357976578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `CLIPVisionLoader`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `SetNode`
- `TrimVideoLatent`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `TrimVideoLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `SetNode`
- `CM_IntToFloat`
- `Int`
- `SetNode`
- `SetNode`
- `Int`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `easy seed`
- `Note`
- `LoadImage`

## 关键参数

- `seed` = `1084029223902319`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（52/82）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`DWPreprocessor`、`TrimVideoLatent`、`KSampler`、`CLIPVisionEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`RHHiddenNodes`、`WanAnimateToVideo`、`ImageBatchMulti`、`Int`、`LoadImage`、`SimpleMath+`、`GetImageRangeFromBatch`、`VAEDecode`、`VHS_GetImageCount`、`CM_IntToFloat`、`VHS_LoadVideo`、`VHS_VideoInfoLoaded`、`CLIPTextEncode`、`easy seed`

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
