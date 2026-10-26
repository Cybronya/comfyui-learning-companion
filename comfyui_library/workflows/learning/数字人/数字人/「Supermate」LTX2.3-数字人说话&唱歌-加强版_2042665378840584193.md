---
key: 数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json
name: 「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json
hash: f18f8a084d0333bc
coverage: 0.495327
learned_at: 2026-10-26 01:59:43
nodes: [SetNode, SamplerCustomAdvanced, GetNode, CFGGuider, GetNode, GetNode, GetNode, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, SetNode, SetNode, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, SetNode, GetNode, GetNode, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, SetNode, VAELoaderKJ, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, LTXVPreprocess, SetNode, GetNode, KSamplerSelect, RandomNoise, PathchSageAttentionKJ, VHS_VideoCombine, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, Note, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, SetNode, Note, MathExpression|pysssss, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, SetLatentNoiseMask, MelBandRoFormerSampler, GetNode, GetNode, SolidMask, PrimitiveInt, SetNode, ComfyMathExpression, LTXVConcatAVLatent, SetNode, SetNode, SetNode, ComfyMathExpression, easy showAnything, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, LTXVCropGuides, RandomNoise, MelBandRoFormerModelLoader, DualCLIPLoader, ManualSigmas, PrimitiveInt, PrimitiveInt, LTXVAudioVAEEncode, WujiCleaner, LTXVConditioning, WujiCleaner, LTX2_NAG, GetNode, LTXVImgToVideoInplace, WujiCleaner, CLIPTextEncode, CR Float To Integer, CLIPTextEncode, Note, Label (rgthree), VHS_LoadAudioUpload, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/「Supermate」LTX2.3-数字人说话&唱歌-加强版_2042665378840584193.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（107 个）：
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `SetNode`
- `LatentUpscaleModelLoader`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `PrimitiveBoolean`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetLatentNoiseMask`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `GetNode`
- `SolidMask`
- `PrimitiveInt`
- `SetNode`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `easy showAnything`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `RandomNoise`
- `MelBandRoFormerModelLoader`
- `DualCLIPLoader`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVAudioVAEEncode` ★核心
- `WujiCleaner`
- `LTXVConditioning`
- `WujiCleaner`
- `LTX2_NAG`
- `GetNode`
- `LTXVImgToVideoInplace`
- `WujiCleaner`
- `CLIPTextEncode` ★核心
- `CR Float To Integer`
- `CLIPTextEncode` ★核心
- `Note`
- `Label (rgthree)`
- `VHS_LoadAudioUpload`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **50%**（53/107）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`RandomNoise`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`SolidMask`、`ComfyMathExpression`、`LTXVCropGuides`、`MelBandRoFormerModelLoader`、`DualCLIPLoader`、`LTXVAudioVAEEncode`、`WujiCleaner`、`LTXVConditioning`、`LTX2_NAG`、`CLIPTextEncode`、`CR Float To Integer`、`Label (rgthree)`、`VHS_LoadAudioUpload`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
