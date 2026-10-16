---
key: 视频生成/图生视频/LTX2.3 数字人说话&唱歌_2035556711162978305.json
name: LTX2.3 数字人说话&唱歌_2035556711162978305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2035556711162978305.json
hash: cd04224eab39b726
coverage: 0.480392
learned_at: 2026-10-15 22:35:49
nodes: [SetNode, SamplerCustomAdvanced, GetNode, CFGGuider, GetNode, GetNode, GetNode, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, SetNode, SetNode, ManualSigmas, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVConditioning, GetNode, GetNode, SetNode, GetNode, GetNode, LTX2_NAG, VAELoaderKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, SetNode, VAELoaderKJ, SetNode, SetNode, Anything Everywhere, SetNode, LatentUpscaleModelLoader, LTXVPreprocess, SetNode, GetNode, KSamplerSelect, RandomNoise, PathchSageAttentionKJ, VHS_VideoCombine, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, Note, PrimitiveBoolean, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, SetNode, Note, MathExpression|pysssss, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, SetLatentNoiseMask, LTXVAudioVAEEncode, MelBandRoFormerSampler, GetNode, GetNode, SolidMask, CLIPTextEncode, PrimitiveInt, SetNode, ComfyMathExpression, CR Float To Integer, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetNode, SetNode, SetNode, ComfyMathExpression, easy showAnything, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, LTXVCropGuides, RandomNoise, LoadImage, MelBandRoFormerModelLoader, DualCLIPLoader, PrimitiveInt, PrimitiveInt, VHS_LoadAudioUpload, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3 数字人说话&唱歌_2035556711162978305.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035556711162978305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（102 个）：
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
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
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
- `LTXVAudioVAEEncode` ★核心
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
- `LoadImage`
- `MelBandRoFormerModelLoader`
- `DualCLIPLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_LoadAudioUpload`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **48%**（49/102）

**有卡**：`SamplerCustomAdvanced`、`CFGGuider`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConditioning`、`LTX2_NAG`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVPreprocess`、`RandomNoise`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`SolidMask`、`ComfyMathExpression`、`CR Float To Integer`、`LTXVCropGuides`、`LoadImage`、`MelBandRoFormerModelLoader`、`DualCLIPLoader`、`VHS_LoadAudioUpload`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
