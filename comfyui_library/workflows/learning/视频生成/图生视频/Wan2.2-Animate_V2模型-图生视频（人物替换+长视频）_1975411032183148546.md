---
key: 视频生成/图生视频/Wan2.2-Animate_V2模型-图生视频（人物替换+长视频）_1975411032183148546.json
name: Wan2.2-Animate_V2模型-图生视频（人物替换+长视频）_1975411032183148546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975411032183148546.json
hash: 4f1837c1c13f0e37
coverage: 0.592233
learned_at: 2026-10-15 22:32:08
nodes: [CLIPVisionLoader, CLIPVisionLoader, SetNode, CLIPLoader, VAELoader, SetNode, LoraLoaderModelOnly, CLIPTextEncode, SetNode, SetNode, TrimVideoLatent, CLIPVisionEncode, SetNode, PreviewImage, Int, CLIPTextEncode, TrimVideoLatent, Int, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, TrimVideoLatent, GetNode, GetNode, GetNode, Int, Int, CM_IntToFloat, SetNode, WanAnimateToVideo, KSampler, VHS_VideoCombine, WanAnimateToVideo, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, GrowMask, SetNode, SetNode, Sam2Segmentation, GetNode, GetNode, GetNode, DWPreprocessor, VHS_VideoCombine, GetNode, GetNode, FaceMaskFromPoseKeypoints, SetNode, SetNode, GetNode, easy seed, GetNode, GetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, SetNode, ModelSamplingSD3, LoraLoaderModelOnly, RHHiddenNodes, VHS_VideoCombine, ImageResizeKJv2, ImageCropByMaskAndResize, PixelPerfectResolution, GetNode, SetNode, LoadImage, GetNode, VHS_VideoCombine, VHS_VideoCombine, PointsEditor, SetNode, DrawMaskOnImage, BlockifyMask, SetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, SetNode, KSampler, VHS_VideoCombine, WanAnimateToVideo, Int, Note, UNETLoader, VHS_VideoCombine, GetNode, ImageBatchMulti, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 668667784588014, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Animate_V2模型-图生视频（人物替换+长视频）_1975411032183148546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975411032183148546.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
- `CLIPVisionLoader`
- `CLIPVisionLoader`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `TrimVideoLatent`
- `CLIPVisionEncode`
- `SetNode`
- `PreviewImage`
- `Int`
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `Int`
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
- `GetNode`
- `Int`
- `Int`
- `CM_IntToFloat`
- `SetNode`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `VHS_VideoCombine`
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
- `GrowMask`
- `SetNode`
- `SetNode`
- `Sam2Segmentation`
- `GetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy seed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `GetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PointsEditor`
- `SetNode`
- `DrawMaskOnImage`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `Int`
- `Note`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `ImageBatchMulti`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `668667784588014`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（61/103）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`TrimVideoLatent`、`CLIPVisionEncode`、`Int`、`KSampler`、`CM_IntToFloat`、`WanAnimateToVideo`、`VHS_VideoCombine`、`SimpleMath+`、`GetImageRangeFromBatch`、`VAEDecode`、`VHS_GetImageCount`、`GrowMask`、`Sam2Segmentation`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`easy seed`、`DownloadAndLoadSAM2Model`、`ModelSamplingSD3`、`RHHiddenNodes`、`ImageResizeKJv2`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`LoadImage`、`PointsEditor`、`DrawMaskOnImage`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`UNETLoader`、`ImageBatchMulti`、`VHS_LoadVideo`

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
