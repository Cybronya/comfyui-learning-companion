---
key: 视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085894326038650882.json
name: Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085894326038650882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085894326038650882.json
hash: e6f3d331592a5d90
coverage: 0.883721
learned_at: 2026-10-15 22:46:47
nodes: [LoadAudio, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, UNETLoader, RandomNoise, VAELoader, BasicGuider, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, LoraLoaderBypassModelOnly, EasyCache, PathchSageAttentionKJ, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, GetImageRangeFromBatch, LoadImage, MarkdownNote, ComfyMathExpression, MiniMaxH3MultiRateSamplerEXPT8, easy showAnything, StringFunction|pysssss, StringFunction|pysssss, ResolutionSelector, PrimitiveFloat, RHLLMChatNode, PrimitiveStringMultiline, ImageResizeKJv2, CreateVideo, LoadAudio, LoadAudio, VHS_LoadVideo, MiniMaxH3ReferenceToVideo, easy clearCacheAll, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, easy showAnything, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085894326038650882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax_h3_多参生视频+自动提示词优化+light2V加速lora0.1版本_2085894326038650882.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Other

**节点**（43 个）：
- `LoadAudio`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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
- `ImageResizeKJv2`
- `CreateVideo`
- `LoadAudio`
- `LoadAudio`
- `VHS_LoadVideo`
- `MiniMaxH3ReferenceToVideo`
- `easy clearCacheAll`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `VHS_VideoCombine`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`LoadAudio`、`CLIPLoader`、`VAELoader`、`LoadImage`、`UNETLoader`、`RandomNoise`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`LoraLoaderBypassModelOnly`、`EasyCache`、`PathchSageAttentionKJ`、`GetImageRangeFromBatch`、`ComfyMathExpression`、`MiniMaxH3MultiRateSamplerEXPT8`、`StringFunction|pysssss`、`ResolutionSelector`、`RHLLMChatNode`、`ImageResizeKJv2`、`CreateVideo`、`VHS_LoadVideo`、`MiniMaxH3ReferenceToVideo`、`easy clearCacheAll`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3MultiRateSamplerEXPT8
