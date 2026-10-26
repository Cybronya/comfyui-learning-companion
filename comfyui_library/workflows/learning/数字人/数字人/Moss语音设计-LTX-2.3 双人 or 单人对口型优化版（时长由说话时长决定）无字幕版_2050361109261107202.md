---
key: 数字人/数字人/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）无字幕版_2050361109261107202.json
name: Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）无字幕版_2050361109261107202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）无字幕版_2050361109261107202.json
hash: d21422dd74ad896f
coverage: 0.8875
learned_at: 2026-10-26 01:56:46
nodes: [RandomNoise, LTXVCropGuides, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetLatentNoiseMask, LTXVLatentUpsampler, Reroute, ComfyMathExpression, LTXVAudioVAEDecode, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, CFGGuider, easy showAnything, EmptyLTXVLatentVideo, SolidMask, LTXVAudioVAEEncode, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, TrimAudioDuration, CreateVideo, UNETLoader, ComfyMathExpression, RunningHub_VoxCPM_LoadModel, PreviewAudio, ManualSigmas, KSamplerSelect, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, DiffusionModelLoaderKJ, VAELoaderKJ, VAELoaderKJ, LoadAudio, MossTTSModelLoader, LayerUtility: PurgeVRAM V2, RunningHub_VoxCPM_Generate, Text, LoadAudio, RunningHub_VoxCPM_LoadModel, PreviewAudio, LayerUtility: PurgeVRAM V2, RunningHub_VoxCPM_Generate, LayerUtility: PurgeVRAM V2, Text, SimpleCalculatorKJ, PreviewAudio, MossTTSModelLoader, CLIPTextEncode, LTXVConditioning, LatentUpscaleModelLoader, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, GetAudioDurationFromAudio, LayerUtility: PurgeVRAM V2, PreviewAudio, PrimitiveInt, LoraLoaderModelOnly, DualCLIPLoader, math_calculate, easy showAnything, MelBandRoFormerModelLoader, MelBandRoFormerSampler, Fast Groups Muter (rgthree), LoadImage, MossTTSVoiceDesign, PreviewAudio, AudioConcat, MossTTSVoiceDesign, Note, CLIPTextEncode, VHS_VideoCombine, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 数字人/数字人/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）无字幕版_2050361109261107202.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Moss语音设计-LTX-2.3 双人 or 单人对口型优化版（时长由说话时长决定）无字幕版_2050361109261107202.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（80 个）：
- `RandomNoise`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `SetLatentNoiseMask`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `TrimAudioDuration`
- `CreateVideo`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `RunningHub_VoxCPM_LoadModel`
- `PreviewAudio`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `DiffusionModelLoaderKJ`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoadAudio`
- `MossTTSModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `RunningHub_VoxCPM_Generate`
- `Text`
- `LoadAudio`
- `RunningHub_VoxCPM_LoadModel`
- `PreviewAudio`
- `LayerUtility: PurgeVRAM V2`
- `RunningHub_VoxCPM_Generate`
- `LayerUtility: PurgeVRAM V2`
- `Text`
- `SimpleCalculatorKJ`
- `PreviewAudio`
- `MossTTSModelLoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetAudioDurationFromAudio`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAudio`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `math_calculate`
- `easy showAnything`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `Fast Groups Muter (rgthree)`
- `LoadImage`
- `MossTTSVoiceDesign`
- `PreviewAudio`
- `AudioConcat`
- `MossTTSVoiceDesign`
- `Note`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **89%**（71/80）

**有卡**：`RandomNoise`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LTXVLatentUpsampler`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`SamplerCustomAdvanced`、`CFGGuider`、`EmptyLTXVLatentVideo`、`SolidMask`、`LTXVAudioVAEEncode`、`ManualSigmas`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`TrimAudioDuration`、`CreateVideo`、`UNETLoader`、`RunningHub_VoxCPM_LoadModel`、`PreviewAudio`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`DiffusionModelLoaderKJ`、`VAELoaderKJ`、`LoadAudio`、`MossTTSModelLoader`、`LayerUtility: PurgeVRAM V2`、`RunningHub_VoxCPM_Generate`、`Text`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`GetAudioDurationFromAudio`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`math_calculate`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LoadImage`、`MossTTSVoiceDesign`、`AudioConcat`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
