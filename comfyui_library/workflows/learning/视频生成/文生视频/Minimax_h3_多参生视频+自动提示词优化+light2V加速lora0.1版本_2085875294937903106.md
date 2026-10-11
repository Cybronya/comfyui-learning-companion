---
key: 视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085875294937903106.json
name: Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085875294937903106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085875294937903106.json
hash: 01abb1b7da95190a
coverage: 0.813953
learned_at: 2026-10-11 20:53:46
nodes: [LoadAudio, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, VHS_VideoCombine, UNETLoader, RandomNoise, VAELoader, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, LoraLoaderBypassModelOnly, EasyCache, PathchSageAttentionKJ, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, GetImageRangeFromBatch, LoadImage, MarkdownNote, ComfyMathExpression, MiniMaxH3MultiRateSamplerEXPT8, easy showAnything, StringFunction|pysssss, StringFunction|pysssss, ResolutionSelector, PrimitiveFloat, RHLLMChatNode, PrimitiveStringMultiline, easy showAnything, ImageResizeKJv2, CreateVideo, LoadAudio, LoadAudio, VHS_LoadVideo, MiniMaxH3ReferenceToVideo, easy clearCacheAll, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly]
patterns: []
missing: [StringFunction|pysssss, StringFunction|pysssss, easy clearCacheAll]
discoveries: [次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085875294937903106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085875294937903106.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Other

**节点**（43 个）：
- `LoadAudio`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `RandomNoise`
- `VAELoader`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `LoraLoaderBypassModelOnly` ★核心
- `EasyCache`
- `PathchSageAttentionKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetImageRangeFromBatch`
- `LoadImage`
- `MarkdownNote`
- `ComfyMathExpression`
- `MiniMaxH3MultiRateSamplerEXPT8` ★核心
- `easy showAnything`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `ResolutionSelector`
- `PrimitiveFloat`
- `RHLLMChatNode`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `ImageResizeKJv2`
- `CreateVideo`
- `LoadAudio`
- `LoadAudio`
- `VHS_LoadVideo`
- `MiniMaxH3ReferenceToVideo`
- `easy clearCacheAll`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **81%**（35/43）

**有卡**：`LoadAudio`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_VideoCombine`、`UNETLoader`、`RandomNoise`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`LoraLoaderBypassModelOnly`、`EasyCache`、`PathchSageAttentionKJ`、`GetImageRangeFromBatch`、`ComfyMathExpression`、`MiniMaxH3MultiRateSamplerEXPT8`、`ResolutionSelector`、`RHLLMChatNode`、`ImageResizeKJv2`、`CreateVideo`、`VHS_LoadVideo`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`

**缺卡**（3）：`StringFunction|pysssss`、`StringFunction|pysssss`、`easy clearCacheAll`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3MultiRateSamplerEXPT8

## 学习发现

- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
