---
key: 数字人/数字人/视频语音对口型 InfiniteTalk-Wan2.1_2027827389857796097.json
name: 视频语音对口型 InfiniteTalk-Wan2.1_2027827389857796097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频语音对口型 InfiniteTalk-Wan2.1_2027827389857796097.json
hash: f9fa43974dd3e961
coverage: 0.756098
learned_at: 2026-10-26 02:05:27
nodes: [LayerUtility: PurgeVRAM, ImageResizeKJv2, Audio Duration (mtb), GetImageSizeAndCount, GetNode, MultiTalkModelLoader, WanVideoLoraSelect, SetNode, GetImageRangeFromBatch, WanVideoDecode, WanVideoVAELoader, WanVideoModelLoader, WanVideoBlockSwap, LayerUtility: PurgeVRAM, SimpleMath+, ImageFromBatch+, SimpleMath+, PreviewAny, AudioSeparation, LayerUtility: PurgeVRAM, SetNode, SimpleMath+, SetNode, AudioCrop, WanVideoSampler, WanVideoImageToVideoMultiTalk, CLIPVisionLoader, DownloadAndLoadWav2VecModel, MultiTalkWav2VecEmbeds, WanVideoClipVisionEncode, WanVideoEncode, VHS_VideoCombine, JjkText, Note, VHS_VideoInfoLoaded, PrimitiveString, WanVideoTextEncodeCached, PrimitiveInt, VHS_LoadVideo, PrimitiveInt, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/视频语音对口型 InfiniteTalk-Wan2.1_2027827389857796097.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频语音对口型 InfiniteTalk-Wan2.1_2027827389857796097.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `LayerUtility: PurgeVRAM`
- `ImageResizeKJv2`
- `Audio Duration (mtb)`
- `GetImageSizeAndCount`
- `GetNode`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `SetNode`
- `GetImageRangeFromBatch`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `SimpleMath+`
- `ImageFromBatch+`
- `SimpleMath+`
- `PreviewAny`
- `AudioSeparation`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `AudioCrop`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoMultiTalk`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `MultiTalkWav2VecEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `JjkText`
- `Note`
- `VHS_VideoInfoLoaded`
- `PrimitiveString`
- `WanVideoTextEncodeCached`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `LoadAudio`

## 知识

覆盖率 **76%**（31/41）

**有卡**：`LayerUtility: PurgeVRAM`、`ImageResizeKJv2`、`Audio Duration (mtb)`、`GetImageSizeAndCount`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`GetImageRangeFromBatch`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`SimpleMath+`、`ImageFromBatch+`、`AudioSeparation`、`AudioCrop`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`CLIPVisionLoader`、`DownloadAndLoadWav2VecModel`、`MultiTalkWav2VecEmbeds`、`WanVideoClipVisionEncode`、`WanVideoEncode`、`VHS_VideoCombine`、`VHS_VideoInfoLoaded`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadAudio`

**用到的条目**：WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode、WanVideoLoraSelect、CLIPVisionLoader
