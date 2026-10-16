---
key: 视频生成/图生视频/Wan2.2-infinitetalk数字人 一键MV分镜成片（图生视频）_1997551281285828610.json
name: Wan2.2-infinitetalk数字人 一键MV分镜成片（图生视频）_1997551281285828610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1997551281285828610.json
hash: da2546b0b3ea76fa
coverage: 0.847222
learned_at: 2026-10-15 22:33:29
nodes: [WanVideoBlockSwap, SetNode, VHS_LoadVideo, AudioCombine, AudioCombine, Audio Remixer, Load Audio Separation Model, AudioCombine, SetNode, PreviewAudio, Anything Everywhere, Anything Everywhere, Anything Everywhere, Int, Note, AudioSeparation, WanVideoSLG, AudioCrop, CR Text, Audio Duration (mtb), PreviewAudio, CR Text, MathExpression|pysssss, DownloadAndLoadWav2VecModel, GetNode, SaveAudio, WanVideoExperimentalArgs, WanVideoSetBlockSwap, MathExpression|pysssss, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoBlockSwap, CogVideoEnhanceAVideo, MultiTalkWav2VecEmbeds, easy cleanGpuUsed, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelect, CLIPVisionLoader, WanVideoModelLoader, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkModelLoader, PrimitiveNode, easy cleanGpuUsed, WanVideoVAELoader, VHS_VideoCombine, GetNode, WanVideoSampler, Int, Int, LoadWanVideoT5TextEncoder, ImageCASharpening+, WanVideoDecode, LayerUtility: PurgeVRAM V2, ColorCorrectOfUtils, Note, WanVideoTextEncode, ImpactSwitch, RHHiddenNodes, CR Text Concatenate, CR Text, CR Text, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, CreateCFGScheduleFloatList, ImageResize+, WanVideoTorchCompileSettings, WanVideoTorchCompileSettings, LoadAudio, SaveAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-infinitetalk数字人 一键MV分镜成片（图生视频）_1997551281285828610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997551281285828610.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
- `WanVideoBlockSwap`
- `SetNode`
- `VHS_LoadVideo`
- `AudioCombine`
- `AudioCombine`
- `Audio Remixer`
- `Load Audio Separation Model`
- `AudioCombine`
- `SetNode`
- `PreviewAudio`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `Int`
- `Note`
- `AudioSeparation`
- `WanVideoSLG`
- `AudioCrop`
- `CR Text`
- `Audio Duration (mtb)`
- `PreviewAudio`
- `CR Text`
- `MathExpression|pysssss`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `SaveAudio`
- `WanVideoExperimentalArgs`
- `WanVideoSetBlockSwap`
- `MathExpression|pysssss`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CogVideoEnhanceAVideo`
- `MultiTalkWav2VecEmbeds`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `PrimitiveNode`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSampler` ★核心
- `Int`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `ImageCASharpening+`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `ColorCorrectOfUtils`
- `Note`
- `WanVideoTextEncode`
- `ImpactSwitch`
- `RHHiddenNodes`
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `CreateCFGScheduleFloatList`
- `ImageResize+`
- `WanVideoTorchCompileSettings`
- `WanVideoTorchCompileSettings`
- `LoadAudio`
- `SaveAudio`
- `LoadImage`

## 知识

覆盖率 **85%**（61/72）

**有卡**：`WanVideoBlockSwap`、`VHS_LoadVideo`、`AudioCombine`、`Audio Remixer`、`Load Audio Separation Model`、`PreviewAudio`、`Int`、`AudioSeparation`、`WanVideoSLG`、`AudioCrop`、`CR Text`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`DownloadAndLoadWav2VecModel`、`SaveAudio`、`WanVideoExperimentalArgs`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`CogVideoEnhanceAVideo`、`MultiTalkWav2VecEmbeds`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoModelLoader`、`CLIPVisionLoader`、`MultiTalkModelLoader`、`WanVideoVAELoader`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`、`ImageCASharpening+`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`ColorCorrectOfUtils`、`WanVideoTextEncode`、`RHHiddenNodes`、`CR Text Concatenate`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`CreateCFGScheduleFloatList`、`ImageResize+`、`WanVideoTorchCompileSettings`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
