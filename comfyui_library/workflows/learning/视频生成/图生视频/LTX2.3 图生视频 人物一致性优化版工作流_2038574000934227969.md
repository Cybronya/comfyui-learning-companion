---
key: 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版工作流_2038574000934227969.json
name: LTX2.3 图生视频 人物一致性优化版工作流_2038574000934227969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038574000934227969.json
hash: c469e1ddaab9ac47
coverage: 0.974359
learned_at: 2026-10-15 22:36:03
nodes: [CFGGuider, KSamplerSelect, CLIPTextEncode, easy int, CheckpointLoaderSimple, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, LTXAVTextEncoderLoader, CR Text, SimpleMath+, ModelPatchTorchSettings, LTXVImgToVideoConditionOnly, LTXVChunkFeedForward, LTXVPreprocess, DapaoImageAspectRatioResizeNode, EmptyLTXVLatentVideo, CLIPTextEncode, LTXVConditioning, PrimitiveFloat, CM_FloatToInt, LTXVEmptyLatentAudio, PrimitiveBoolean, LTXVConcatAVLatent, LTXVAudioVAELoader, easy cleanGpuUsed, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, SamplerCustomAdvanced, RandomNoise, Seed (rgthree), RH_LLMAPI_Pro_Node, easy int, easy int, VHS_VideoCombine, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版工作流_2038574000934227969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038574000934227969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（39 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `CR Text`
- `SimpleMath+`
- `ModelPatchTorchSettings`
- `LTXVImgToVideoConditionOnly`
- `LTXVChunkFeedForward`
- `LTXVPreprocess`
- `DapaoImageAspectRatioResizeNode`
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
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Seed (rgthree)`
- `RH_LLMAPI_Pro_Node`
- `easy int`
- `easy int`
- `VHS_VideoCombine`
- `CR Text`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`easy int`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXAVTextEncoderLoader`、`CR Text`、`SimpleMath+`、`ModelPatchTorchSettings`、`LTXVImgToVideoConditionOnly`、`LTXVChunkFeedForward`、`LTXVPreprocess`、`DapaoImageAspectRatioResizeNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`easy cleanGpuUsed`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`Seed (rgthree)`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、Seed (rgthree)
