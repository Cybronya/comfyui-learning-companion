---
key: 数字人/数字人/wan2.1视频对口型（支持超长30秒）_2061334128561315841.json
name: wan2.1视频对口型（支持超长30秒）_2061334128561315841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wan2.1视频对口型（支持超长30秒）_2061334128561315841.json
hash: 5bcc90785db145f7
coverage: 0.589286
learned_at: 2026-10-26 01:59:24
nodes: [DownloadAndLoadWav2VecModel, GetNode, MultiTalkWav2VecEmbeds, GetNode, SetNode, PreviewAny, GetNode, AudioSeparation, SetNode, WanVideoImageToVideoMultiTalk, WanVideoClipVisionEncode, GetNode, SetNode, ImageResizeKJv2, GetImageSizeAndCount, GetNode, WanVideoEncode, GetNode, SetNode, WanVideoSampler, WanVideoTextEncodeCached, LayerUtility: PurgeVRAM, GetNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, ImageFromBatch+, Audio Duration (mtb), SetNode, GetImageRangeFromBatch, WanVideoDecode, SetNode, WanVideoVAELoader, LayerUtility: PurgeVRAM, CLIPVisionLoader, SetNode, GetNode, SimpleMath+, FloatConstant, PrimitiveInt, PrimitiveInt, JjkText, GetNode, AudioCrop, WanVideoModelLoader, WanVideoLoraSelect, MultiTalkModelLoader, VHS_LoadVideo, SimpleMath+, SetNode, PrimitiveString, WanVideoBlockSwap, Note, VHS_VideoCombine, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/wan2.1视频对口型（支持超长30秒）_2061334128561315841.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wan2.1视频对口型（支持超长30秒）_2061334128561315841.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（56 个）：
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `MultiTalkWav2VecEmbeds`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `GetNode`
- `AudioSeparation`
- `SetNode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoEncode`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SimpleMath+`
- `SimpleMath+`
- `ImageFromBatch+`
- `Audio Duration (mtb)`
- `SetNode`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `SetNode`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `FloatConstant`
- `PrimitiveInt`
- `PrimitiveInt`
- `JjkText`
- `GetNode`
- `AudioCrop`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `VHS_LoadVideo`
- `SimpleMath+`
- `SetNode`
- `PrimitiveString`
- `WanVideoBlockSwap`
- `Note`
- `VHS_VideoCombine`
- `LoadAudio`

## 知识

覆盖率 **59%**（33/56）

**有卡**：`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`WanVideoImageToVideoMultiTalk`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`ImageFromBatch+`、`Audio Duration (mtb)`、`GetImageRangeFromBatch`、`WanVideoDecode`、`WanVideoVAELoader`、`CLIPVisionLoader`、`FloatConstant`、`AudioCrop`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`VHS_LoadVideo`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`LoadAudio`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader
