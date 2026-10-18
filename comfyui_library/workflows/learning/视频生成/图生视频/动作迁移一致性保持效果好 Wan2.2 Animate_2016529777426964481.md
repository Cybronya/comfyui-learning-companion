---
key: 视频生成/图生视频/动作迁移一致性保持效果好 Wan2.2 Animate_2016529777426964481.json
name: 动作迁移一致性保持效果好 Wan2.2 Animate_2016529777426964481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移一致性保持效果好 Wan2.2 Animate_2016529777426964481.json
hash: 71d7a9da5d810712
coverage: 0.6375
learned_at: 2026-10-15 22:34:43
nodes: [CLIPVisionLoader, SetNode, CLIPLoader, VAELoader, SetNode, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, SetNode, SetNode, DWPreprocessor, SetNode, TrimVideoLatent, KSampler, CLIPVisionEncode, ImageResizeKJv2, SetNode, PreviewImage, SetNode, VHS_VideoCombine, DWPreprocessor, RHHiddenNodes, LoraLoaderModelOnly, TrimVideoLatent, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanAnimateToVideo, KSampler, TrimVideoLatent, GetNode, GetNode, ImageBatchMulti, GetNode, VHS_VideoCombine, WanAnimateToVideo, KSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, WanAnimateToVideo, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, SetNode, CM_IntToFloat, SetNode, SetNode, VHS_VideoInfoLoaded, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, SimpleMath+, easy seed, Int, Int, Int, Int, Int, LoadImage, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1015822453010917, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/动作迁移一致性保持效果好 Wan2.2 Animate_2016529777426964481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016529777426964481.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
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
- `ImageBatchMulti`
- `GetNode`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `KSampler` ★核心
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
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `easy seed`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1015822453010917`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（51/80）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`DWPreprocessor`、`TrimVideoLatent`、`KSampler`、`CLIPVisionEncode`、`ImageResizeKJv2`、`VHS_VideoCombine`、`RHHiddenNodes`、`WanAnimateToVideo`、`ImageBatchMulti`、`SimpleMath+`、`GetImageRangeFromBatch`、`VAEDecode`、`VHS_GetImageCount`、`CM_IntToFloat`、`VHS_VideoInfoLoaded`、`CLIPTextEncode`、`easy seed`、`Int`、`LoadImage`、`VHS_LoadVideo`

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
