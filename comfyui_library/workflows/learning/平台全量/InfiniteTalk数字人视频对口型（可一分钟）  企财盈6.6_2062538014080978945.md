---
key: 平台全量/InfiniteTalk数字人视频对口型（可一分钟）  企财盈6.6_2062538014080978945.json
name: InfiniteTalk数字人视频对口型（可一分钟）  企财盈6.6_2062538014080978945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/InfiniteTalk数字人视频对口型（可一分钟）  企财盈6.6_2062538014080978945.json
hash: d39c92cf31f97363
coverage: 0.593496
learned_at: 2026-11-14 00:32:38
nodes: [SetNode, Reroute, Reroute, AudioSeparation, Reroute, Reroute, Reroute, Reroute, SetNode, Reroute, Reroute, Reroute, SetNode, CLIPVisionLoader, Reroute, LoadWanVideoT5TextEncoder, Reroute, Note, GetNode, Reroute, MarkdownNote, DownloadAndLoadWav2VecModel, MathExpression|pysssss, MultiTalkWav2VecEmbeds, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoSampler, WanVideoModelLoader, easy showAnything, MathExpression|pysssss, Audio Duration (mtb), Reroute, WanVideoImageToVideoMultiTalk, Note, LoadVideo, VHS_LoadVideo, HAIGC_VideoPreview, HAIGC_VideoLoader, HAIGC_VideoConcat, GetAudioDurationFromAudio, MathExpression|pysssss, easy showAnything, WanVideoClipVisionEncode, GetImageRangeFromBatch, easy forLoopEnd, easy forLoopStart, SetNode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, Reroute, Reroute, Reroute, SetNode, CLIPVisionLoader, Reroute, LoadWanVideoT5TextEncoder, Note, GetNode, Reroute, DownloadAndLoadWav2VecModel, PlaySound|pysssss, MathExpression|pysssss, MultiTalkWav2VecEmbeds, WanVideoTextEncode, WanVideoSampler, easy showAnything, MathExpression|pysssss, Audio Duration (mtb), Reroute, WanVideoImageToVideoMultiTalk, easy showAnything, Note, WanVideoClipVisionEncode, GetImageRangeFromBatch, GetAudioDurationFromAudio, PlaySound|pysssss, GetNode, WanVideoEncode, Anything Everywhere, WanVideoEncode, WanVideoVAELoader, easy showAnything, GetAudioDurationFromAudio, WanVideoDecode, AudioCrop, easy showAnything, MathExpression|pysssss, AudioCrop, WanVideoDecode, PreviewAudio, easy showAnything, easy showAnything, VHS_VideoInfoLoaded, easy showAnything, VHS_LoadVideo, MathExpression|pysssss, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfoLoaded, PreviewAudio, PreviewAudio, PreviewAudio, AudioSeparation, LoadAudio, WanVideoBlockSwap, LamSaveVideo, WanSkipEndFrameImages_F2, ImageBatch, VHS_VideoCombine, HAIGC_VideoTransition, PrimitiveNode, WanSkipEndFrameImages_F2]
patterns: []
missing: []
---

# 平台全量/InfiniteTalk数字人视频对口型（可一分钟）  企财盈6.6_2062538014080978945.json

> 来源文件 `comfyui_library/workflows/平台全量/InfiniteTalk数字人视频对口型（可一分钟）  企财盈6.6_2062538014080978945.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（123 个）：
- `SetNode`
- `Reroute`
- `Reroute`
- `AudioSeparation`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `CLIPVisionLoader`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `Reroute`
- `Note`
- `GetNode`
- `Reroute`
- `MarkdownNote`
- `DownloadAndLoadWav2VecModel`
- `MathExpression|pysssss`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `easy showAnything`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `Reroute`
- `WanVideoImageToVideoMultiTalk`
- `Note`
- `LoadVideo`
- `VHS_LoadVideo`
- `HAIGC_VideoPreview`
- `HAIGC_VideoLoader`
- `HAIGC_VideoConcat`
- `GetAudioDurationFromAudio`
- `MathExpression|pysssss`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `easy forLoopEnd`
- `easy forLoopStart`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `CLIPVisionLoader`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `GetNode`
- `Reroute`
- `DownloadAndLoadWav2VecModel`
- `PlaySound|pysssss`
- `MathExpression|pysssss`
- `MultiTalkWav2VecEmbeds`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `Reroute`
- `WanVideoImageToVideoMultiTalk`
- `easy showAnything`
- `Note`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `GetAudioDurationFromAudio`
- `PlaySound|pysssss`
- `GetNode`
- `WanVideoEncode`
- `Anything Everywhere`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `easy showAnything`
- `GetAudioDurationFromAudio`
- `WanVideoDecode`
- `AudioCrop`
- `easy showAnything`
- `MathExpression|pysssss`
- `AudioCrop`
- `WanVideoDecode`
- `PreviewAudio`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `VHS_LoadVideo`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfoLoaded`
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `AudioSeparation`
- `LoadAudio`
- `WanVideoBlockSwap`
- `LamSaveVideo`
- `WanSkipEndFrameImages_F2`
- `ImageBatch`
- `VHS_VideoCombine`
- `HAIGC_VideoTransition`
- `PrimitiveNode`
- `WanSkipEndFrameImages_F2`

## 知识

覆盖率 **59%**（73/123）

**有卡**：`AudioSeparation`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`DownloadAndLoadWav2VecModel`、`MathExpression|pysssss`、`MultiTalkWav2VecEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`MultiTalkModelLoader`、`WanVideoSampler`、`WanVideoModelLoader`、`Audio Duration (mtb)`、`WanVideoImageToVideoMultiTalk`、`LoadVideo`、`VHS_LoadVideo`、`HAIGC_VideoPreview`、`HAIGC_VideoLoader`、`HAIGC_VideoConcat`、`GetAudioDurationFromAudio`、`WanVideoClipVisionEncode`、`GetImageRangeFromBatch`、`easy forLoopEnd`、`easy forLoopStart`、`PlaySound|pysssss`、`WanVideoEncode`、`WanVideoVAELoader`、`WanVideoDecode`、`AudioCrop`、`PreviewAudio`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadAudio`、`WanVideoBlockSwap`、`LamSaveVideo`、`WanSkipEndFrameImages_F2`、`ImageBatch`、`VHS_VideoCombine`、`HAIGC_VideoTransition`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
