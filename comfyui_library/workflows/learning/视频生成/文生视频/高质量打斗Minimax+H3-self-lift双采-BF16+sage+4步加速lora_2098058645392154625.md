---
key: 视频生成/文生视频/高质量打斗Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098058645392154625.json
name: 高质量打斗Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098058645392154625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高质量打斗Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098058645392154625.json
hash: 2d89894d86c1b2f9
coverage: 0.851852
learned_at: 2026-10-11 21:42:03
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, LayerUtility: PurgeVRAM V2, H3SigmaRefiner, CLIPLoader, ComfyMathExpression, KSamplerSelect, VAELoader, VAELoader, MarkdownNote, VHS_VideoCombine, BasicScheduler, SelfLiftH3Sampler, MiniMaxLowVRAMAttention, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxChunkFeedForward, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: [LayerUtility: PurgeVRAM V2]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/高质量打斗Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098058645392154625.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高质量打斗Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098058645392154625.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（27 个）：
- `ConditioningZeroOut`
- `MiniMaxH3AVDecodeT8`
- `LayerUtility: PurgeVRAM V2`
- `H3SigmaRefiner`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `VAELoader`
- `VAELoader`
- `MarkdownNote`
- `VHS_VideoCombine`
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `MiniMaxLowVRAMAttention`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`H3SigmaRefiner`、`CLIPLoader`、`ComfyMathExpression`、`KSamplerSelect`、`VAELoader`、`VHS_VideoCombine`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxLowVRAMAttention`、`UNETLoader`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxChunkFeedForward`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`ResolutionSelector`

**缺卡**（1）：`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
