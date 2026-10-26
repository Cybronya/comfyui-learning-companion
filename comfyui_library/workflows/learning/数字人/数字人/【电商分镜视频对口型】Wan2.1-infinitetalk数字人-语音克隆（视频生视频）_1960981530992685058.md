---
key: 数字人/数字人/【电商分镜视频对口型】Wan2.1-infinitetalk数字人-语音克隆（视频生视频）_1960981530992685058.json
name: 【电商分镜视频对口型】Wan2.1-infinitetalk数字人-语音克隆（视频生视频）_1960981530992685058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/【电商分镜视频对口型】Wan2.1-infinitetalk数字人-语音克隆（视频生视频）_1960981530992685058.json
hash: 2455e63c75f0e15e
coverage: 0.809524
learned_at: 2026-10-26 01:59:58
nodes: [SetNode, Audio Remixer, Load Audio Separation Model, Anything Everywhere, Anything Everywhere, WanVideoSLG, DownloadAndLoadWav2VecModel, CogVideoEnhanceAVideo, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ImageCASharpening+, LayerUtility: PurgeVRAM V2, GetNode, VHS_VideoCombine, AudioCombine, AudioCombine, AudioCombine, SetNode, PreviewAudio, Anything Everywhere, easy cleanGpuUsed, WanVideoSetBlockSwap, MathExpression|pysssss, MathExpression|pysssss, Audio Duration (mtb), WanVideoDecode, MultiTalkModelLoader, WanVideoBlockSwap, CR Text, WanVideoClipVisionEncode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelect, VHS_LoadVideo, AudioSeparation, AudioCrop, CR Prompt Text, LoadAudio, Int, Note, ImpactSwitch, PreviewAudio, SaveAudio, MultiTalkWav2VecEmbeds, GetNode, WanVideoSampler, WanVideoExperimentalArgs, CR Text, CR Text, Note, IndexTTSRun, PreviewAudio, WanVideoTextEncode, WanVideoEncode, WanVideoImageToVideoMultiTalk, ImageResize+, ReverseImageBatch, Make Image Batch, ColorCorrectOfUtils, Note, Note, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/【电商分镜视频对口型】Wan2.1-infinitetalk数字人-语音克隆（视频生视频）_1960981530992685058.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/【电商分镜视频对口型】Wan2.1-infinitetalk数字人-语音克隆（视频生视频）_1960981530992685058.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（63 个）：
- `SetNode`
- `Audio Remixer`
- `Load Audio Separation Model`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoSLG`
- `DownloadAndLoadWav2VecModel`
- `CogVideoEnhanceAVideo`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `VHS_VideoCombine`
- `AudioCombine`
- `AudioCombine`
- `AudioCombine`
- `SetNode`
- `PreviewAudio`
- `Anything Everywhere`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `WanVideoDecode`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `CR Text`
- `WanVideoClipVisionEncode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `VHS_LoadVideo`
- `AudioSeparation`
- `AudioCrop`
- `CR Prompt Text`
- `LoadAudio`
- `Int`
- `Note`
- `ImpactSwitch`
- `PreviewAudio`
- `SaveAudio`
- `MultiTalkWav2VecEmbeds`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `CR Text`
- `CR Text`
- `Note`
- `IndexTTSRun`
- `PreviewAudio`
- `WanVideoTextEncode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `ImageResize+`
- `ReverseImageBatch`
- `Make Image Batch`
- `ColorCorrectOfUtils`
- `Note`
- `Note`
- `VHS_LoadVideo`

## 知识

覆盖率 **81%**（51/63）

**有卡**：`Audio Remixer`、`Load Audio Separation Model`、`WanVideoSLG`、`DownloadAndLoadWav2VecModel`、`CogVideoEnhanceAVideo`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`AudioCombine`、`PreviewAudio`、`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`MathExpression|pysssss`、`Audio Duration (mtb)`、`WanVideoDecode`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`CR Text`、`WanVideoClipVisionEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`AudioSeparation`、`AudioCrop`、`CR Prompt Text`、`LoadAudio`、`Int`、`SaveAudio`、`MultiTalkWav2VecEmbeds`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`IndexTTSRun`、`WanVideoTextEncode`、`WanVideoEncode`、`WanVideoImageToVideoMultiTalk`、`ImageResize+`、`ReverseImageBatch`、`Make Image Batch`、`ColorCorrectOfUtils`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelect
