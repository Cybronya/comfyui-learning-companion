---
key: 视频生成/图生视频/Infinite或者Infinite+IndexTTS2(单人)_1993149833712254977.json
name: Infinite或者Infinite+IndexTTS2(单人)_1993149833712254977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Infinite或者Infinite+IndexTTS2(单人)_1993149833712254977.json
hash: 8a4b3a5cdb153462
coverage: 0.610169
learned_at: 2026-10-15 22:33:17
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, PreviewAny, MultiTalkWav2VecEmbeds, Note, GetNode, ImageResizeKJv2, Note, DownloadAndLoadWav2VecModel, Wav2VecModelLoader, MarkdownNote, MarkdownNote, WanVideoSampler, MarkdownNote, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, LoadImage, MelBandRoFormerModelLoader, WanVideoVAELoader, MultiTalkModelLoader, PreviewAudio, MelBandRoFormerSampler, SetNode, AudioToFPS, easy showAnything, easy showAnything, SetNode, CR Text, WanVideoTextEncodeCached, GetImageSizeAndCount, GetNode, WanVideoClipVisionEncode, WanVideoImageToVideoMultiTalk, GetNode, Note, WanVideoPassImagesFromSamples, GetNode, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, IndexTTS2Run, SetNode, easy int, easy int, LoadAudio, LoadAudio, ImpactConditionalBranch, RunningHub Deepcleaner, PrimitiveBoolean, CR Text, CR Text, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Infinite或者Infinite+IndexTTS2(单人)_1993149833712254977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993149833712254977.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（59 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `MultiTalkWav2VecEmbeds`
- `Note`
- `GetNode`
- `ImageResizeKJv2`
- `Note`
- `DownloadAndLoadWav2VecModel`
- `Wav2VecModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `WanVideoVAELoader`
- `MultiTalkModelLoader`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `AudioToFPS`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `CR Text`
- `WanVideoTextEncodeCached`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoMultiTalk`
- `GetNode`
- `Note`
- `WanVideoPassImagesFromSamples`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `IndexTTS2Run`
- `SetNode`
- `easy int`
- `easy int`
- `LoadAudio`
- `LoadAudio`
- `ImpactConditionalBranch`
- `RunningHub Deepcleaner`
- `PrimitiveBoolean`
- `CR Text`
- `CR Text`
- `MarkdownNote`

## 知识

覆盖率 **61%**（36/59）

**有卡**：`MultiTalkWav2VecEmbeds`、`ImageResizeKJv2`、`DownloadAndLoadWav2VecModel`、`Wav2VecModelLoader`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`LoadImage`、`MelBandRoFormerModelLoader`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`PreviewAudio`、`MelBandRoFormerSampler`、`AudioToFPS`、`CR Text`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoPassImagesFromSamples`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`IndexTTS2Run`、`easy int`、`LoadAudio`、`ImpactConditionalBranch`、`RunningHub Deepcleaner`、`PrimitiveBoolean`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、CLIPVisionLoader
