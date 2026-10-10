---
key: 视频生成/文生视频/Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1963994200775737346.json
name: Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1963994200775737346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1963994200775737346.json
hash: afc7f0a22d568136
coverage: 0.62069
learned_at: 2026-10-10 22:58:39
nodes: [MarkdownNote, SetNode, SetNode, SetNode, SetNode, SetNode, AudioSeparation, DownloadAndLoadWav2VecModel, GetNode, GetNode, GetNode, GetNode, Note, GetImageSizeAndCount, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcatMulti, MultiTalkWav2VecEmbeds, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, WanVideoTorchCompileSettings, SetNode, GetImageRangeFromBatch, SetNode, WanVideoDecode, GetNode, GetNode, GetNode, ToInt, SoundFlow_GetLength, easy int, Display Int (rgthree), PreviewAny, INTConstant, ImageResizeKJv2, GetNode, WanVideoEncode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ReverseImageBatch, ImageBatchMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, Note, WanVideoSampler, SimpleMath+, LoadAudio, AudioCrop, VHS_LoadVideo, INTConstant, WanVideoTextEncodeCached]
patterns: []
missing: [Display Int (rgthree), SimpleMath+, easy int]
discoveries: [次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1963994200775737346.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Aiwood-改进版KJ-Infinitetalk视频对口型工作流_1963994200775737346.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（58 个）：
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `AudioSeparation`
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
- `MultiTalkWav2VecEmbeds`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ToInt`
- `SoundFlow_GetLength`
- `easy int`
- `Display Int (rgthree)`
- `PreviewAny`
- `INTConstant`
- `ImageResizeKJv2`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ReverseImageBatch`
- `ImageBatchMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `Note`
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `LoadAudio`
- `AudioCrop`
- `VHS_LoadVideo`
- `INTConstant`
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **62%**（36/58）

**有卡**：`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`ImageConcatMulti`、`MultiTalkWav2VecEmbeds`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`ToInt`、`SoundFlow_GetLength`、`INTConstant`、`ImageResizeKJv2`、`WanVideoEncode`、`VHS_VideoCombine`、`ReverseImageBatch`、`ImageBatchMulti`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSampler`、`LoadAudio`、`AudioCrop`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`

**缺卡**（3）：`Display Int (rgthree)`、`SimpleMath+`、`easy int`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader

## 学习发现

- 次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
