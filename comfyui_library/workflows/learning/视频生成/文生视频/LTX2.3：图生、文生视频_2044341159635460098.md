---
key: 视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json
name: LTX2.3：图生、文生视频_2044341159635460098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json
hash: de12ad41b50b2843
coverage: 0.788462
learned_at: 2026-10-11 19:49:40
nodes: [LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, KSamplerSelect, CFGGuider, LTXVPreprocess, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVConditioning, CLIPTextEncode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, EmptyLTXVLatentVideo, PrimitiveInt, VHS_VideoCombine, LTXVLatentUpsampler, INTConstant, PreviewAny, LayerUtility: ImageScaleByAspectRatio V2, LTXAVTextEncoderLoader, CM_FloatToInt, PrimitiveFloat, RandomNoise, RandomNoise, ManualSigmas, INTConstant, RH_LLMAPI_Pro_Node, CR Text, CLIPTextEncode, PrimitiveBoolean, LoraLoaderModelOnly, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, CR Text, INTConstant, MarkdownNote, CR Text, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: [CR Text, CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（52 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVPreprocess`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LTXVLatentUpsampler` ★核心
- `INTConstant`
- `PreviewAny`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXAVTextEncoderLoader`
- `CM_FloatToInt`
- `PrimitiveFloat`
- `RandomNoise`
- `RandomNoise`
- `ManualSigmas`
- `INTConstant`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `CR Text`
- `INTConstant`
- `MarkdownNote`
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **79%**（41/52）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`KSamplerSelect`、`CFGGuider`、`LTXVPreprocess`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`INTConstant`、`LTXAVTextEncoderLoader`、`CM_FloatToInt`、`RandomNoise`、`RH_LLMAPI_Pro_Node`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoadImage`

**缺卡**（4）：`CR Text`、`CR Text`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
