---
key: 数字人/数字人/【视频对口型】Wan2.1-infinitetalk数字人（视频生视频）_1959331787396820994.json
name: 【视频对口型】Wan2.1-infinitetalk数字人（视频生视频）_1959331787396820994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/【视频对口型】Wan2.1-infinitetalk数字人（视频生视频）_1959331787396820994.json
hash: 1e8e7d3d603b2a22
coverage: 0.824561
learned_at: 2026-10-26 02:00:00
nodes: [SetNode, Audio Remixer, Load Audio Separation Model, Anything Everywhere, Anything Everywhere, Int, AudioSeparation, WanVideoSLG, AudioCrop, DownloadAndLoadWav2VecModel, GetNode, WanVideoExperimentalArgs, CogVideoEnhanceAVideo, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, ImpactSwitch, LoadAudio, SaveAudio, ImageCASharpening+, LayerUtility: PurgeVRAM V2, GetNode, VHS_VideoCombine, Note, AudioCombine, AudioCombine, AudioCombine, SetNode, PreviewAudio, Anything Everywhere, easy cleanGpuUsed, WanVideoSetBlockSwap, SaveAudio, MathExpression|pysssss, MathExpression|pysssss, Audio Duration (mtb), WanVideoDecode, WanVideoTextEncode, MultiTalkModelLoader, WanVideoBlockSwap, WanVideoSampler, ImageResize+, CR Text, CR Text, PreviewAudio, VHS_LoadVideo, VHS_LoadVideo, WanVideoClipVisionEncode, ColorCorrectOfUtils, Note, WanVideoModelLoader, MultiTalkWav2VecEmbeds, WanVideoLoraSelect, WanVideoEncode, WanVideoImageToVideoMultiTalk, CR Text, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 数字人/数字人/【视频对口型】Wan2.1-infinitetalk数字人（视频生视频）_1959331787396820994.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/【视频对口型】Wan2.1-infinitetalk数字人（视频生视频）_1959331787396820994.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（57 个）：
- `SetNode`
- `Audio Remixer`
- `Load Audio Separation Model`
- `Anything Everywhere`
- `Anything Everywhere`
- `Int`
- `AudioSeparation`
- `WanVideoSLG`
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `WanVideoExperimentalArgs`
- `CogVideoEnhanceAVideo`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `ImpactSwitch`
- `LoadAudio`
- `SaveAudio`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `AudioCombine`
- `AudioCombine`
- `AudioCombine`
- `SetNode`
- `PreviewAudio`
- `Anything Everywhere`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `SaveAudio`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `ImageResize+`
- `CR Text`
- `CR Text`
- `PreviewAudio`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `WanVideoClipVisionEncode`
- `ColorCorrectOfUtils`
- `Note`
- `WanVideoModelLoader`
- `MultiTalkWav2VecEmbeds`
- `WanVideoLoraSelect`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `CR Text`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **82%**（47/57）

**有卡**：`Audio Remixer`、`Load Audio Separation Model`、`Int`、`AudioSeparation`、`WanVideoSLG`、`AudioCrop`、`DownloadAndLoadWav2VecModel`、`WanVideoExperimentalArgs`、`CogVideoEnhanceAVideo`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadAudio`、`SaveAudio`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`AudioCombine`、`PreviewAudio`、`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`MathExpression|pysssss`、`Audio Duration (mtb)`、`WanVideoDecode`、`WanVideoTextEncode`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`ImageResize+`、`CR Text`、`VHS_LoadVideo`、`WanVideoClipVisionEncode`、`ColorCorrectOfUtils`、`WanVideoModelLoader`、`MultiTalkWav2VecEmbeds`、`WanVideoLoraSelect`、`WanVideoEncode`、`WanVideoImageToVideoMultiTalk`、`WanVideoTorchCompileSettings`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelect
