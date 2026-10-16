---
key: 视频生成/图生视频/【S2V数字人】Wan2.2图生视频-语音克隆_1961362912252203010.json
name: 【S2V数字人】Wan2.2图生视频-语音克隆_1961362912252203010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1961362912252203010.json
hash: e35e5e014e81caea
coverage: 0.790323
learned_at: 2026-10-15 22:31:28
nodes: [SetNode, Audio Remixer, Load Audio Separation Model, Anything Everywhere, Anything Everywhere, WanVideoVAELoader, ImageCASharpening+, LayerUtility: PurgeVRAM V2, GetNode, AudioCombine, AudioCombine, AudioCombine, SetNode, PreviewAudio, Anything Everywhere, CR Text, AudioSeparation, AudioCrop, Note, ImpactSwitch, ColorCorrectOfUtils, IndexTTSRun, LoadWanVideoT5TextEncoder, MathExpression|pysssss, Audio Duration (mtb), WanVideoSetBlockSwap, Int, easy cleanGpuUsed, VHS_VideoCombine, WanVideoSampler, CLIPVisionLoader, LoadAudio, WanVideoDecode, MathExpression|pysssss, WanVideoLoraSelect, AudioEncoderEncode, GetNode, WanVideoEncode, WanVideoModelLoader, WanVideoTorchCompileSettings, PreviewImage, WanVideoTextEncode, Note, RH_Translator, RHHiddenNodes, ShowText|pysssss, CR Text Concatenate, CR Text Concatenate, Note, WanVideoLoraSelect, VHS_LoadVideo, PreviewAudio, CR Prompt Text, WanVideoEmptyEmbeds, AudioEncoderLoader, ImageResize+, CR Text, WanVideoBlockSwap, PreviewAudio, LoadImage, WanVideoAddAudioEmbeds, WanVideoContextOptions]
patterns: []
missing: []
---

# 视频生成/图生视频/【S2V数字人】Wan2.2图生视频-语音克隆_1961362912252203010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1961362912252203010.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（62 个）：
- `SetNode`
- `Audio Remixer`
- `Load Audio Separation Model`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `AudioCombine`
- `AudioCombine`
- `AudioCombine`
- `SetNode`
- `PreviewAudio`
- `Anything Everywhere`
- `CR Text`
- `AudioSeparation`
- `AudioCrop`
- `Note`
- `ImpactSwitch`
- `ColorCorrectOfUtils`
- `IndexTTSRun`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `Audio Duration (mtb)`
- `WanVideoSetBlockSwap`
- `Int`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `LoadAudio`
- `WanVideoDecode`
- `MathExpression|pysssss`
- `WanVideoLoraSelect`
- `AudioEncoderEncode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `PreviewImage`
- `WanVideoTextEncode`
- `Note`
- `RH_Translator`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `Note`
- `WanVideoLoraSelect`
- `VHS_LoadVideo`
- `PreviewAudio`
- `CR Prompt Text`
- `WanVideoEmptyEmbeds`
- `AudioEncoderLoader`
- `ImageResize+`
- `CR Text`
- `WanVideoBlockSwap`
- `PreviewAudio`
- `LoadImage`
- `WanVideoAddAudioEmbeds`
- `WanVideoContextOptions`

## 知识

覆盖率 **79%**（49/62）

**有卡**：`Audio Remixer`、`Load Audio Separation Model`、`WanVideoVAELoader`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`AudioCombine`、`PreviewAudio`、`CR Text`、`AudioSeparation`、`AudioCrop`、`ColorCorrectOfUtils`、`IndexTTSRun`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`Audio Duration (mtb)`、`WanVideoSetBlockSwap`、`Int`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoSampler`、`CLIPVisionLoader`、`LoadAudio`、`WanVideoDecode`、`WanVideoLoraSelect`、`AudioEncoderEncode`、`WanVideoEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`RH_Translator`、`RHHiddenNodes`、`CR Text Concatenate`、`VHS_LoadVideo`、`CR Prompt Text`、`WanVideoEmptyEmbeds`、`AudioEncoderLoader`、`ImageResize+`、`WanVideoBlockSwap`、`LoadImage`、`WanVideoAddAudioEmbeds`、`WanVideoContextOptions`

**用到的条目**：LoadImage、WanVideoSampler、AudioEncoderLoader、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、AudioEncoderEncode
