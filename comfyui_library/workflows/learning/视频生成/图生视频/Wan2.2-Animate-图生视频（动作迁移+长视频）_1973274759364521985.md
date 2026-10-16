---
key: 视频生成/图生视频/Wan2.2-Animate-图生视频（动作迁移+长视频）_1973274759364521985.json
name: Wan2.2-Animate-图生视频（动作迁移+长视频）_1973274759364521985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1973274759364521985.json
hash: c3102d82beba821a
coverage: 0.62069
learned_at: 2026-10-15 22:32:02
nodes: [CLIPVisionLoader, CLIPVisionLoader, SetNode, CLIPLoader, VAELoader, SetNode, ModelSamplingSD3, LoraLoaderModelOnly, UNETLoader, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, TrimVideoLatent, KSampler, CLIPVisionEncode, ImageResizeKJv2, SetNode, PreviewImage, SetNode, LoraLoaderModelOnly, CLIPTextEncode, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanAnimateToVideo, KSampler, TrimVideoLatent, GetNode, GetNode, VHS_VideoCombine, ImageBatchMulti, GetNode, GetNode, VHS_VideoCombine, Int, WanAnimateToVideo, KSampler, easy seed, LoadImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, WanAnimateToVideo, SimpleMath+, GetImageRangeFromBatch, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, Int, SetNode, CM_IntToFloat, Int, SetNode, SetNode, Int, VHS_VideoInfoLoaded, SimpleMath+, SetNode, SetNode, RHHiddenNodes, Int, Note, DWPreprocessor, VHS_LoadVideo, SetNode, DWPreprocessor, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, VHS_VideoCombine, PixelPerfectResolution]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 492300541326366, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Animate-图生视频（动作迁移+长视频）_1973274759364521985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1973274759364521985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `TrimVideoLatent`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
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
- `WanAnimateToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `easy seed`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `VAEDecode` ★核心
- `VHS_GetImageCount`
- `Int`
- `SetNode`
- `CM_IntToFloat`
- `Int`
- `SetNode`
- `SetNode`
- `Int`
- `VHS_VideoInfoLoaded`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `Int`
- `Note`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `SetNode`
- `DWPreprocessor`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `PixelPerfectResolution`

## 关键参数

- `seed` = `492300541326366`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（54/87）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`TrimVideoLatent`、`KSampler`、`CLIPVisionEncode`、`ImageResizeKJv2`、`WanAnimateToVideo`、`VHS_VideoCombine`、`ImageBatchMulti`、`Int`、`easy seed`、`LoadImage`、`SimpleMath+`、`GetImageRangeFromBatch`、`VAEDecode`、`VHS_GetImageCount`、`CM_IntToFloat`、`VHS_VideoInfoLoaded`、`RHHiddenNodes`、`DWPreprocessor`、`VHS_LoadVideo`、`PixelPerfectResolution`

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
