---
key: 数字人/数字人/ComfyUI_电商视频_整人物替换_Wan2.2_Animate_2081230895100547074.json
name: ComfyUI_电商视频_整人物替换_Wan2.2_Animate_2081230895100547074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ComfyUI_电商视频_整人物替换_Wan2.2_Animate_2081230895100547074.json
hash: fa3d1fcceb8234cc
coverage: 0.810345
learned_at: 2026-10-26 01:54:06
nodes: [PixelPerfectResolution, DownloadAndLoadSAM2Model, PreviewImage, MaskPreview, Note, MarkdownNote, ImageScale, DWPreprocessor, DWPreprocessor, GetVideoComponents, CLIPTextEncode, CLIPTextEncode, CLIPVisionEncode, MarkdownNote, Sam2Segmentation, GrowMask, DrawMaskOnImage, BlockifyMask, VAEDecode, TrimVideoLatent, ImageFromBatch, WanAnimateToVideo, CreateVideo, ImageBatch, KSampler, VAEDecode, TrimVideoLatent, ImageFromBatch, WanAnimateToVideo, CreateVideo, KSampler, ImageBatch, MarkdownNote, SaveVideo, TrimVideoLatent, VAEDecode, WanAnimateToVideo, ImageFromBatch, CreateVideo, KSampler, SaveVideo, LoraLoaderModelOnly, VAELoader, ModelSamplingSD3, CLIPVisionLoader, LoraLoaderModelOnly, UNETLoader, PrimitiveInt, PrimitiveInt, MarkdownNote, MarkdownNote, CLIPLoader, MarkdownNote, PointsEditor, SaveVideo, LoadVideo, LoadImage, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 360779201293613, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/ComfyUI_电商视频_整人物替换_Wan2.2_Animate_2081230895100547074.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ComfyUI_电商视频_整人物替换_Wan2.2_Animate_2081230895100547074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `PixelPerfectResolution`
- `DownloadAndLoadSAM2Model`
- `PreviewImage`
- `MaskPreview`
- `Note`
- `MarkdownNote`
- `ImageScale`
- `DWPreprocessor`
- `DWPreprocessor`
- `GetVideoComponents`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `MarkdownNote`
- `Sam2Segmentation`
- `GrowMask`
- `DrawMaskOnImage`
- `BlockifyMask`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `ImageFromBatch`
- `WanAnimateToVideo`
- `CreateVideo`
- `ImageBatch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `ImageFromBatch`
- `WanAnimateToVideo`
- `CreateVideo`
- `KSampler` ★核心
- `ImageBatch`
- `MarkdownNote`
- `SaveVideo`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `WanAnimateToVideo`
- `ImageFromBatch`
- `CreateVideo`
- `KSampler` ★核心
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `MarkdownNote`
- `PointsEditor`
- `SaveVideo`
- `LoadVideo`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `360779201293613`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（47/58）

**有卡**：`PixelPerfectResolution`、`DownloadAndLoadSAM2Model`、`MaskPreview`、`ImageScale`、`DWPreprocessor`、`GetVideoComponents`、`CLIPTextEncode`、`CLIPVisionEncode`、`Sam2Segmentation`、`GrowMask`、`DrawMaskOnImage`、`BlockifyMask`、`VAEDecode`、`TrimVideoLatent`、`ImageFromBatch`、`WanAnimateToVideo`、`CreateVideo`、`ImageBatch`、`KSampler`、`SaveVideo`、`LoraLoaderModelOnly`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionLoader`、`UNETLoader`、`CLIPLoader`、`PointsEditor`、`LoadVideo`、`LoadImage`

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
