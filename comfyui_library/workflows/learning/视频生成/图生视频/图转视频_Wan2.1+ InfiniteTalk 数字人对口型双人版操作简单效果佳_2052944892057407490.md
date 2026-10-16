---
key: 视频生成/图生视频/图转视频_Wan2.1+ InfiniteTalk 数字人对口型双人版操作简单效果佳_2052944892057407490.json
name: 图转视频_Wan2.1+ InfiniteTalk 数字人对口型双人版操作简单效果佳_2052944892057407490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2052944892057407490.json
hash: aa24fa3cda512fe3
coverage: 0.588235
learned_at: 2026-10-15 22:37:34
nodes: [Reroute, Reroute, Reroute, WanVideoClipVisionEncode, Reroute, Reroute, WanVideoTorchCompileSettings, SetNode, Reroute, Reroute, Anything Everywhere, GetNode, Reroute, WanVideoLoraSelect, WanVideoLoraSelect, GetImageRangeFromBatch, SetNode, MultiTalkModelLoader, AudioCrop, MultiTalkWav2VecEmbeds, Note, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, easy int, easy showAnything, WanVideoBlockSwap, Reroute, PlaySound|pysssss, GetNode, SeparateMasks, WanVideoDecode, VHS_VideoCombine, Reroute, Reroute, WanVideoImageToVideoMultiTalk, WanVideoTextEncode, WanVideoSampler, Reroute, WanVideoLoraSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, AudioCrop, AudioCrop, Reroute, Reroute, AudioSeparation, Audio Duration (mtb), MathExpression|pysssss, PreviewAudio, MathExpression|pysssss, GetNode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, AudioSeparation, AudioSeparation, PreviewAudio, SetNode, MarkdownNote, LoadAudio, LoadAudio, LoadAudio, LayerMask: MaskPreview]
patterns: []
missing: []
---

# 视频生成/图生视频/图转视频_Wan2.1+ InfiniteTalk 数字人对口型双人版操作简单效果佳_2052944892057407490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052944892057407490.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（68 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoClipVisionEncode`
- `Reroute`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `Reroute`
- `Reroute`
- `Anything Everywhere`
- `GetNode`
- `Reroute`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetImageRangeFromBatch`
- `SetNode`
- `MultiTalkModelLoader`
- `AudioCrop`
- `MultiTalkWav2VecEmbeds`
- `Note`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `easy int`
- `easy showAnything`
- `WanVideoBlockSwap`
- `Reroute`
- `PlaySound|pysssss`
- `GetNode`
- `SeparateMasks`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `Reroute`
- `WanVideoLoraSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `AudioCrop`
- `AudioCrop`
- `Reroute`
- `Reroute`
- `AudioSeparation`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `PreviewAudio`
- `MathExpression|pysssss`
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `AudioSeparation`
- `AudioSeparation`
- `PreviewAudio`
- `SetNode`
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LayerMask: MaskPreview`

## 知识

覆盖率 **59%**（40/68）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`GetImageRangeFromBatch`、`MultiTalkModelLoader`、`AudioCrop`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`easy int`、`WanVideoBlockSwap`、`PlaySound|pysssss`、`SeparateMasks`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncode`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`AudioSeparation`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`PreviewAudio`、`LoadAudio`、`LayerMask: MaskPreview`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
