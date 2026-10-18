---
key: 视频生成/图生视频/aidir-LTX2.3 首帧图生视频 人物一致性优化版💃_2069596918434590721.json
name: aidir-LTX2.3 首帧图生视频 人物一致性优化版💃_2069596918434590721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/aidir-LTX2.3 首帧图生视频 人物一致性优化版💃_2069596918434590721.json
hash: 05ab90173baecd1f
coverage: 0.95122
learned_at: 2026-10-15 22:40:30
nodes: [CFGGuider, KSamplerSelect, CLIPTextEncode, easy int, easy int, easy int, CheckpointLoaderSimple, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, LTXAVTextEncoderLoader, CR Text, SimpleMath+, ModelPatchTorchSettings, LTXVImgToVideoConditionOnly, LTXVChunkFeedForward, LTXVPreprocess, DapaoImageAspectRatioResizeNode, EmptyLTXVLatentVideo, CLIPTextEncode, LTXVConditioning, PrimitiveFloat, CM_FloatToInt, LTXVEmptyLatentAudio, PrimitiveBoolean, LTXVConcatAVLatent, LTXVAudioVAELoader, easy cleanGpuUsed, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, ManualSigmas, SamplerCustomAdvanced, RandomNoise, Seed (rgthree), VHS_VideoCombine, Note Plus (mtb), MarkdownNote, RH_LLMAPI_Pro_Node, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/aidir-LTX2.3 首帧图生视频 人物一致性优化版💃_2069596918434590721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069596918434590721.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（41 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `easy int`
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
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `MarkdownNote`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`CFGGuider`、`KSamplerSelect`、`CLIPTextEncode`、`easy int`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LTXAVTextEncoderLoader`、`CR Text`、`SimpleMath+`、`ModelPatchTorchSettings`、`LTXVImgToVideoConditionOnly`、`LTXVChunkFeedForward`、`LTXVPreprocess`、`DapaoImageAspectRatioResizeNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`easy cleanGpuUsed`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`Seed (rgthree)`、`VHS_VideoCombine`、`Note Plus (mtb)`、`RH_LLMAPI_Pro_Node`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、Seed (rgthree)
