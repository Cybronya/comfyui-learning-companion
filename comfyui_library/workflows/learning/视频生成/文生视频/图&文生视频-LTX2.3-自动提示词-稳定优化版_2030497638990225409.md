---
key: 视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json
name: 图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json
hash: 823bb7932110bf21
coverage: 0.483516
learned_at: 2026-10-11 03:16:52
nodes: [KSamplerSelect, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, RandomNoise, PathchSageAttentionKJ, ModelPatchTorchSettings, GetNode, LayerUtility: ImageScaleByAspectRatio V2, CM_IntToFloat, GetNode, CLIPTextEncode, CLIPTextEncode, easy showAnything, SetNode, LTXVPreprocess, GetNode, SetNode, LTXVChunkFeedForward, SetNode, SetNode, ManualSigmas, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, ManualSigmas, KSamplerSelect, CFGGuider, RandomNoise, SetNode, SetNode, LTXVConditioning, GetNode, GetNode, GetNode, GetNode, LTXVImgToVideoConditionOnly, GetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, PrimitiveBoolean, LTXVImgToVideoConditionOnly, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, INTConstant, SetNode, MathExpression|pysssss, SetNode, INTConstant, INTConstant, MarkdownNote, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, GetNode, LTXVAudioVAEDecode, VHS_VideoCombine, VRAMReserver, LTXVAudioVAELoader, CheckpointLoaderSimple, LatentUpscaleModelLoader, LoraLoaderModelOnly, LoadImage, LTXAVTextEncoderLoader, Text Multiline, Text Multiline, Text Multiline, GetNode, JoinStrings, AILab_QwenVL, INTConstant, Note, Note, Note]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, Text Multiline, Text Multiline, Text Multiline]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（91 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CM_IntToFloat`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `SetNode`
- `LTXVPreprocess`
- `GetNode`
- `SetNode`
- `LTXVChunkFeedForward`
- `SetNode`
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `VRAMReserver`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LTXAVTextEncoderLoader`
- `Text Multiline`
- `Text Multiline`
- `Text Multiline`
- `GetNode`
- `JoinStrings`
- `AILab_QwenVL`
- `INTConstant`
- `Note`
- `Note`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **48%**（44/91）

**有卡**：`KSamplerSelect`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CM_IntToFloat`、`CLIPTextEncode`、`LTXVPreprocess`、`LTXVChunkFeedForward`、`ManualSigmas`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVImgToVideoConditionOnly`、`LTXVLatentUpsampler`、`PrimitiveBoolean`、`INTConstant`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`VRAMReserver`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LoadImage`、`LTXAVTextEncoderLoader`、`JoinStrings`、`AILab_QwenVL`

**缺卡**（5）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`Text Multiline`、`Text Multiline`、`Text Multiline`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
