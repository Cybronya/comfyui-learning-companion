---
key: 视频生成/图生视频/Wan2.2-Animate-图生视频 官方原版更稳定 人物替换SEC（精准换人）+长视频 稳如老狗_1983610116006191105.json
name: Wan2.2-Animate-图生视频 官方原版更稳定 人物替换SEC（精准换人）+长视频 稳如老狗_1983610116006191105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-图生视频 官方原版更稳定 人物替换SEC（精准换人）+长视频 稳如老狗_1983610116006191105.json
hash: febee8590a6c8031
coverage: 0.586538
learned_at: 2026-10-15 22:32:45
nodes: [CLIPVisionLoader, CLIPVisionLoader, SetNode, CLIPLoader, VAELoader, SetNode, LoraLoaderModelOnly, CLIPTextEncode, SetNode, SetNode, TrimVideoLatent, CLIPVisionEncode, CLIPTextEncode, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, TrimVideoLatent, GetNode, GetNode, GetNode, Int, CM_IntToFloat, SetNode, WanAnimateToVideo, KSampler, VHS_VideoCombine, WanAnimateToVideo, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, GetImageRangeFromBatch, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, VAEDecode, VHS_GetImageCount, GrowMask, Sam2Segmentation, GetNode, GetNode, GetNode, DWPreprocessor, VHS_VideoCombine, GetNode, GetNode, FaceMaskFromPoseKeypoints, SetNode, SetNode, GetNode, easy seed, GetNode, GetNode, GetNode, GetNode, DownloadAndLoadSAM2Model, SetNode, ModelSamplingSD3, LoraLoaderModelOnly, ImageBatchMulti, VHS_VideoCombine, GetNode, ImageResizeKJv2, ImageCropByMaskAndResize, PixelPerfectResolution, GetNode, SetNode, GetNode, VHS_VideoCombine, SetNode, DrawMaskOnImage, UNETLoader, BlockifyMask, SetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, SetNode, KSampler, VHS_VideoCombine, WanAnimateToVideo, VHS_LoadVideo, Int, Note, LoadImage, VHS_VideoCombine, Int, Int, Int, PreviewImage, SetNode, SetNode, SetNode, PointsEditor, VHS_VideoCombine, PreviewImage, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 698788920950459, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2-Animate-图生视频 官方原版更稳定 人物替换SEC（精准换人）+长视频 稳如老狗_1983610116006191105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983610116006191105.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
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
- `CLIPTextEncode` ★核心
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
- `GetNode`
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
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `GetNode`
- `ImageResizeKJv2`
- `ImageCropByMaskAndResize`
- `PixelPerfectResolution`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `DrawMaskOnImage`
- `UNETLoader` ★核心
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
- `VHS_LoadVideo`
- `Int`
- `Note`
- `LoadImage`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `Int`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `PointsEditor`
- `VHS_VideoCombine`
- `PreviewImage`
- `RHHiddenNodes`

## 关键参数

- `seed` = `698788920950459`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（61/104）

**有卡**：`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`TrimVideoLatent`、`CLIPVisionEncode`、`KSampler`、`Int`、`CM_IntToFloat`、`WanAnimateToVideo`、`VHS_VideoCombine`、`SimpleMath+`、`GetImageRangeFromBatch`、`VAEDecode`、`VHS_GetImageCount`、`GrowMask`、`Sam2Segmentation`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`easy seed`、`DownloadAndLoadSAM2Model`、`ModelSamplingSD3`、`ImageBatchMulti`、`ImageResizeKJv2`、`ImageCropByMaskAndResize`、`PixelPerfectResolution`、`DrawMaskOnImage`、`UNETLoader`、`BlockifyMask`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`、`RHHiddenNodes`

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
