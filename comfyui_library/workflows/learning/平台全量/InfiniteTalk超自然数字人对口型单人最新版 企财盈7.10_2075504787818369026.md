---
key: 平台全量/InfiniteTalk超自然数字人对口型单人最新版 企财盈7.10_2075504787818369026.json
name: InfiniteTalk超自然数字人对口型单人最新版 企财盈7.10_2075504787818369026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/InfiniteTalk超自然数字人对口型单人最新版 企财盈7.10_2075504787818369026.json
hash: c45dbcf1d7345327
coverage: 0.571429
learned_at: 2026-11-14 00:32:40
nodes: [SetNode, Reroute, Reroute, AudioSeparation, Reroute, Reroute, Reroute, Reroute, SetNode, WanVideoClipVisionEncode, Reroute, Reroute, Reroute, SetNode, CLIPVisionLoader, Reroute, LoadWanVideoT5TextEncoder, PreviewAudio, GetImageRangeFromBatch, Reroute, Anything Everywhere, Note, Note, easy int, GetNode, PreviewAudio, Reroute, WanVideoEncode, MarkdownNote, DownloadAndLoadWav2VecModel, WanVideoDecode, PlaySound|pysssss, MathExpression|pysssss, MultiTalkWav2VecEmbeds, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoSampler, AudioCrop, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, MathExpression|pysssss, Audio Duration (mtb), MathExpression|pysssss, Reroute, WanVideoImageToVideoMultiTalk, VHS_VideoInfoLoaded, LoadAudio, VHS_VideoCombine, easy showAnything, easy showAnything, VHS_LoadVideo, WanVideoTextEncode, easy showAnything, GetAudioDurationFromAudio, easy showAnything]
patterns: []
missing: []
---

# 平台全量/InfiniteTalk超自然数字人对口型单人最新版 企财盈7.10_2075504787818369026.json

> 来源文件 `comfyui_library/workflows/平台全量/InfiniteTalk超自然数字人对口型单人最新版 企财盈7.10_2075504787818369026.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（63 个）：
- `SetNode`
- `Reroute`
- `Reroute`
- `AudioSeparation`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `WanVideoClipVisionEncode`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `CLIPVisionLoader`
- `Reroute`
- `LoadWanVideoT5TextEncoder`
- `PreviewAudio`
- `GetImageRangeFromBatch`
- `Reroute`
- `Anything Everywhere`
- `Note`
- `Note`
- `easy int`
- `GetNode`
- `PreviewAudio`
- `Reroute`
- `WanVideoEncode`
- `MarkdownNote`
- `DownloadAndLoadWav2VecModel`
- `WanVideoDecode`
- `PlaySound|pysssss`
- `MathExpression|pysssss`
- `MultiTalkWav2VecEmbeds`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoSampler` ★核心
- `AudioCrop`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `Reroute`
- `WanVideoImageToVideoMultiTalk`
- `VHS_VideoInfoLoaded`
- `LoadAudio`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy showAnything`
- `VHS_LoadVideo`
- `WanVideoTextEncode`
- `easy showAnything`
- `GetAudioDurationFromAudio`
- `easy showAnything`

## 知识

覆盖率 **57%**（36/63）

**有卡**：`AudioSeparation`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`PreviewAudio`、`GetImageRangeFromBatch`、`easy int`、`WanVideoEncode`、`DownloadAndLoadWav2VecModel`、`WanVideoDecode`、`PlaySound|pysssss`、`MathExpression|pysssss`、`MultiTalkWav2VecEmbeds`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`MultiTalkModelLoader`、`WanVideoSampler`、`AudioCrop`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Audio Duration (mtb)`、`WanVideoImageToVideoMultiTalk`、`VHS_VideoInfoLoaded`、`LoadAudio`、`VHS_VideoCombine`、`VHS_LoadVideo`、`WanVideoTextEncode`、`GetAudioDurationFromAudio`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
