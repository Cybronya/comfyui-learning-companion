---
key: 视频生成/文生视频/Ltx2.3数字人唱歌6.9_2064342443386032129.json
name: Ltx2.3数字人唱歌6.9_2064342443386032129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.3数字人唱歌6.9_2064342443386032129.json
hash: c0e95b0ac975d3a1
coverage: 0.839286
learned_at: 2026-10-11 20:21:28
nodes: [ManualSigmas, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, RandomNoise, KSamplerSelect, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, SetNode, LTXVConditioning, VAELoaderKJ, ManualSigmas, LTXVAudioVAEEncode, VAELoaderKJ, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, LTXVCropGuides, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVSeparateAVLatent, SimpleMath+, QZ_ResolutionPreset, SimpleMath+, LTXVImgToVideoInplace, PrimitiveNode, SaveVideo, CLIPTextEncode, LatentUpscaleModelLoader, DualCLIPLoader, CFGGuider, CLIPTextEncode, SoundFlow_GetLength, ComfyMathExpression, Int, CM_FloatToInt, GetNode, SolidMask, SimpleMath+, LoadImage, ImageResizeKJv2, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, SetLatentNoiseMask, LTXVConcatAVLatent, LoadAudio, MelBandRoFormerModelLoader, UNETLoader, LoraLoaderModelOnly, LTX2_NAG, MelBandRoFormerSampler, TrimAudioDuration, PrimitiveInt]
patterns: []
missing: [SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed]
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Ltx2.3数字人唱歌6.9_2064342443386032129.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.3数字人唱歌6.9_2064342443386032129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `LTXVConditioning`
- `VAELoaderKJ`
- `ManualSigmas`
- `LTXVAudioVAEEncode` ★核心
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SimpleMath+`
- `QZ_ResolutionPreset`
- `SimpleMath+`
- `LTXVImgToVideoInplace`
- `PrimitiveNode`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `Int`
- `CM_FloatToInt`
- `GetNode`
- `SolidMask`
- `SimpleMath+`
- `LoadImage`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `MelBandRoFormerSampler` ★核心
- `TrimAudioDuration`
- `PrimitiveInt`

## 知识

覆盖率 **84%**（47/56）

**有卡**：`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVConditioning`、`VAELoaderKJ`、`LTXVAudioVAEEncode`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`QZ_ResolutionPreset`、`LTXVImgToVideoInplace`、`SaveVideo`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`SoundFlow_GetLength`、`ComfyMathExpression`、`Int`、`CM_FloatToInt`、`SolidMask`、`LoadImage`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`LoadAudio`、`MelBandRoFormerModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LTX2_NAG`、`MelBandRoFormerSampler`、`TrimAudioDuration`

**缺卡**（4）：`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
