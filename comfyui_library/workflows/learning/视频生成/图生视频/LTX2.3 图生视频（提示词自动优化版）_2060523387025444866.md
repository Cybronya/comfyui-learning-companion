---
key: 视频生成/图生视频/LTX2.3 图生视频（提示词自动优化版）_2060523387025444866.json
name: LTX2.3 图生视频（提示词自动优化版）_2060523387025444866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 图生视频（提示词自动优化版）_2060523387025444866.json
hash: d9762bbdd630c987
coverage: 0.95122
learned_at: 2026-10-15 22:38:48
nodes: [CFGGuider, KSamplerSelect, ModelPatchTorchSettings, LTXVImgToVideoConditionOnly, LTXVChunkFeedForward, LTXVPreprocess, CLIPTextEncode, LTXVConditioning, PrimitiveFloat, CM_FloatToInt, PrimitiveBoolean, LTXVConcatAVLatent, LTXVAudioVAELoader, easy cleanGpuUsed, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, RandomNoise, ManualSigmas, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, LTXAVTextEncoderLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, VHS_VideoCombine, Note, Seed (rgthree), LoraLoaderModelOnly, DapaoImageAspectRatioResizeNode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LoadImage, CR Text, CR Text, easy int, easy int, easy int, RH_LLMAPI_Pro_Node, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 图生视频（提示词自动优化版）_2060523387025444866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060523387025444866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（41 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ModelPatchTorchSettings`
- `LTXVImgToVideoConditionOnly`
- `LTXVChunkFeedForward`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PrimitiveFloat`
- `CM_FloatToInt`
- `PrimitiveBoolean`
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `easy cleanGpuUsed`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `Note`
- `Seed (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `DapaoImageAspectRatioResizeNode`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `CR Text`
- `CR Text`
- `easy int`
- `easy int`
- `easy int`
- `RH_LLMAPI_Pro_Node`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`CFGGuider`、`KSamplerSelect`、`ModelPatchTorchSettings`、`LTXVImgToVideoConditionOnly`、`LTXVChunkFeedForward`、`LTXVPreprocess`、`CLIPTextEncode`、`LTXVConditioning`、`CM_FloatToInt`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`easy cleanGpuUsed`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`RandomNoise`、`ManualSigmas`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`Seed (rgthree)`、`DapaoImageAspectRatioResizeNode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LoadImage`、`CR Text`、`easy int`、`RH_LLMAPI_Pro_Node`、`SamplerCustomAdvanced`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、Seed (rgthree)
