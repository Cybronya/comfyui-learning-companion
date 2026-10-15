---
key: 视频生成/文生视频/LTX2.3+图生视频 提示词自动优化版 数字人说话唱歌_2063795562855624705.json
name: LTX2.3+图生视频 提示词自动优化版 数字人说话唱歌_2063795562855624705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3+图生视频 提示词自动优化版 数字人说话唱歌_2063795562855624705.json
hash: eab402991288be5d
coverage: 0.952381
learned_at: 2026-10-15 22:45:02
nodes: [CFGGuider, KSamplerSelect, easy int, easy int, easy int, SimpleMath+, ModelPatchTorchSettings, LTXVImgToVideoConditionOnly, LTXVChunkFeedForward, LTXVPreprocess, EmptyLTXVLatentVideo, CLIPTextEncode, LTXVConditioning, PrimitiveFloat, CM_FloatToInt, LTXVEmptyLatentAudio, PrimitiveBoolean, LTXVConcatAVLatent, LTXVAudioVAELoader, easy cleanGpuUsed, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, Seed (rgthree), ManualSigmas, CR Text, CheckpointLoaderSimple, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, CR Text, CLIPTextEncode, LoraLoaderModelOnly, LTXAVTextEncoderLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, DapaoImageAspectRatioResizeNode, VHS_VideoCombine, Note, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3+图生视频 提示词自动优化版 数字人说话唱歌_2063795562855624705.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3+图生视频 提示词自动优化版 数字人说话唱歌_2063795562855624705.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `easy int`
- `easy int`
- `easy int`
- `SimpleMath+`
- `ModelPatchTorchSettings`
- `LTXVImgToVideoConditionOnly`
- `LTXVChunkFeedForward`
- `LTXVPreprocess`
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
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Seed (rgthree)`
- `ManualSigmas`
- `CR Text`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DapaoImageAspectRatioResizeNode`
- `VHS_VideoCombine`
- `Note`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **95%**（40/42）

**有卡**：`CFGGuider`、`KSamplerSelect`、`easy int`、`SimpleMath+`、`ModelPatchTorchSettings`、`LTXVImgToVideoConditionOnly`、`LTXVChunkFeedForward`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`easy cleanGpuUsed`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`RandomNoise`、`Seed (rgthree)`、`ManualSigmas`、`CR Text`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`RH_LLMAPI_Pro_Node`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`DapaoImageAspectRatioResizeNode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、Seed (rgthree)
