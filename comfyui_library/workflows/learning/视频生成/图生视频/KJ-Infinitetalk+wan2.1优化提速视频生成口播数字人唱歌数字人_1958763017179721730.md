---
key: 视频生成/图生视频/KJ-Infinitetalk+wan2.1优化提速视频生成口播数字人唱歌数字人_1958763017179721730.json
name: KJ-Infinitetalk+wan2.1优化提速视频生成口播数字人唱歌数字人_1958763017179721730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958763017179721730.json
hash: 8fc64a8079f6037f
coverage: 0.7
learned_at: 2026-10-15 22:31:23
nodes: [SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, WanVideoModelLoader, WanVideoTorchCompileSettings, GetImageSizeAndCount, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, Display Int (rgthree), MultiTalkWav2VecEmbeds, SoundFlow_GetLength, DownloadAndLoadWav2VecModel, WanVideoSampler, WanVideoBlockSwap, SetNode, CLIPVisionLoader, WanVideoLoraSelect, MarkdownNote, MultiTalkModelLoader, SimpleMath+, ToInt, AudioSeparation, easy int, SDVN Any Show, ImageResizeKJv2, GetImageRangeFromBatch, GetNode, WanVideoEncode, GetNode, GetImageRangeFromBatch, INTConstant, SetNode, SetNode, PreviewAny, Note, GetNode, SetNode, GetNode, GetNode, SetNode, INTConstant, ImageConcatMulti, WanVideoDecode, GetImageSizeAndCount, LoadAudio, WanVideoTextEncodeCached, VHS_LoadVideo, BatchThief, SDVN Any Show, GetImageSize, scale, VHS_VideoCombine, GetNode, VHS_VideoCombine, VHS_VideoCombine, AudioCrop]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ-Infinitetalk+wan2.1优化提速视频生成口播数字人唱歌数字人_1958763017179721730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958763017179721730.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（60 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `Display Int (rgthree)`
- `MultiTalkWav2VecEmbeds`
- `SoundFlow_GetLength`
- `DownloadAndLoadWav2VecModel`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoLoraSelect`
- `MarkdownNote`
- `MultiTalkModelLoader`
- `SimpleMath+`
- `ToInt`
- `AudioSeparation`
- `easy int`
- `SDVN Any Show`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `GetImageRangeFromBatch`
- `INTConstant`
- `SetNode`
- `SetNode`
- `PreviewAny`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `LoadAudio`
- `WanVideoTextEncodeCached`
- `VHS_LoadVideo`
- `BatchThief`
- `SDVN Any Show`
- `GetImageSize`
- `scale`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AudioCrop`

## 知识

覆盖率 **70%**（42/60）

**有卡**：`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`Display Int (rgthree)`、`MultiTalkWav2VecEmbeds`、`SoundFlow_GetLength`、`DownloadAndLoadWav2VecModel`、`WanVideoSampler`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`SimpleMath+`、`ToInt`、`AudioSeparation`、`easy int`、`SDVN Any Show`、`ImageResizeKJv2`、`GetImageRangeFromBatch`、`WanVideoEncode`、`INTConstant`、`ImageConcatMulti`、`WanVideoDecode`、`LoadAudio`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`BatchThief`、`GetImageSize`、`scale`、`AudioCrop`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader
