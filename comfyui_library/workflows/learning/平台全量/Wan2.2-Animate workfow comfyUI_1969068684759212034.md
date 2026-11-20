---
key: 平台全量/Wan2.2-Animate workfow comfyUI_1969068684759212034.json
name: Wan2.2-Animate workfow comfyUI_1969068684759212034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Animate workfow comfyUI_1969068684759212034.json
hash: 2c79af94d2b6a3be
coverage: 0.731707
learned_at: 2026-11-14 01:05:53
nodes: [SetNode, SetNode, INTConstant, INTConstant, ImageResizeKJv2, SaveVideo, VAEDecode, TrimVideoLatent, KSampler, CreateVideo, Reroute, DWPreprocessor, PixelPerfectResolution, ImageCropByMaskAndResize, SetNode, SetNode, SetNode, Sam2Segmentation, GrowMask, SetNode, GetNode, DrawMaskOnImage, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, BlockifyMask, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, LoadImage, VHS_LoadVideo, MarkdownNote, UNETLoader, CLIPLoader, DownloadAndLoadSAM2Model, FaceMaskFromPoseKeypoints, LoraLoaderModelOnly, VAELoader, PointsEditor, WanAnimateToVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 837775305187218, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-Animate workfow comfyUI_1969068684759212034.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Animate workfow comfyUI_1969068684759212034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `SaveVideo`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSampler` ★核心
- `CreateVideo`
- `Reroute`
- `DWPreprocessor`
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `SetNode`
- `SetNode`
- `SetNode`
- `Sam2Segmentation`
- `GrowMask`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `BlockifyMask`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `DownloadAndLoadSAM2Model`
- `FaceMaskFromPoseKeypoints`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PointsEditor`
- `WanAnimateToVideo`

## 关键参数

- `seed` = `837775305187218`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`INTConstant`、`ImageResizeKJv2`、`SaveVideo`、`VAEDecode`、`TrimVideoLatent`、`KSampler`、`CreateVideo`、`DWPreprocessor`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`Sam2Segmentation`、`GrowMask`、`DrawMaskOnImage`、`VHS_VideoCombine`、`BlockifyMask`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`、`VHS_LoadVideo`、`UNETLoader`、`CLIPLoader`、`DownloadAndLoadSAM2Model`、`FaceMaskFromPoseKeypoints`、`LoraLoaderModelOnly`、`VAELoader`、`PointsEditor`、`WanAnimateToVideo`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
