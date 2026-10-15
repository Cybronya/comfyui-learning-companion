---
key: 视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json
name: 优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json
hash: 08c82052bd100fab
coverage: 0.721519
learned_at: 2026-10-15 22:47:49
nodes: [KSamplerSelect, CFGGuider, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVChunkFeedForward, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, LoraLoaderModelOnly, LTXVAudioVAELoader, CheckpointLoaderSimple, RandomNoise, RandomNoise, JWDatetimeString, CR Text, LTXVConcatAVLatent, ManualSigmas, LTXVLatentUpsampler, LTXVSeparateAVLatent, MarkdownNote, RH_LLMAPI_Pro_Node, MarkdownNote, PreviewAny, CR Text, MarkdownNote, SetNode, CLIPTextEncode, LTXAVTextEncoderLoader, CLIPTextEncode, GetNode, MathExpression|pysssss, GetNode, LTXVConditioning, LayerUtility: ImageScaleByAspectRatio V2, TextCombinerTwo, Textbox, GetNode, GetNode, SetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, MathExpression|pysssss, MathExpression|pysssss, GetNode, GetNode, PrimitiveFloat, CM_FloatToInt, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVPreprocess, PrimitiveInt, LTXVImgToVideoConditionOnly, INTConstant, INTConstant, INTConstant, SetNode, SetNode, SetNode, INTConstant, PreviewAny, CR Text, AILab_QwenVL, Reroute, Reroute, Bjornulf_IfElse, PreviewAny, GetNode, PrimitiveBoolean, Qwen2.5VL, LoadImage, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（79 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `RandomNoise`
- `JWDatetimeString`
- `CR Text`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `PreviewAny`
- `CR Text`
- `MarkdownNote`
- `SetNode`
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `GetNode`
- `MathExpression|pysssss`
- `GetNode`
- `LTXVConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextCombinerTwo`
- `Textbox`
- `GetNode`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `CM_FloatToInt`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `PrimitiveInt`
- `LTXVImgToVideoConditionOnly`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `PreviewAny`
- `CR Text`
- `AILab_QwenVL`
- `Reroute`
- `Reroute`
- `Bjornulf_IfElse`
- `PreviewAny`
- `GetNode`
- `PrimitiveBoolean`
- `Qwen2.5VL`
- `LoadImage`
- `PrimitiveBoolean`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（57/79）

**有卡**：`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`RandomNoise`、`JWDatetimeString`、`CR Text`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`RH_LLMAPI_Pro_Node`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`MathExpression|pysssss`、`LTXVConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextCombinerTwo`、`Textbox`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`LTXVImgToVideoConditionOnly`、`LTXVPreprocess`、`INTConstant`、`AILab_QwenVL`、`Bjornulf_IfElse`、`PrimitiveBoolean`、`Qwen2.5VL`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
