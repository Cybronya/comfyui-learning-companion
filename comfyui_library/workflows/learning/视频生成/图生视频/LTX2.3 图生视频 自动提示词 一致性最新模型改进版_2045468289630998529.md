---
key: 视频生成/图生视频/LTX2.3 图生视频 自动提示词 一致性最新模型改进版_2045468289630998529.json
name: LTX2.3 图生视频 自动提示词 一致性最新模型改进版_2045468289630998529.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2045468289630998529.json
hash: 244b5f7c8e6b1237
coverage: 0.931034
learned_at: 2026-10-15 22:36:48
nodes: [RandomNoise, SamplerCustomAdvanced, CLIPTextEncode, JWInteger, JWInteger, Note, Note, Note, LoadImage, CR Text, UNETLoader, JWInteger, LTXVEmptyLatentAudio, CM_FloatToInt, LTX2AttentionTunerPatch, LTXVConcatAVLatent, LoraLoaderModelOnly, PathchSageAttentionKJ, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, ManualSigmas, CR Text, LTXAVTextEncoderLoader, ConcatTextOfUtils, CLIPTextEncode, RH_LLMAPI_Pro_Node, LatentUpscaleModelLoader, ResizeImageMaskNode, LTXVLatentUpsampler, LoraLoaderModelOnly, VAEDecodeTiled, easy cleanGpuUsed, ModelPatchTorchSettings, LTXVChunkFeedForward, CFGGuider, LTX2_NAG, LTXVConditioning, CFGGuider, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, LTXVAudioVAELoader, VAELoader, PrimitiveFloat, CR Prompt Text, KSamplerSelect, ManualSigmas, VAEDecodeTiled, LTXVAudioVAEDecode, PrimitiveBoolean, LTXVImgToVideoConditionOnly, LTXVPreprocess, KSamplerSelect, VHS_VideoCombine, VHS_VideoCombine, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 图生视频 自动提示词 一致性最新模型改进版_2045468289630998529.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045468289630998529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（58 个）：
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `CR Text`
- `UNETLoader` ★核心
- `JWInteger`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `LTX2AttentionTunerPatch`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `ManualSigmas`
- `CR Text`
- `LTXAVTextEncoderLoader`
- `ConcatTextOfUtils`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `LatentUpscaleModelLoader`
- `ResizeImageMaskNode`
- `LTXVLatentUpsampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `CFGGuider`
- `LTX2_NAG`
- `LTXVConditioning`
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `VAELoader`
- `PrimitiveFloat`
- `CR Prompt Text`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveBoolean`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（54/58）

**有卡**：`RandomNoise`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`JWInteger`、`LoadImage`、`CR Text`、`UNETLoader`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`LTX2AttentionTunerPatch`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`ManualSigmas`、`LTXAVTextEncoderLoader`、`ConcatTextOfUtils`、`RH_LLMAPI_Pro_Node`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`CFGGuider`、`LTX2_NAG`、`LTXVConditioning`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`VAELoader`、`CR Prompt Text`、`KSamplerSelect`、`PrimitiveBoolean`、`LTXVPreprocess`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
