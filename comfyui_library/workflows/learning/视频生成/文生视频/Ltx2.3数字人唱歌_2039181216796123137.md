---
key: 视频生成/文生视频/Ltx2.3数字人唱歌_2039181216796123137.json
name: Ltx2.3数字人唱歌_2039181216796123137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.3数字人唱歌_2039181216796123137.json
hash: 9b370fe2c6c3e43c
coverage: 0.909091
learned_at: 2026-10-15 22:45:21
nodes: [ManualSigmas, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, RandomNoise, KSamplerSelect, LatentUpscaleModelLoader, CFGGuider, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, SetNode, DualCLIPLoader, LoraLoaderModelOnly, LTXVConditioning, VAELoaderKJ, ManualSigmas, Int, PrimitiveInt, SimpleMath+, ComfyMathExpression, SoundFlow_GetLength, CM_FloatToInt, MelBandRoFormerSampler, MelBandRoFormerModelLoader, LTXVAudioVAEEncode, ImageResizeKJv2, VAELoaderKJ, CLIPTextEncode, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, EmptyLTXVLatentVideo, UNETLoader, SolidMask, GetNode, LTXVCropGuides, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVSeparateAVLatent, SimpleMath+, QZ_ResolutionPreset, SimpleMath+, LTXVImgToVideoInplace, LTXVImgToVideoInplace, CLIPTextEncode, LoadAudio, SetLatentNoiseMask, LTXVConcatAVLatent, LoadImage, PrimitiveNode, TrimAudioDuration, SaveVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/Ltx2.3数字人唱歌_2039181216796123137.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.3数字人唱歌_2039181216796123137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `CFGGuider`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `VAELoaderKJ`
- `ManualSigmas`
- `Int`
- `PrimitiveInt`
- `SimpleMath+`
- `ComfyMathExpression`
- `SoundFlow_GetLength`
- `CM_FloatToInt`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `LTXVAudioVAEEncode` ★核心
- `ImageResizeKJv2`
- `VAELoaderKJ`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `UNETLoader` ★核心
- `SolidMask`
- `GetNode`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SimpleMath+`
- `QZ_ResolutionPreset`
- `SimpleMath+`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LoadImage`
- `PrimitiveNode`
- `TrimAudioDuration`
- `SaveVideo`

## 知识

覆盖率 **91%**（50/55）

**有卡**：`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LTXVConditioning`、`VAELoaderKJ`、`Int`、`SimpleMath+`、`ComfyMathExpression`、`SoundFlow_GetLength`、`CM_FloatToInt`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`LTXVAudioVAEEncode`、`ImageResizeKJv2`、`CLIPTextEncode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`EmptyLTXVLatentVideo`、`UNETLoader`、`SolidMask`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`QZ_ResolutionPreset`、`LTXVImgToVideoInplace`、`LoadAudio`、`SetLatentNoiseMask`、`LoadImage`、`TrimAudioDuration`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
