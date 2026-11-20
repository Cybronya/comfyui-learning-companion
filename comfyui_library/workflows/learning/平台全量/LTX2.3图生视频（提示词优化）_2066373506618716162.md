---
key: 平台全量/LTX2.3图生视频（提示词优化）_2066373506618716162.json
name: LTX2.3图生视频（提示词优化）_2066373506618716162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3图生视频（提示词优化）_2066373506618716162.json
hash: fa0c01f23aeacf9c
coverage: 0.975
learned_at: 2026-11-14 00:38:38
nodes: [CFGGuider, KSamplerSelect, easy int, SimpleMath+, ModelPatchTorchSettings, LTXVImgToVideoConditionOnly, LTXVChunkFeedForward, EmptyLTXVLatentVideo, CLIPTextEncode, LTXVConditioning, PrimitiveFloat, CM_FloatToInt, LTXVEmptyLatentAudio, PrimitiveBoolean, LTXVConcatAVLatent, LTXVAudioVAELoader, easy cleanGpuUsed, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, RandomNoise, CheckpointLoaderSimple, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, CLIPTextEncode, LTXAVTextEncoderLoader, VHS_VideoCombine, easy int, Seed (rgthree), ManualSigmas, SamplerCustomAdvanced, CR Text, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, easy int, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 平台全量/LTX2.3图生视频（提示词优化）_2066373506618716162.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3图生视频（提示词优化）_2066373506618716162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（40 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `easy int`
- `SimpleMath+`
- `ModelPatchTorchSettings`
- `LTXVImgToVideoConditionOnly`
- `LTXVChunkFeedForward`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PrimitiveFloat`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `PrimitiveBoolean`
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `easy cleanGpuUsed`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `RH_LLMAPI_Pro_Node`
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `easy int`
- `Seed (rgthree)`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CR Text`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`CFGGuider`、`KSamplerSelect`、`easy int`、`SimpleMath+`、`ModelPatchTorchSettings`、`LTXVImgToVideoConditionOnly`、`LTXVChunkFeedForward`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`easy cleanGpuUsed`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`RandomNoise`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`RH_LLMAPI_Pro_Node`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`Seed (rgthree)`、`ManualSigmas`、`SamplerCustomAdvanced`、`CR Text`、`PathchSageAttentionKJ`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、Seed (rgthree)
