---
key: 图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json
name: Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json
hash: fb09d2e6e6b1ffb9
coverage: 0.623529
learned_at: 2026-10-23 11:28:06
nodes: [CLIPVisionLoader, CLIPVisionLoader, SetNode, CLIPLoader, VAELoader, SetNode, CLIPTextEncode, SetNode, SetNode, KSampler, ImageResizeKJv2, SetNode, PreviewImage, SetNode, CLIPTextEncode, TrimVideoLatent, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanAnimateToVideo, KSampler, TrimVideoLatent, GetNode, GetNode, VHS_VideoCombine, Int, KSampler, easy seed, LoadImage, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, GetNode, WanAnimateToVideo, SimpleMath+, GetImageRangeFromBatch, VAEDecode, VAEDecode, Int, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfoLoaded, SimpleMath+, CM_IntToFloat, GetImageRangeFromBatch, GetImageRangeFromBatch, SetNode, GetNode, DWPreprocessor, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, GetNode, GetNode, ImageBatchMulti, VHS_VideoCombine, VAEDecode, TrimVideoLatent, VHS_GetImageCount, VHS_GetImageCount, VHS_GetImageCount, Int, Int, Int, LoraLoaderModelOnly, SetNode, WanAnimateToVideo, CLIPVisionEncode, UNETLoader, ModelSamplingSD3, RHHiddenNodes, LoraLoaderModelOnly, RHHiddenNodes, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 64854475981723, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2-Animate-图生视频 官方原版更稳定 动作迁移（不变背景）+长视频 稳如老狗_1983452230231760897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `KSampler` ★核心
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `CLIPTextEncode` ★核心
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
- `Int`
- `KSampler` ★核心
- `easy seed`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimateToVideo`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SimpleMath+`
- `CM_IntToFloat`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `DWPreprocessor`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VHS_GetImageCount`
- `VHS_GetImageCount`
- `VHS_GetImageCount`
- `Int`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `WanAnimateToVideo`
- `CLIPVisionEncode`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `64854475981723`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（53/85）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`ImageResizeKJv2`、`TrimVideoLatent`、`WanAnimateToVideo`、`VHS_VideoCombine`、`Int`、`easy seed`、`LoadImage`、`SimpleMath+`、`GetImageRangeFromBatch`、`VAEDecode`、`VHS_VideoInfoLoaded`、`CM_IntToFloat`、`DWPreprocessor`、`ImageBatchMulti`、`VHS_GetImageCount`、`LoraLoaderModelOnly`、`CLIPVisionEncode`、`UNETLoader`、`ModelSamplingSD3`、`RHHiddenNodes`、`VHS_LoadVideo`

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
