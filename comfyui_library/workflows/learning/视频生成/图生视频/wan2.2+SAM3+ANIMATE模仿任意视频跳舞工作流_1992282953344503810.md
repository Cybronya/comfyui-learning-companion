---
key: 视频生成/图生视频/wan2.2+SAM3+ANIMATE模仿任意视频跳舞工作流_1992282953344503810.json
name: wan2.2+SAM3+ANIMATE模仿任意视频跳舞工作流_1992282953344503810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992282953344503810.json
hash: 64c4691dbb3ac12f
coverage: 0.770833
learned_at: 2026-10-15 22:33:16
nodes: [Note, CLIPVisionEncode, MarkdownNote, MarkdownNote, ModelSamplingSD3, MarkdownNote, CLIPTextEncode, CLIPTextEncode, LoadSAM3Model, ImpactImageBatchToImageList, DrawMaskOnImage, DWPreprocessor, VHS_VideoInfoLoaded, WanAnimateToVideo, MarkdownNote, VAEDecode, GetImageRangeFromBatch, PreviewImage, PreviewImage, ACE_TextGoogleTranslate, RunningHub Deepcleaner, easy showAnything, MarkdownNote, MarkdownNote, CLIPLoader, VAELoader, CLIPVisionLoader, MaskListToMaskBatch, LoraLoaderModelOnly, easy int, PixelPerfectResolution, DWPreprocessor, LayerUtility: ImageScaleByAspectRatio V2, BlockifyMask, LayerMask: MaskGrow, PreviewImage, MaskPreview, MaskPreview, SAM3Segmentation, LoraLoaderModelOnly, UNETLoader, VHS_VideoCombine, KSampler, VHS_LoadVideo, easy int, SimpleMath+, CR Text, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 553822106743207, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.2+SAM3+ANIMATE模仿任意视频跳舞工作流_1992282953344503810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992282953344503810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `Note`
- `CLIPVisionEncode`
- `MarkdownNote`
- `MarkdownNote`
- `ModelSamplingSD3`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadSAM3Model`
- `ImpactImageBatchToImageList`
- `DrawMaskOnImage`
- `DWPreprocessor`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `MarkdownNote`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `PreviewImage`
- `PreviewImage`
- `ACE_TextGoogleTranslate`
- `RunningHub Deepcleaner`
- `easy showAnything`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `MaskListToMaskBatch`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BlockifyMask`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `MaskPreview`
- `MaskPreview`
- `SAM3Segmentation`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `VHS_LoadVideo`
- `easy int`
- `SimpleMath+`
- `CR Text`
- `LoadImage`

## 关键参数

- `seed` = `553822106743207`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **77%**（37/48）

**有卡**：`CLIPVisionEncode`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadSAM3Model`、`ImpactImageBatchToImageList`、`DrawMaskOnImage`、`DWPreprocessor`、`VHS_VideoInfoLoaded`、`WanAnimateToVideo`、`VAEDecode`、`GetImageRangeFromBatch`、`ACE_TextGoogleTranslate`、`RunningHub Deepcleaner`、`CLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`MaskListToMaskBatch`、`LoraLoaderModelOnly`、`easy int`、`PixelPerfectResolution`、`LayerUtility: ImageScaleByAspectRatio V2`、`BlockifyMask`、`LayerMask: MaskGrow`、`MaskPreview`、`SAM3Segmentation`、`UNETLoader`、`VHS_VideoCombine`、`KSampler`、`VHS_LoadVideo`、`SimpleMath+`、`CR Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
