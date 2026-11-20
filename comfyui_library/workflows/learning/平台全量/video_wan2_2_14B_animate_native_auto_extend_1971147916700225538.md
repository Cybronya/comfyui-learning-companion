---
key: 平台全量/video_wan2_2_14B_animate_native_auto_extend_1971147916700225538.json
name: video_wan2_2_14B_animate_native_auto_extend_1971147916700225538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_wan2_2_14B_animate_native_auto_extend_1971147916700225538.json
hash: b66045d87610543c
coverage: 0.382609
learned_at: 2026-11-14 01:18:50
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, GrowMask, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecode, KSampler, GetNode, GetNode, GetNode, CLIPTextEncode, SetNode, SetNode, GetNode, MarkdownNote, TrimVideoLatent, SetNode, SetNode, PrimitiveInt, PrimitiveInt, CLIPLoader, VAELoader, SetNode, UNETLoader, PrimitiveInt, SetNode, TrimVideoLatent, GetNode, GetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageScale, PixelPerfectResolution, Note, SetNode, SetNode, CLIPVisionLoader, SetNode, LoadImage, SetNode, SetNode, GetNode, CLIPVisionEncode, MathExpression|pysssss, GetNode, GetNode, easy showAnything, SetNode, MarkdownNote, MarkdownNote, MarkdownNote, VHS_VideoCombine, VHS_VideoCombine, DrawMaskOnImage, DownloadAndLoadSAM2Model, Sam2Segmentation, SetNode, VHS_VideoCombine, VHS_VideoCombine, BlockifyMask, MaskToImage, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, GetNode, WanAnimateToVideo, WanAnimateToVideo, easy forLoopStart, GetNode, SetNode, GetNode, SetNode, SetNode, DWPreprocessor, DWPreprocessor, SetNode, GetNode, GetNode, ImageFromBatch, ImageBatch, GetNode, VAEDecode, VHS_VideoCombine, GetNode, easy forLoopEnd, GetNode, ImageFromBatch, VHS_LoadVideo, PointsEditor, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 387378783691198, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/video_wan2_2_14B_animate_native_auto_extend_1971147916700225538.json

> 来源文件 `comfyui_library/workflows/平台全量/video_wan2_2_14B_animate_native_auto_extend_1971147916700225538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（115 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GrowMask`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `TrimVideoLatent`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `SetNode`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `PixelPerfectResolution`
- `Note`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionEncode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `BlockifyMask`
- `MaskToImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `easy forLoopStart`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `DWPreprocessor`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `ImageBatch`
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `ImageFromBatch`
- `VHS_LoadVideo`
- `PointsEditor`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `387378783691198`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **38%**（44/115）

**有卡**：`LoraLoaderModelOnly`、`GrowMask`、`ModelSamplingSD3`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`TrimVideoLatent`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`VHS_VideoInfo`、`ImageScale`、`PixelPerfectResolution`、`CLIPVisionLoader`、`LoadImage`、`CLIPVisionEncode`、`MathExpression|pysssss`、`VHS_VideoCombine`、`DrawMaskOnImage`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`BlockifyMask`、`MaskToImage`、`WanAnimateToVideo`、`easy forLoopStart`、`DWPreprocessor`、`ImageFromBatch`、`ImageBatch`、`easy forLoopEnd`、`VHS_LoadVideo`、`PointsEditor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
