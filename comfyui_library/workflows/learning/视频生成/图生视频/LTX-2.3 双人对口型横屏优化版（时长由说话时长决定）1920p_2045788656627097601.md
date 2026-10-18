---
key: 视频生成/图生视频/LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json
name: LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json
hash: 909e4f2a0eb3c5bd
coverage: 0.9
learned_at: 2026-10-15 22:36:52
nodes: [RandomNoise, LTXVCropGuides, ManualSigmas, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetLatentNoiseMask, LTXVLatentUpsampler, Reroute, CLIPTextEncode, ComfyMathExpression, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVConditioning, VAELoaderKJ, VAELoaderKJ, KSamplerSelect, PrimitiveBoolean, RandomNoise, LTXVPreprocess, SamplerCustomAdvanced, CFGGuider, ResizeImagesByLongerEdge, ResizeImageMaskNode, ComfyMathExpression, easy showAnything, SimpleCalculatorKJ, easy showAnything, EmptyLTXVLatentVideo, SolidMask, MelBandRoFormerSampler, LTXVAudioVAEEncode, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, TrimAudioDuration, PrimitiveInt, CreateVideo, CLIPTextEncode, LatentUpscaleModelLoader, DualCLIPLoader, MelBandRoFormerModelLoader, LoadImage, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_LoadModel, Text, RunningHub_VoxCPM_Generate, LoadAudio, RunningHub_VoxCPM_Generate, LoadAudio, Text, VHS_VideoCombine, PreviewAudio, PreviewAudio, PreviewAudio, AudioConcat, GetAudioDurationFromAudio, math_calculate, DiffusionModelLoaderKJ, UNETLoader, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX-2.3 双人对口型横屏优化版（时长由说话时长决定）1920p_2045788656627097601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045788656627097601.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（70 个）：
- `RandomNoise`
- `LTXVCropGuides`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `SetLatentNoiseMask`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `PrimitiveBoolean`
- `RandomNoise`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `easy showAnything`
- `SimpleCalculatorKJ`
- `easy showAnything`
- `EmptyLTXVLatentVideo`
- `SolidMask`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `TrimAudioDuration`
- `PrimitiveInt`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `MelBandRoFormerModelLoader`
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_LoadModel`
- `Text`
- `RunningHub_VoxCPM_Generate`
- `LoadAudio`
- `RunningHub_VoxCPM_Generate`
- `LoadAudio`
- `Text`
- `VHS_VideoCombine`
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `AudioConcat`
- `GetAudioDurationFromAudio`
- `math_calculate`
- `DiffusionModelLoaderKJ`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`

## 知识

覆盖率 **90%**（63/70）

**有卡**：`RandomNoise`、`LTXVCropGuides`、`ManualSigmas`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`VAELoaderKJ`、`KSamplerSelect`、`PrimitiveBoolean`、`LTXVPreprocess`、`SamplerCustomAdvanced`、`CFGGuider`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`SimpleCalculatorKJ`、`EmptyLTXVLatentVideo`、`SolidMask`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`VAEDecodeTiled`、`TrimAudioDuration`、`CreateVideo`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`RunningHub_VoxCPM_LoadModel`、`Text`、`RunningHub_VoxCPM_Generate`、`LoadAudio`、`VHS_VideoCombine`、`PreviewAudio`、`AudioConcat`、`GetAudioDurationFromAudio`、`math_calculate`、`DiffusionModelLoaderKJ`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
