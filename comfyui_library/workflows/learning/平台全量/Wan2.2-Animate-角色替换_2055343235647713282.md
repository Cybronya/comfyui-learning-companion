---
key: 平台全量/Wan2.2-Animate-角色替换_2055343235647713282.json
name: Wan2.2-Animate-角色替换_2055343235647713282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Animate-角色替换_2055343235647713282.json
hash: e4fa5ff853212729
coverage: 0.974359
learned_at: 2026-11-14 01:05:56
nodes: [CLIPVisionLoader, VAELoader, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, FaceMaskFromPoseKeypoints, VHS_VideoCombine, INTConstant, CLIPTextEncode, CLIPTextEncode, DWPreprocessor, CLIPLoader, CLIPVisionLoader, CLIPVisionEncode, ModelSamplingSD3, TrimVideoLatent, PixelPerfectResolution, ShowAnything|Mie, DownloadAndLoadSAM2Model, KSampler, VAEDecode, VHS_VideoCombine, ImageConcatMulti, ImageResizeKJv2, INTConstant, ImageCropByMaskAndResize, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, WanAnimateToVideo, INTConstant, VantageWanBlockSwap, Fast Groups Bypasser (rgthree), PointsEditor]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 77, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-Animate-角色替换_2055343235647713282.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Animate-角色替换_2055343235647713282.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（39 个）：
- `CLIPVisionLoader`
- `VAELoader`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `VHS_VideoCombine`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `DWPreprocessor`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `PixelPerfectResolution`
- `ShowAnything|Mie`
- `DownloadAndLoadSAM2Model`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `INTConstant`
- `ImageCropByMaskAndResize`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `WanAnimateToVideo`
- `INTConstant`
- `VantageWanBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `PointsEditor`

## 关键参数

- `seed` = `77`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`CLIPVisionLoader`、`VAELoader`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`FaceMaskFromPoseKeypoints`、`VHS_VideoCombine`、`INTConstant`、`CLIPTextEncode`、`DWPreprocessor`、`CLIPLoader`、`CLIPVisionEncode`、`ModelSamplingSD3`、`TrimVideoLatent`、`PixelPerfectResolution`、`ShowAnything|Mie`、`DownloadAndLoadSAM2Model`、`KSampler`、`VAEDecode`、`ImageConcatMulti`、`ImageResizeKJv2`、`ImageCropByMaskAndResize`、`VHS_LoadVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`WanAnimateToVideo`、`VantageWanBlockSwap`、`PointsEditor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
