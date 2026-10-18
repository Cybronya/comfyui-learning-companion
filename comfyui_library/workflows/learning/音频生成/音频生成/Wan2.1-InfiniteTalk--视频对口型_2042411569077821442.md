---
key: 音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json
name: Wan2.1-InfiniteTalk--视频对口型_2042411569077821442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json
hash: 7b30988fec179016
coverage: 0.660714
learned_at: 2026-10-18 02:28:45
nodes: [MarkdownNote, SetNode, SetNode, SetNode, SetNode, SetNode, DownloadAndLoadWav2VecModel, GetNode, GetNode, GetNode, GetNode, Note, GetImageSizeAndCount, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcatMulti, WanVideoSampler, MultiTalkWav2VecEmbeds, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, GetImageRangeFromBatch, WanVideoDecode, GetNode, GetNode, SimpleMath+, easy int, PreviewAny, WanVideoTextEncodeCached, INTConstant, INTConstant, ImageResizeKJv2, GetNode, WanVideoEncode, ImageBatchMulti, Note, SoundFlow_GetLength, ToInt, ReverseImageBatch, Display Int (rgthree), SetNode, MultiTalkModelLoader, WanVideoLoraSelect, WanVideoVAELoader, WanVideoModelLoader, CLIPVisionLoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, VHS_LoadVideo, LoadAudio, VHS_VideoCombine, GetNode, AudioSeparation, AudioCrop, SetNode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Wan2.1-InfiniteTalk--视频对口型_2042411569077821442.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `MultiTalkWav2VecEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `easy int`
- `PreviewAny`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoEncode`
- `ImageBatchMulti`
- `Note`
- `SoundFlow_GetLength`
- `ToInt`
- `ReverseImageBatch`
- `Display Int (rgthree)`
- `SetNode`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `VHS_LoadVideo`
- `LoadAudio`
- `VHS_VideoCombine`
- `GetNode`
- `AudioSeparation`
- `AudioCrop`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **66%**（37/56）

**有卡**：`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`ImageConcatMulti`、`WanVideoSampler`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`SimpleMath+`、`easy int`、`WanVideoTextEncodeCached`、`INTConstant`、`ImageResizeKJv2`、`WanVideoEncode`、`ImageBatchMulti`、`SoundFlow_GetLength`、`ToInt`、`ReverseImageBatch`、`Display Int (rgthree)`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`VHS_LoadVideo`、`LoadAudio`、`VHS_VideoCombine`、`AudioSeparation`、`AudioCrop`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader
