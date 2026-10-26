---
key: 数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json
name: 多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json
hash: e4d294d4f298f6c8
coverage: 0.763158
learned_at: 2026-10-26 02:01:28
nodes: [CLIPLoader, VAELoader, ComfyMathExpression, VAELoader, LayerUtility: PurgeVRAM V2, ConditioningZeroOut, LTXVSeparateAVLatent, ModelPreviewOverrideKJ, LTXVSeparateAVLatent, UNETLoader, ModelAttentionBackend, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, BasicScheduler, SelfLiftAvatarH3Sampler, LayerUtility: PurgeVRAM V2, KSamplerSelect, VAEDecodeAudio, PrimitiveInt, GetNode, ComfyMathExpression, CreateVideo, SetNode, MiniMaxH3ReferenceToVideo, GetNode, PrimitiveInt, SetNode, RTXVideoFrameGeneration, VAEDecode, LoadImage, LoadImage, LoadImage, ResolutionSelector, JjkText, SaveVideo, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
---

# 数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/多图参考H3_ Two-Player Brawl! Multiple Screenshots_2111978242201710593.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `VAELoader`
- `LayerUtility: PurgeVRAM V2`
- `ConditioningZeroOut`
- `LTXVSeparateAVLatent`
- `ModelPreviewOverrideKJ`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SelfLiftAvatarH3Sampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveInt`
- `GetNode`
- `ComfyMathExpression`
- `CreateVideo`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `RTXVideoFrameGeneration`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `JjkText`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveInt`

## 知识

覆盖率 **76%**（29/38）

**有卡**：`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`LayerUtility: PurgeVRAM V2`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`ModelPreviewOverrideKJ`、`UNETLoader`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`BasicScheduler`、`SelfLiftAvatarH3Sampler`、`KSamplerSelect`、`VAEDecodeAudio`、`CreateVideo`、`MiniMaxH3ReferenceToVideo`、`RTXVideoFrameGeneration`、`VAEDecode`、`LoadImage`、`ResolutionSelector`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
