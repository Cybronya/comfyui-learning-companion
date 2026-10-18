---
key: 视频生成/图生视频/图转视频_Wan2.1+ InfiniteTalk 数字人对口型三人版多人版_2053305138537873409.json
name: 图转视频_Wan2.1+ InfiniteTalk 数字人对口型三人版多人版_2053305138537873409.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图转视频_Wan2.1+ InfiniteTalk 数字人对口型三人版多人版_2053305138537873409.json
hash: 2dde7a82190b65f2
coverage: 0.581081
learned_at: 2026-10-15 22:37:38
nodes: [Reroute, Reroute, Reroute, WanVideoClipVisionEncode, Reroute, Reroute, WanVideoTorchCompileSettings, SetNode, Reroute, Reroute, Anything Everywhere, GetNode, Reroute, WanVideoLoraSelect, WanVideoLoraSelect, GetImageRangeFromBatch, SetNode, MultiTalkModelLoader, AudioCrop, MultiTalkWav2VecEmbeds, Note, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelect, WanVideoModelLoader, easy showAnything, WanVideoBlockSwap, Reroute, PlaySound|pysssss, GetNode, SeparateMasks, WanVideoDecode, VHS_VideoCombine, Reroute, Reroute, WanVideoImageToVideoMultiTalk, WanVideoTextEncode, WanVideoSampler, Reroute, WanVideoLoraSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, AudioCrop, AudioCrop, Reroute, Reroute, AudioSeparation, Audio Duration (mtb), MathExpression|pysssss, PreviewAudio, MathExpression|pysssss, GetNode, MarkdownNote, AudioSeparation, PreviewAudio, SetNode, LoadAudio, LoadAudio, LoadAudio, AudioCrop, Reroute, MarkdownNote, MarkdownNote, AudioSeparation, Reroute, AudioSeparation, LoadAudio, MarkdownNote, MarkdownNote, LayerMask: MaskPreview, MarkdownNote, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/图转视频_Wan2.1+ InfiniteTalk 数字人对口型三人版多人版_2053305138537873409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053305138537873409.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（74 个）：
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
- `AudioSeparation`
- `PreviewAudio`
- `SetNode`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `AudioCrop`
- `Reroute`
- `MarkdownNote`
- `MarkdownNote`
- `AudioSeparation`
- `Reroute`
- `AudioSeparation`
- `LoadAudio`
- `MarkdownNote`
- `MarkdownNote`
- `LayerMask: MaskPreview`
- `MarkdownNote`
- `easy int`

## 知识

覆盖率 **58%**（43/74）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`GetImageRangeFromBatch`、`MultiTalkModelLoader`、`AudioCrop`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`PlaySound|pysssss`、`SeparateMasks`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoImageToVideoMultiTalk`、`WanVideoTextEncode`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`AudioSeparation`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`PreviewAudio`、`LoadAudio`、`LayerMask: MaskPreview`、`easy int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
