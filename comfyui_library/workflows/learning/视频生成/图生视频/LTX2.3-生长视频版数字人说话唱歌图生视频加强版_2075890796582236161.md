---
key: 视频生成/图生视频/LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2075890796582236161.json
name: LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2075890796582236161.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2075890796582236161.json
hash: ce7f75e8b2e93815
coverage: 0.495238
learned_at: 2026-10-15 22:41:27
nodes: [SetNode, SamplerCustomAdvanced, GetNode, CFGGuider, GetNode, GetNode, GetNode, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, SetNode, SetNode, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, SetNode, GetNode, GetNode, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, SetNode, VAELoaderKJ, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, LTXVPreprocess, SetNode, GetNode, KSamplerSelect, RandomNoise, PathchSageAttentionKJ, VHS_VideoCombine, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, Note, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, SetNode, Note, MathExpression|pysssss, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, SetLatentNoiseMask, MelBandRoFormerSampler, GetNode, GetNode, SolidMask, CLIPTextEncode, PrimitiveInt, SetNode, ComfyMathExpression, CR Float To Integer, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetNode, SetNode, SetNode, ComfyMathExpression, easy showAnything, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, LTXVCropGuides, RandomNoise, MelBandRoFormerModelLoader, DualCLIPLoader, ManualSigmas, PrimitiveInt, PrimitiveInt, LTXVAudioVAEEncode, WujiCleaner, LTXVConditioning, WujiCleaner, WujiCleaner, LTX2_NAG, VHS_LoadAudioUpload, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-生长视频版数字人说话唱歌图生视频加强版_2075890796582236161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075890796582236161.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（105 个）：
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
- `GetNode`
- `CLIPTextEncode` ★核心
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
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `SetNode`
- `ComfyMathExpression`
- `CR Float To Integer`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
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
- `WujiCleaner`
- `LTX2_NAG`
- `VHS_LoadAudioUpload`
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **50%**（52/105）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`RandomNoise`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`MelBandRoFormerSampler`、`SolidMask`、`ComfyMathExpression`、`CR Float To Integer`、`LTXVCropGuides`、`MelBandRoFormerModelLoader`、`DualCLIPLoader`、`LTXVAudioVAEEncode`、`WujiCleaner`、`LTXVConditioning`、`LTX2_NAG`、`VHS_LoadAudioUpload`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
