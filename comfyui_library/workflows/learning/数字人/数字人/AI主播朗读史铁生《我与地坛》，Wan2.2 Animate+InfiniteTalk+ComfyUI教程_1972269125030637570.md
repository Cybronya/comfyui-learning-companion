---
key: 数字人/数字人/AI主播朗读史铁生《我与地坛》，Wan2.2 Animate+InfiniteTalk+ComfyUI教程_1972269125030637570.json
name: AI主播朗读史铁生《我与地坛》，Wan2.2 Animate+InfiniteTalk+ComfyUI教程_1972269125030637570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI主播朗读史铁生《我与地坛》，Wan2.2 Animate+InfiniteTalk+ComfyUI教程_1972269125030637570.json
hash: 5217ec97df4f0e09
coverage: 0.466667
learned_at: 2026-10-26 01:53:37
nodes: [CLIPVisionLoader, LoraLoaderModelOnly, CLIPLoader, SetNode, GetNode, GetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionEncode, SetNode, GetNode, GetNode, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, DWPreprocessor, ImageScale, TrimVideoLatent, Note, MarkdownNote, UNETLoader, KSampler, PrimitiveInt, PrimitiveInt, MarkdownNote, Bjornulf_ShowInt, KSampler, CLIPTextEncode, WanAnimateToVideo, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SaveVideo, VAEDecode, GetNode, GetNode, CreateVideo, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, ImageFromBatch, VAEDecode, VAEDecode, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, PixelPerfectResolution, Bjornulf_ShowInt, VAEDecode, ImageBatch, ImageBatch, ImageBatch, SetNode, SetNode, SetNode, DownloadAndLoadWav2VecModel, WanVideoTorchCompileSettings, WanVideoVAELoader, CLIPVisionLoader, Bjornulf_ShowInt, AudioSeparation, WanVideoLoraSelect, PreviewAudio, WanVideoBlockSwap, MultiTalkModelLoader, WanVideoModelLoader, GetNode, WanVideoSampler, GetNode, Note, GetImageRangeFromBatch, GetImageSizeAndCount, WanVideoEncode, SetNode, VHS_LoadVideo, ImageFromBatch, SetNode, AudioCrop, VHS_LoadVideo, Bjornulf_ShowInt, VHS_LoadVideo, MultiTalkWav2VecEmbeds, LoraLoaderModelOnly, WanVideoTextEncodeCached, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, WanVideoDecode, GetNode, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, DWPreprocessor, Fast Groups Bypasser (rgthree), Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 888, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/AI主播朗读史铁生《我与地坛》，Wan2.2 Animate+InfiniteTalk+ComfyUI教程_1972269125030637570.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI主播朗读史铁生《我与地坛》，Wan2.2 Animate+InfiniteTalk+ComfyUI教程_1972269125030637570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（150 个）：
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
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
- `GetNode`
- `GetNode`
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
- `SetNode`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `ImageScale`
- `TrimVideoLatent`
- `Note`
- `MarkdownNote`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `Bjornulf_ShowInt`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `WanAnimateToVideo`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `ImageFromBatch`
- `MarkdownNote`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveVideo`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `TrimVideoLatent`
- `ImageFromBatch`
- `MarkdownNote`
- `KSampler` ★核心
- `ImageFromBatch`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `PixelPerfectResolution`
- `Bjornulf_ShowInt`
- `VAEDecode` ★核心
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `SetNode`
- `SetNode`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `Bjornulf_ShowInt`
- `AudioSeparation`
- `WanVideoLoraSelect`
- `PreviewAudio`
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `Note`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `WanVideoEncode`
- `SetNode`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `SetNode`
- `AudioCrop`
- `VHS_LoadVideo`
- `Bjornulf_ShowInt`
- `VHS_LoadVideo`
- `MultiTalkWav2VecEmbeds`
- `LoraLoaderModelOnly` ★核心
- `WanVideoTextEncodeCached`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`

## 关键参数

- `seed` = `888`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **47%**（70/150）

**有卡**：`CLIPVisionLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionEncode`、`TrimVideoLatent`、`CLIPTextEncode`、`DWPreprocessor`、`ImageScale`、`UNETLoader`、`KSampler`、`Bjornulf_ShowInt`、`WanAnimateToVideo`、`LoadImage`、`ImageFromBatch`、`SaveVideo`、`VAEDecode`、`CreateVideo`、`PixelPerfectResolution`、`ImageBatch`、`DownloadAndLoadWav2VecModel`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`AudioSeparation`、`WanVideoLoraSelect`、`PreviewAudio`、`WanVideoBlockSwap`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoSampler`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`WanVideoEncode`、`VHS_LoadVideo`、`AudioCrop`、`MultiTalkWav2VecEmbeds`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoDecode`、`VHS_VideoCombine`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
