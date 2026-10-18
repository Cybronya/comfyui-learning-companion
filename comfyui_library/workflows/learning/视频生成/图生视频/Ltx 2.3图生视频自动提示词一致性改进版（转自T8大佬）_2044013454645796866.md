---
key: 视频生成/图生视频/Ltx 2.3图生视频自动提示词一致性改进版（转自T8大佬）_2044013454645796866.json
name: Ltx 2.3图生视频自动提示词一致性改进版（转自T8大佬）_2044013454645796866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx 2.3图生视频自动提示词一致性改进版（转自T8大佬）_2044013454645796866.json
hash: 46940459c0f1a554
coverage: 0.981818
learned_at: 2026-10-15 22:36:35
nodes: [RandomNoise, LTXVLatentUpsampler, CFGGuider, LTXVPreprocess, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVImgToVideoConditionOnly, easy cleanGpuUsed, VAEDecodeTiled, CFGGuider, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, JWInteger, JWInteger, JWInteger, VAELoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, LTX2AttentionTunerPatch, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveBoolean, CR Text, RH_LLMAPI_Pro_Node, LTXAVTextEncoderLoader, ResizeImageMaskNode, ConcatTextOfUtils, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, PrimitiveFloat, ManualSigmas, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CM_FloatToInt, LTX2_NAG, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, UNETLoader, CR Prompt Text, LoadImage, CR Text, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/Ltx 2.3图生视频自动提示词一致性改进版（转自T8大佬）_2044013454645796866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044013454645796866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（55 个）：
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVImgToVideoConditionOnly`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `CFGGuider`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `VAELoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `LTXAVTextEncoderLoader`
- `ResizeImageMaskNode`
- `ConcatTextOfUtils`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（54/55）

**有卡**：`RandomNoise`、`LTXVLatentUpsampler`、`CFGGuider`、`LTXVPreprocess`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVImgToVideoConditionOnly`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`ManualSigmas`、`JWInteger`、`VAELoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`CR Text`、`RH_LLMAPI_Pro_Node`、`LTXAVTextEncoderLoader`、`ResizeImageMaskNode`、`ConcatTextOfUtils`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`LTX2_NAG`、`UNETLoader`、`CR Prompt Text`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
