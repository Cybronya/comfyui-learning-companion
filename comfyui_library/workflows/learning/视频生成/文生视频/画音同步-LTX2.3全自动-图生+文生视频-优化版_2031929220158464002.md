---
key: 视频生成/文生视频/画音同步-LTX2.3全自动-图生+文生视频-优化版_2031929220158464002.json
name: 画音同步-LTX2.3全自动-图生+文生视频-优化版_2031929220158464002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/画音同步-LTX2.3全自动-图生+文生视频-优化版_2031929220158464002.json
hash: a813bc0675a0102d
coverage: 0.8
learned_at: 2026-10-11 03:16:53
nodes: [LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, KSamplerSelect, CFGGuider, LTXVPreprocess, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, EmptyLTXVLatentVideo, PrimitiveInt, VHS_VideoCombine, LTXVLatentUpsampler, PreviewAny, CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CheckpointLoaderSimple, CM_FloatToInt, PrimitiveFloat, RandomNoise, RandomNoise, RH_LLMAPI_Pro_Node, INTConstant, INTConstant, ManualSigmas, CR Text, SimpleMath+, easy int, PrimitiveBoolean, MarkdownNote, LoadImage]
patterns: []
missing: [CR Text, CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, easy int]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/画音同步-LTX2.3全自动-图生+文生视频-优化版_2031929220158464002.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/画音同步-LTX2.3全自动-图生+文生视频-优化版_2031929220158464002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
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
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LTXVLatentUpsampler` ★核心
- `PreviewAny`
- `CR Text`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `CM_FloatToInt`
- `PrimitiveFloat`
- `RandomNoise`
- `RandomNoise`
- `RH_LLMAPI_Pro_Node`
- `INTConstant`
- `INTConstant`
- `ManualSigmas`
- `CR Text`
- `SimpleMath+`
- `easy int`
- `PrimitiveBoolean`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **80%**（40/50）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVImgToVideoConditionOnly`、`KSamplerSelect`、`CFGGuider`、`LTXVPreprocess`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`CM_FloatToInt`、`RandomNoise`、`RH_LLMAPI_Pro_Node`、`INTConstant`、`PrimitiveBoolean`、`LoadImage`

**缺卡**（6）：`CR Text`、`CR Text`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`easy int`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
