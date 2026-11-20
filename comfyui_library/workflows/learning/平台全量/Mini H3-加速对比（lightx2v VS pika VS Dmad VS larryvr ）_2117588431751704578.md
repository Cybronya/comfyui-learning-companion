---
key: 平台全量/Mini H3-加速对比（lightx2v VS pika VS Dmad VS larryvr ）_2117588431751704578.json
name: Mini H3-加速对比（lightx2v VS pika VS Dmad VS larryvr ）_2117588431751704578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Mini H3-加速对比（lightx2v VS pika VS Dmad VS larryvr ）_2117588431751704578.json
hash: 7b62967cf914db61
coverage: 0.986667
learned_at: 2026-11-14 00:40:37
nodes: [LoadImage, PrimitiveFloat, CR Prompt Text, ResolutionSelector, CLIPLoader, VAELoader, VAELoader, UNETLoader, BlockSparseAttention, LoraLoaderModelOnly, MiniMaxLowVRAMAttention, ComfyMathExpression, ModelAttentionBackend, MiniMaxChunkFeedForward, ModelPreviewOverrideKJ, MiniMaxH3ReferenceToVideo, KSamplerSelect, BasicScheduler, ConditioningZeroOut, H3SigmaRefiner, SelfLiftH3Sampler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, ModelAttentionBackend, BlockSparseAttention, ModelPreviewOverrideKJ, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, KSamplerSelect, BasicScheduler, ConditioningZeroOut, H3SigmaRefiner, SelfLiftH3Sampler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, LoraLoaderModelOnly, ModelAttentionBackend, BlockSparseAttention, ModelPreviewOverrideKJ, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, KSamplerSelect, BasicScheduler, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ConditioningZeroOut, H3SigmaRefiner, SelfLiftH3Sampler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, ModelAttentionBackend, BlockSparseAttention, ModelPreviewOverrideKJ, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, KSamplerSelect, BasicScheduler, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ConditioningZeroOut, H3SigmaRefiner, SelfLiftH3Sampler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, AddLabel, AddLabel, AddLabel, AddLabel]
patterns: []
missing: []
---

# 平台全量/Mini H3-加速对比（lightx2v VS pika VS Dmad VS larryvr ）_2117588431751704578.json

> 来源文件 `comfyui_library/workflows/平台全量/Mini H3-加速对比（lightx2v VS pika VS Dmad VS larryvr ）_2117588431751704578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（75 个）：
- `LoadImage`
- `PrimitiveFloat`
- `CR Prompt Text`
- `ResolutionSelector`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `BlockSparseAttention`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxLowVRAMAttention`
- `ComfyMathExpression`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `ModelPreviewOverrideKJ`
- `MiniMaxH3ReferenceToVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `SelfLiftH3Sampler` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `ModelPreviewOverrideKJ`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `SelfLiftH3Sampler` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `ModelPreviewOverrideKJ`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `SelfLiftH3Sampler` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `ModelPreviewOverrideKJ`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ReferenceToVideo`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `SelfLiftH3Sampler` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `AddLabel`

## 知识

覆盖率 **99%**（74/75）

**有卡**：`LoadImage`、`CR Prompt Text`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`BlockSparseAttention`、`LoraLoaderModelOnly`、`MiniMaxLowVRAMAttention`、`ComfyMathExpression`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`ModelPreviewOverrideKJ`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`BasicScheduler`、`ConditioningZeroOut`、`H3SigmaRefiner`、`SelfLiftH3Sampler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`ImageConcatMulti`、`AddLabel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
