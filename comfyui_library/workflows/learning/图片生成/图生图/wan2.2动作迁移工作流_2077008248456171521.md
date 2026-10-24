---
key: 图片生成/图生图/wan2.2动作迁移工作流_2077008248456171521.json
name: wan2.2动作迁移工作流_2077008248456171521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2动作迁移工作流_2077008248456171521.json
hash: 5d6abe518abbb634
coverage: 0.854545
learned_at: 2026-10-23 11:46:03
nodes: [DownloadAndLoadSAM2Model, PreviewImage, MaskPreview, MarkdownNote, PointsEditor, GetVideoComponents, CLIPVisionEncode, MarkdownNote, Sam2Segmentation, GrowMask, DrawMaskOnImage, BlockifyMask, VAEDecode, TrimVideoLatent, ImageFromBatch, WanAnimateToVideo, CreateVideo, ImageBatch, KSampler, VAEDecode, TrimVideoLatent, ImageFromBatch, WanAnimateToVideo, CreateVideo, KSampler, ImageBatch, SaveVideo, MarkdownNote, SaveVideo, TrimVideoLatent, VAEDecode, WanAnimateToVideo, ImageFromBatch, CreateVideo, KSampler, SaveVideo, LoraLoaderModelOnly, CLIPLoader, VAELoader, ModelSamplingSD3, CLIPVisionLoader, LoraLoaderModelOnly, UNETLoader, PrimitiveInt, PrimitiveInt, MarkdownNote, CLIPTextEncode, LoadImage, DWPreprocessor, DWPreprocessor, ImageScale, Note, PixelPerfectResolution, LoadVideo, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 45845332552465, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan2.2动作迁移工作流_2077008248456171521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2动作迁移工作流_2077008248456171521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `DownloadAndLoadSAM2Model`
- `PreviewImage`
- `MaskPreview`
- `MarkdownNote`
- `PointsEditor`
- `GetVideoComponents`
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
- `SaveVideo`
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
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `DWPreprocessor`
- `DWPreprocessor`
- `ImageScale`
- `Note`
- `PixelPerfectResolution`
- `LoadVideo`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `45845332552465`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（47/55）

**有卡**：`DownloadAndLoadSAM2Model`、`MaskPreview`、`PointsEditor`、`GetVideoComponents`、`CLIPVisionEncode`、`Sam2Segmentation`、`GrowMask`、`DrawMaskOnImage`、`BlockifyMask`、`VAEDecode`、`TrimVideoLatent`、`ImageFromBatch`、`WanAnimateToVideo`、`CreateVideo`、`ImageBatch`、`KSampler`、`SaveVideo`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionLoader`、`UNETLoader`、`CLIPTextEncode`、`LoadImage`、`DWPreprocessor`、`ImageScale`、`PixelPerfectResolution`、`LoadVideo`

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
