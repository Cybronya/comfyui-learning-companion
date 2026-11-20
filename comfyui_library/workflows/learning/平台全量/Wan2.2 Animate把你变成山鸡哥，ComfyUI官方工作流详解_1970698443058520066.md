---
key: 平台全量/Wan2.2 Animate把你变成山鸡哥，ComfyUI官方工作流详解_1970698443058520066.json
name: Wan2.2 Animate把你变成山鸡哥，ComfyUI官方工作流详解_1970698443058520066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate把你变成山鸡哥，ComfyUI官方工作流详解_1970698443058520066.json
hash: 6815697d5f145d08
coverage: 0.43956
learned_at: 2026-11-14 01:05:22
nodes: [CLIPVisionLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, Sam2Segmentation, GrowMask, SetNode, GetNode, GetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionEncode, SetNode, SaveVideo, VAEDecode, PixelPerfectResolution, GetNode, GetNode, DownloadAndLoadSAM2Model, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, DrawMaskOnImage, BlockifyMask, SetNode, SetNode, GetNode, GetNode, CreateVideo, GetNode, DWPreprocessor, DWPreprocessor, ImageScale, MarkdownNote, MarkdownNote, GetNode, GetNode, CreateVideo, VAEDecode, WanAnimateToVideo, ImageFromBatch, ImageBatch, TrimVideoLatent, ImageFromBatch, MarkdownNote, Note, MarkdownNote, LoadImage, UNETLoader, KSampler, PrimitiveInt, PrimitiveInt, CLIPTextEncode, MarkdownNote, Bjornulf_ShowInt, KSampler, SaveVideo, MaskPreview, PreviewImage, WanAnimateToVideo, VHS_LoadVideo, MarkdownNote, PointsEditor, Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 888, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2 Animate把你变成山鸡哥，ComfyUI官方工作流详解_1970698443058520066.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate把你变成山鸡哥，ComfyUI官方工作流详解_1970698443058520066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Sam2Segmentation`
- `GrowMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionEncode`
- `SetNode`
- `SaveVideo`
- `VAEDecode` ★核心
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `TrimVideoLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `DWPreprocessor`
- `DWPreprocessor`
- `ImageScale`
- `MarkdownNote`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `VAEDecode` ★核心
- `WanAnimateToVideo`
- `ImageFromBatch`
- `ImageBatch`
- `TrimVideoLatent`
- `ImageFromBatch`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `LoadImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `Bjornulf_ShowInt`
- `KSampler` ★核心
- `SaveVideo`
- `MaskPreview`
- `PreviewImage`
- `WanAnimateToVideo`
- `VHS_LoadVideo`
- `MarkdownNote`
- `PointsEditor`
- `Label (rgthree)`

## 关键参数

- `seed` = `888`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **44%**（40/91）

**有卡**：`CLIPVisionLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`Sam2Segmentation`、`GrowMask`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionEncode`、`SaveVideo`、`VAEDecode`、`PixelPerfectResolution`、`DownloadAndLoadSAM2Model`、`TrimVideoLatent`、`CLIPTextEncode`、`DrawMaskOnImage`、`BlockifyMask`、`CreateVideo`、`DWPreprocessor`、`ImageScale`、`WanAnimateToVideo`、`ImageFromBatch`、`ImageBatch`、`LoadImage`、`UNETLoader`、`KSampler`、`Bjornulf_ShowInt`、`MaskPreview`、`VHS_LoadVideo`、`PointsEditor`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
