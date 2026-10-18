---
key: 视频生成/图生视频/Ltx2.3-Dasiwa_V3--图生视频(人脸一致性)_2070741486152544258.json
name: Ltx2.3-Dasiwa_V3--图生视频(人脸一致性)_2070741486152544258.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3-Dasiwa_V3--图生视频(人脸一致性)_2070741486152544258.json
hash: 6842761798887f38
coverage: 0.913043
learned_at: 2026-10-15 22:40:41
nodes: [RandomNoise, KSamplerSelect, SamplerCustomAdvanced, ModelPatchTorchSettings, PrimitiveBoolean, Note, Note, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAELoader, VAELoader, LTXVEmptyLatentAudio, CM_FloatToInt, ResizeImageMaskNode, LTXVPreprocess, LTXVConcatAVLatent, PathchSageAttentionKJ, LTXVChunkFeedForward, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, CR Text, LTXVConditioning, LTXAVTextEncoderLoader, CR Prompt Text, ConcatTextOfUtils, CLIPTextEncode, RH_LLMAPI_Pro_Node, CFGGuider, LTX2_NAG, CLIPTextEncode, LTX2AttentionTunerPatch, JWInteger, JWInteger, JWInteger, LatentUpscaleModelLoader, CR Text, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LTXVAudioVAEDecode, easy cleanGpuUsed, PrimitiveFloat, VHS_VideoCombine, ManualSigmas, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/Ltx2.3-Dasiwa_V3--图生视频(人脸一致性)_2070741486152544258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070741486152544258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（46 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelPatchTorchSettings`
- `PrimitiveBoolean`
- `Note`
- `Note`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAELoader`
- `VAELoader`
- `LTXVEmptyLatentAudio` ★核心
- `CM_FloatToInt`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `CR Text`
- `LTXVConditioning`
- `LTXAVTextEncoderLoader`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `CFGGuider`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `LTX2AttentionTunerPatch`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LatentUpscaleModelLoader`
- `CR Text`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LTXVAudioVAEDecode` ★核心
- `easy cleanGpuUsed`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `ManualSigmas`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ModelPatchTorchSettings`、`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAELoader`、`VAELoader`、`LTXVEmptyLatentAudio`、`CM_FloatToInt`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`CR Text`、`LTXVConditioning`、`LTXAVTextEncoderLoader`、`CR Prompt Text`、`ConcatTextOfUtils`、`CLIPTextEncode`、`RH_LLMAPI_Pro_Node`、`CFGGuider`、`LTX2_NAG`、`LTX2AttentionTunerPatch`、`JWInteger`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LTXVAudioVAEDecode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`ManualSigmas`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
