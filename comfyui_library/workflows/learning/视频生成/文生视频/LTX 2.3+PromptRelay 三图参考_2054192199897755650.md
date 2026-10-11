---
key: 视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json
name: LTX 2.3+PromptRelay 三图参考_2054192199897755650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json
hash: 189771a6356d736d
coverage: 0.702128
learned_at: 2026-10-11 19:49:35
nodes: [SetNode, GetNode, GetNode, VAELoaderKJ, SetNode, DualCLIPLoader, KSamplerSelect, LTXVConcatAVLatent, RandomNoise, CFGGuider, ManualSigmas, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVAudioVAEDecode, VAELoaderKJ, UNETLoader, GetNode, EmptyLTXVLatentVideo, MathExpression|pysssss, CLIPTextEncode, LTXVConditioning, Reroute, MathExpression|pysssss, SamplerCustomAdvanced, GetImageRangeFromBatch, PrimitiveInt, LTX2_NAG, VHS_VideoCombine, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, PrimitiveNode, LoadImage, LoadImage, LoadImage, PromptRelayEncodeTimeline, PrimitiveInt, PrimitiveInt, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, MathExpression|pysssss, LTXVAddGuideMulti]
patterns: []
missing: [MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss]
parameters: {"batch_size": 1, "height": 24, "width": 361}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3+PromptRelay 三图参考_2054192199897755650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `SetNode`
- `GetNode`
- `GetNode`
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
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `Reroute`
- `MathExpression|pysssss`
- `SamplerCustomAdvanced` ★核心
- `GetImageRangeFromBatch`
- `PrimitiveInt`
- `LTX2_NAG`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PrimitiveNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PromptRelayEncodeTimeline`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `361`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（33/47）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`UNETLoader`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`SamplerCustomAdvanced`、`GetImageRangeFromBatch`、`LTX2_NAG`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LoadImage`、`PromptRelayEncodeTimeline`、`ImageResizeKJv2`、`LTXVAddGuideMulti`

**缺卡**（3）：`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
