---
key: 视频生成/图生视频/LTX 2.3+PromptRelay 三图参考_2040053495893598209.json
name: LTX 2.3+PromptRelay 三图参考_2040053495893598209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2040053495893598209.json
hash: 1287d0f95069aedd
coverage: 0.755556
learned_at: 2026-10-15 22:36:13
nodes: [SetNode, GetNode, GetNode, ImageResizeKJv2, VAELoaderKJ, SetNode, DualCLIPLoader, KSamplerSelect, LTXVConcatAVLatent, RandomNoise, CFGGuider, ManualSigmas, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVAudioVAEDecode, VAELoaderKJ, UNETLoader, GetNode, EmptyLTXVLatentVideo, ImageResizeKJv2, MathExpression|pysssss, CLIPTextEncode, LTXVConditioning, Reroute, MathExpression|pysssss, MathExpression|pysssss, SamplerCustomAdvanced, GetImageRangeFromBatch, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, PrimitiveNode, PromptRelayEncodeTimeline, LTXVAddGuideMulti, PrimitiveInt, LTX2_NAG, VHS_VideoCombine, LoadImage, ImageResizeKJv2, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 465}
---

# 视频生成/图生视频/LTX 2.3+PromptRelay 三图参考_2040053495893598209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040053495893598209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（45 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `GetNode`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `Reroute`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SamplerCustomAdvanced` ★核心
- `GetImageRangeFromBatch`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`
- `PromptRelayEncodeTimeline`
- `LTXVAddGuideMulti`
- `PrimitiveInt`
- `LTX2_NAG`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `465`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`ImageResizeKJv2`、`VAELoaderKJ`、`DualCLIPLoader`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`UNETLoader`、`EmptyLTXVLatentVideo`、`MathExpression|pysssss`、`CLIPTextEncode`、`LTXVConditioning`、`SamplerCustomAdvanced`、`GetImageRangeFromBatch`、`LoadImage`、`PromptRelayEncodeTimeline`、`LTXVAddGuideMulti`、`LTX2_NAG`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
