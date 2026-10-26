---
key: 数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json
name: 一键数字人对口型 Multitalk all for free V1.0_1979010362202820609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json
hash: cd70ad558d042570
coverage: 0.574074
learned_at: 2026-10-26 02:00:02
nodes: [MarkdownNote, GetNode, SetNode, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, GetNode, WanVideoBlockSwap, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, SetNode, WanVideoTorchCompileSettings, GetNode, WanVideoDecode, GetImageRangeFromBatch, GetImageSizeAndCount, GetImageRangeFromBatch, GetImageSizeAndCount, Note, PreviewAny, SetNode, MultiTalkWav2VecEmbeds, SetNode, MelBandRoFormerSampler, MarkdownNote, MarkdownNote, WanVideoVAELoader, WanVideoEncode, ImageConcatMulti, WanVideoImageToVideoMultiTalk, VHS_VideoCombine, WanVideoLoraSelect, WanVideoModelLoader, Wav2VecModelLoader, DownloadAndLoadWav2VecModel, WanVideoSampler, MultiTalkModelLoader, MelBandRoFormerModelLoader, LoadAudio, WanVideoTextEncodeCached, Note, VHS_LoadVideo, INTConstant, INTConstant, INTConstant, ImageResizeKJv2, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/一键数字人对口型 Multitalk all for free V1.0_1979010362202820609.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（54 个）：
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `Note`
- `PreviewAny`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoVAELoader`
- `WanVideoEncode`
- `ImageConcatMulti`
- `WanVideoImageToVideoMultiTalk`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Wav2VecModelLoader`
- `DownloadAndLoadWav2VecModel`
- `WanVideoSampler` ★核心
- `MultiTalkModelLoader`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `WanVideoTextEncodeCached`
- `Note`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`

## 知识

覆盖率 **57%**（31/54）

**有卡**：`CLIPVisionLoader`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`MultiTalkWav2VecEmbeds`、`MelBandRoFormerSampler`、`WanVideoVAELoader`、`WanVideoEncode`、`ImageConcatMulti`、`WanVideoImageToVideoMultiTalk`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`Wav2VecModelLoader`、`DownloadAndLoadWav2VecModel`、`WanVideoSampler`、`MultiTalkModelLoader`、`MelBandRoFormerModelLoader`、`LoadAudio`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`INTConstant`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
