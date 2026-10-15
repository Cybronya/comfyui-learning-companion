---
key: 视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+8步加速lora_2098043798923333634.json
name: 高质量高速度Minimax+H3-self-lift双采-BF16+sage+8步加速lora_2098043798923333634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+8步加速lora_2098043798923333634.json
hash: 7425637c4a0c80d5
coverage: 0.869565
learned_at: 2026-10-15 22:49:09
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, LayerUtility: PurgeVRAM V2, H3SigmaRefiner, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxChunkFeedForward, VAELoader, VAELoader, LoadImage, MarkdownNote, PrimitiveStringMultiline, VHS_VideoCombine, BasicScheduler, SelfLiftH3Sampler, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, ResolutionSelector, UNETLoader, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8]
patterns: []
missing: []
---

# 视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+8步加速lora_2098043798923333634.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+8步加速lora_2098043798923333634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（23 个）：
- `ConditioningZeroOut`
- `MiniMaxH3AVDecodeT8`
- `LayerUtility: PurgeVRAM V2`
- `H3SigmaRefiner`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`LayerUtility: PurgeVRAM V2`、`H3SigmaRefiner`、`CLIPLoader`、`ComfyMathExpression`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`VAELoader`、`LoadImage`、`VHS_VideoCombine`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ResolutionSelector`、`UNETLoader`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`MiniMaxH3AudioConditioningT8`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
