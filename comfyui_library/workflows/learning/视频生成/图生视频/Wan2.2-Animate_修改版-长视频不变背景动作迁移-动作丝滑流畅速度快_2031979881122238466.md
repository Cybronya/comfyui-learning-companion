---
key: 视频生成/图生视频/Wan2.2-Animate_修改版-长视频不变背景动作迁移-动作丝滑流畅速度快_2031979881122238466.json
name: Wan2.2-Animate_修改版-长视频不变背景动作迁移-动作丝滑流畅速度快_2031979881122238466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031979881122238466.json
hash: 300c1caeb9858ea1
coverage: 0.604651
learned_at: 2026-10-15 22:35:34
nodes: [CLIPVisionLoader, CLIPVisionLoader, SetNode, VAELoader, SetNode, SetNode, SetNode, KSampler, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, easy seed, VHS_VideoCombine, GetNode, GetNode, GetNode, GetImageRangeFromBatch, VAEDecode, GetImageRangeFromBatch, GetImageRangeFromBatch, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, ImageBatchMulti, VAEDecode, TrimVideoLatent, VHS_GetImageCount, VHS_GetImageCount, VHS_GetImageCount, SetNode, WanAnimateToVideo, CLIPVisionEncode, DWPreprocessor, WanAnimateToVideo, CLIPLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, VHS_VideoCombine, Int, Int, Int, CLIPTextEncode, VHS_VideoInfoLoaded, SetNode, SetNode, Int, Int, ImageResizeKJv2, CM_IntToFloat, SetNode, SetNode, SetNode, SimpleMath+, SetNode, SetNode, PreviewImage, SimpleMath+, WanAnimateToVideo, KSampler, TrimVideoLatent, VAEDecode, VHS_VideoCombine, CR Text, LoadImage, VHS_LoadVideo, VHS_VideoCombine, DWPreprocessor, PrimitiveInt, PrimitiveInt, SetNode, GetNode, SetNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 463163742290935, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Animate_修改版-长视频不变背景动作迁移-动作丝滑流畅速度快_2031979881122238466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031979881122238466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `easy seed`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VHS_GetImageCount`
- `VHS_GetImageCount`
- `VHS_GetImageCount`
- `SetNode`
- `WanAnimateToVideo`
- `CLIPVisionEncode`
- `DWPreprocessor`
- `WanAnimateToVideo`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Int`
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `CM_IntToFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SimpleMath+`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `SetNode`

## 关键参数

- `seed` = `463163742290935`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **60%**（52/86）

**有卡**：`CLIPVisionLoader`、`VAELoader`、`KSampler`、`TrimVideoLatent`、`easy seed`、`VHS_VideoCombine`、`GetImageRangeFromBatch`、`VAEDecode`、`ImageBatchMulti`、`VHS_GetImageCount`、`WanAnimateToVideo`、`CLIPVisionEncode`、`DWPreprocessor`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`Int`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`CM_IntToFloat`、`SimpleMath+`、`CR Text`、`LoadImage`、`VHS_LoadVideo`

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
