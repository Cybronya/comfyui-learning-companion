---
key: 视频生成/图生视频/视频-【S2V数字人】Wan2.2图生视频-语音克隆_1978783026970824706.json
name: 视频-【S2V数字人】Wan2.2图生视频-语音克隆_1978783026970824706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978783026970824706.json
hash: 72de916bf9ad0d04
coverage: 0.761194
learned_at: 2026-10-15 22:32:20
nodes: [Audio Remixer, Load Audio Separation Model, Anything Everywhere, Anything Everywhere, WanVideoVAELoader, ImageCASharpening+, LayerUtility: PurgeVRAM V2, AudioCombine, AudioCombine, AudioCombine, SetNode, PreviewAudio, ColorCorrectOfUtils, WanVideoSetBlockSwap, easy cleanGpuUsed, CLIPVisionLoader, WanVideoModelLoader, RHHiddenNodes, ShowText|pysssss, CR Text Concatenate, Note, GetNode, WanVideoBlockSwap, WanVideoTorchCompileSettings, AudioEncoderLoader, WanVideoEncode, WanVideoLoraSelect, WanVideoLoraSelect, ImageResize+, Note, WanVideoEmptyEmbeds, ImpactSwitch, CR Text, PreviewAudio, AudioCrop, AudioSeparation, AudioEncoderEncode, Note, VHS_LoadVideo, Int, IndexTTSRun, PreviewImage, CR Prompt Text, PreviewAudio, LoadAudio, LoadImage, CR Text Concatenate, WanVideoTextEncode, Anything Everywhere, LoadWanVideoT5TextEncoder, WanVideoTextEncodeCached, WanVideoDecode, GetImageSize, VHS_VideoCombine, RH_Translator, easy showAnything, Audio Duration (mtb), easy showAnything, easy showAnything, GetNode, MathExpression|pysssss, SetNode, MathExpression|pysssss, WanVideoContextOptions, WanVideoAddS2VEmbeds, WanVideoSampler, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/视频-【S2V数字人】Wan2.2图生视频-语音克隆_1978783026970824706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978783026970824706.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（67 个）：
- `Audio Remixer`
- `Load Audio Separation Model`
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM V2`
- `AudioCombine`
- `AudioCombine`
- `AudioCombine`
- `SetNode`
- `PreviewAudio`
- `ColorCorrectOfUtils`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `Note`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `AudioEncoderLoader`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImageResize+`
- `Note`
- `WanVideoEmptyEmbeds`
- `ImpactSwitch`
- `CR Text`
- `PreviewAudio`
- `AudioCrop`
- `AudioSeparation`
- `AudioEncoderEncode`
- `Note`
- `VHS_LoadVideo`
- `Int`
- `IndexTTSRun`
- `PreviewImage`
- `CR Prompt Text`
- `PreviewAudio`
- `LoadAudio`
- `LoadImage`
- `CR Text Concatenate`
- `WanVideoTextEncode`
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `GetImageSize`
- `VHS_VideoCombine`
- `RH_Translator`
- `easy showAnything`
- `Audio Duration (mtb)`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `MathExpression|pysssss`
- `WanVideoContextOptions`
- `WanVideoAddS2VEmbeds`
- `WanVideoSampler` ★核心
- `CR Text`

## 知识

覆盖率 **76%**（51/67）

**有卡**：`Audio Remixer`、`Load Audio Separation Model`、`WanVideoVAELoader`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`AudioCombine`、`PreviewAudio`、`ColorCorrectOfUtils`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanVideoModelLoader`、`RHHiddenNodes`、`CR Text Concatenate`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`AudioEncoderLoader`、`WanVideoEncode`、`WanVideoLoraSelect`、`ImageResize+`、`WanVideoEmptyEmbeds`、`CR Text`、`AudioCrop`、`AudioSeparation`、`AudioEncoderEncode`、`VHS_LoadVideo`、`Int`、`IndexTTSRun`、`CR Prompt Text`、`LoadAudio`、`LoadImage`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`GetImageSize`、`VHS_VideoCombine`、`RH_Translator`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`WanVideoContextOptions`、`WanVideoAddS2VEmbeds`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、AudioEncoderLoader、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、AudioEncoderEncode
