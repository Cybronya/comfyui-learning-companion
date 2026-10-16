---
key: 视频生成/图生视频/LTX2.3 音色参考（ID-lora）生视频_2043718764537057282.json
name: LTX2.3 音色参考（ID-lora）生视频_2043718764537057282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043718764537057282.json
hash: cc7d7d6d1533f0c7
coverage: 0.46729
learned_at: 2026-10-15 22:36:33
nodes: [GetNode, SetNode, CFGGuider, GetNode, GetNode, GetNode, CFGGuider, KSamplerSelect, GetNode, LTXVAudioVAEDecode, GetNode, easy cleanGpuUsed, ManualSigmas, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, GetNode, VAELoaderKJ, ModelPatchTorchSettings, SetNode, SetNode, Anything Everywhere, SetNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, RandomNoise, GetNode, PathchSageAttentionKJ, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, GetNode, GetNode, SetNode, SetNode, MathExpression|pysssss, MathExpression|pysssss, PrimitiveInt, SetNode, SetNode, SetNode, SetNode, PrimitiveInt, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, RandomNoise, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, SetNode, Note, ManualSigmas, PrimitiveBoolean, EmptyLTXVLatentVideo, LTXVChunkFeedForward, SetNode, VAELoaderKJ, SetNode, SamplerCustomAdvanced, LatentUpscaleModelLoader, SamplerCustomAdvanced, GetNode, KSamplerSelect, LTXVCropGuides, GetNode, CLIPTextEncode, CLIPTextEncode, SetNode, MelBandRoFormerSampler, LTXVReferenceAudio, GetNode, GetNode, GetNode, GetNode, LTXVConditioning, LTX2_NAG, SetNode, PrimitiveInt, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, SetNode, LTXVImgToVideoInplace, GetNode, LTXVImgToVideoInplace, LoadImage, Note, LoraLoaderModelOnly, DualCLIPLoader, MelBandRoFormerModelLoader, SetNode, AudioCrop, Note, PrimitiveInt, PrimitiveStringMultiline, UNETLoader, LoadAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 音色参考（ID-lora）生视频_2043718764537057282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043718764537057282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（107 个）：
- `GetNode`
- `SetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `SetNode`
- `Note`
- `ManualSigmas`
- `PrimitiveBoolean`
- `EmptyLTXVLatentVideo`
- `LTXVChunkFeedForward`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `LTXVReferenceAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `LTX2_NAG`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LoadImage`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `MelBandRoFormerModelLoader`
- `SetNode`
- `AudioCrop`
- `Note`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadAudio`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（50/107）

**有卡**：`CFGGuider`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`easy cleanGpuUsed`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`VAELoaderKJ`、`ModelPatchTorchSettings`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`RandomNoise`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`MathExpression|pysssss`、`LTXVLatentUpsampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`PrimitiveBoolean`、`EmptyLTXVLatentVideo`、`LTXVChunkFeedForward`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`CLIPTextEncode`、`MelBandRoFormerSampler`、`LTXVReferenceAudio`、`LTXVConditioning`、`LTX2_NAG`、`ComfyMathExpression`、`LTXVImgToVideoInplace`、`LoadImage`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`AudioCrop`、`UNETLoader`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
