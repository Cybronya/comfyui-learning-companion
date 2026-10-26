---
key: 数字人/数字人/AI还原“袁绍拔剑讨董”名场面！Wan2.2 Animate+InfiniteTalk+ComfyUI教程，含ComfyUI工作流_1972551620766724098.json
name: AI还原“袁绍拔剑讨董”名场面！Wan2.2 Animate+InfiniteTalk+ComfyUI教程，含ComfyUI工作流_1972551620766724098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI还原“袁绍拔剑讨董”名场面！Wan2.2 Animate+InfiniteTalk+ComfyUI教程，含ComfyUI工作流_1972551620766724098.json
hash: 0e19fa8f4b94758a
coverage: 0.429864
learned_at: 2026-10-26 01:53:49
nodes: [CLIPVisionLoader, LoraLoaderModelOnly, CLIPLoader, GetNode, GetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ModelSamplingSD3, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionEncode, SetNode, TrimVideoLatent, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, SetNode, SetNode, TrimVideoLatent, MarkdownNote, UNETLoader, KSampler, MarkdownNote, KSampler, WanAnimateToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CreateVideo, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, ImageFromBatch, VAEDecode, VAEDecode, WanAnimateToVideo, WanAnimateToVideo, ImageBatch, ImageBatch, SetNode, SetNode, SetNode, DownloadAndLoadWav2VecModel, WanVideoTorchCompileSettings, WanVideoVAELoader, CLIPVisionLoader, Bjornulf_ShowInt, AudioSeparation, WanVideoLoraSelect, PreviewAudio, WanVideoBlockSwap, MultiTalkModelLoader, WanVideoModelLoader, GetNode, WanVideoSampler, GetNode, Note, GetImageRangeFromBatch, GetImageSizeAndCount, WanVideoEncode, ImageFromBatch, SetNode, AudioCrop, Bjornulf_ShowInt, MultiTalkWav2VecEmbeds, LoraLoaderModelOnly, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoImageToVideoMultiTalk, WanVideoDecode, GetNode, GetNode, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CreateVideo, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CreateVideo, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CreateVideo, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SaveVideo, VAEDecode, GetNode, GetNode, CreateVideo, GetNode, TrimVideoLatent, ImageFromBatch, MarkdownNote, KSampler, ImageBatch, ImageBatch, ImageBatch, ImageBatch, ImageBatch, VAEDecode, VAEDecode, VAEDecode, VAEDecode, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, WanAnimateToVideo, VAEDecode, VHS_LoadVideo, Bjornulf_ShowInt, SetNode, VHS_LoadVideo, SetNode, SetNode, VHS_LoadVideo, LoadImage, VHS_LoadVideo, VHS_LoadVideo, CLIPTextEncode, WanVideoTextEncodeCached, GetImageRangeFromBatch, Fast Groups Bypasser (rgthree), Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 888, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/AI还原“袁绍拔剑讨董”名场面！Wan2.2 Animate+InfiniteTalk+ComfyUI教程，含ComfyUI工作流_1972551620766724098.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI还原“袁绍拔剑讨董”名场面！Wan2.2 Animate+InfiniteTalk+ComfyUI教程，含ComfyUI工作流_1972551620766724098.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（221 个）：
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
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
- `TrimVideoLatent`
- `MarkdownNote`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `WanAnimateToVideo`
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
- `ImageFromBatch`
- `SetNode`
- `AudioCrop`
- `Bjornulf_ShowInt`
- `MultiTalkWav2VecEmbeds`
- `LoraLoaderModelOnly` ★核心
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
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
- `CreateVideo`
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
- `GetNode`
- `GetNode`
- `CreateVideo`
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
- `GetNode`
- `GetNode`
- `CreateVideo`
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
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `ImageBatch`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `WanAnimateToVideo`
- `VAEDecode` ★核心
- `VHS_LoadVideo`
- `Bjornulf_ShowInt`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `WanVideoTextEncodeCached`
- `GetImageRangeFromBatch`
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

覆盖率 **43%**（95/221）

**有卡**：`CLIPVisionLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`CLIPVisionEncode`、`TrimVideoLatent`、`CLIPTextEncode`、`UNETLoader`、`KSampler`、`WanAnimateToVideo`、`ImageFromBatch`、`CreateVideo`、`VAEDecode`、`ImageBatch`、`DownloadAndLoadWav2VecModel`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`Bjornulf_ShowInt`、`AudioSeparation`、`WanVideoLoraSelect`、`PreviewAudio`、`WanVideoBlockSwap`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoSampler`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`WanVideoEncode`、`AudioCrop`、`MultiTalkWav2VecEmbeds`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoDecode`、`VHS_VideoCombine`、`SaveVideo`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncodeCached`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 8 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
