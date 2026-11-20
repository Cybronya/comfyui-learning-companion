---
key: 数字人/数字人/【长时数字人口播】wanvideo_InfiniteTalk_2115534592798183426.json
name: 【长时数字人口播】wanvideo_InfiniteTalk_2115534592798183426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/【长时数字人口播】wanvideo_InfiniteTalk_2115534592798183426.json
hash: a1fd2d436f2e5909
coverage: 0.520833
learned_at: 2026-10-30 17:56:42
nodes: [MarkdownNote, WanVideoVAELoader, SetNode, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, GetNode, GetNode, WanVideoLoraSelect, WanVideoBlockSwap, INTConstant, INTConstant, WanVideoClipVisionEncode, GetNode, SetNode, PreviewAny, SetNode, MultiTalkWav2VecEmbeds, Note, WanVideoModelLoader, WanVideoTorchCompileSettings, GetNode, GetNode, GetImageSizeAndCount, GetNode, LoadImage, ImageResizeKJv2, Note, SetNode, LoadAudio, DownloadAndLoadWav2VecModel, Wav2VecModelLoader, MelBandRoFormerSampler, MarkdownNote, MarkdownNote, MelBandRoFormerModelLoader, MultiTalkModelLoader, GetNode, VHS_VideoCombine, WanVideoPassImagesFromSamples, WanVideoTextEncodeCached, INTConstant, WanVideoImageToVideoMultiTalk, WanVideoSampler, Note, Note]
patterns: []
missing: []
---

# 数字人/数字人/【长时数字人口播】wanvideo_InfiniteTalk_2115534592798183426.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/【长时数字人口播】wanvideo_InfiniteTalk_2115534592798183426.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
- `MarkdownNote`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `INTConstant`
- `INTConstant`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `Note`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `LoadImage`
- `ImageResizeKJv2`
- `Note`
- `SetNode`
- `LoadAudio`
- `DownloadAndLoadWav2VecModel`
- `Wav2VecModelLoader`
- `MelBandRoFormerSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MelBandRoFormerModelLoader`
- `MultiTalkModelLoader`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoPassImagesFromSamples`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoSampler` ★核心
- `Note`
- `Note`

## 知识

覆盖率 **52%**（25/48）

**有卡**：`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`INTConstant`、`WanVideoClipVisionEncode`、`MultiTalkWav2VecEmbeds`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`LoadImage`、`ImageResizeKJv2`、`LoadAudio`、`DownloadAndLoadWav2VecModel`、`Wav2VecModelLoader`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`MultiTalkModelLoader`、`VHS_VideoCombine`、`WanVideoPassImagesFromSamples`、`WanVideoTextEncodeCached`、`WanVideoImageToVideoMultiTalk`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
