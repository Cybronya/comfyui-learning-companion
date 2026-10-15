---
key: 视频生成/文生视频/LTX2.3+PromptRelay+四图参考_2056629366276321282.json
name: LTX2.3+PromptRelay+四图参考_2056629366276321282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3+PromptRelay+四图参考_2056629366276321282.json
hash: b818d4f5625837b1
coverage: 0.765957
learned_at: 2026-10-15 22:45:01
nodes: [SetNode, GetNode, GetNode, VAELoaderKJ, SetNode, DualCLIPLoader, LTXVConcatAVLatent, RandomNoise, CFGGuider, ManualSigmas, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVAudioVAEDecode, VAELoaderKJ, UNETLoader, GetNode, EmptyLTXVLatentVideo, MathExpression|pysssss, CLIPTextEncode, LTXVConditioning, MathExpression|pysssss, PrimitiveInt, LTX2_NAG, PathchSageAttentionKJ, MathExpression|pysssss, LoadImage, LoadImage, Reroute, LoraLoaderModelOnly, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, PrimitiveInt, PrimitiveInt, LTXVAddGuideMulti, PromptRelayEncodeTimeline, SamplerCustomAdvanced, LTXVEmptyLatentAudio, LoadImage, PrimitiveNode, LoadImage, LoraLoaderModelOnly, ImageResizeKJv2, KSamplerSelect, GetImageRangeFromBatch, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 361}
---

# 视频生成/文生视频/LTX2.3+PromptRelay+四图参考_2056629366276321282.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3+PromptRelay+四图参考_2056629366276321282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `SetNode`
- `DualCLIPLoader`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `GetNode`
- `EmptyLTXVLatentVideo`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `LTX2_NAG`
- `PathchSageAttentionKJ`
- `MathExpression|pysssss`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVAddGuideMulti`
- `PromptRelayEncodeTimeline`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LoadImage`
- `PrimitiveNode`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `KSamplerSelect` ★核心
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（36/47）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`UNETLoader`、`EmptyLTXVLatentVideo`、`MathExpression|pysssss`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`PathchSageAttentionKJ`、`LoadImage`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`LTXVAddGuideMulti`、`PromptRelayEncodeTimeline`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`KSamplerSelect`、`GetImageRangeFromBatch`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
