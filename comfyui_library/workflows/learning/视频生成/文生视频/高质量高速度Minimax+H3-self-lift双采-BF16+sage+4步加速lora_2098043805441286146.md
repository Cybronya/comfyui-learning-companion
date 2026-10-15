---
key: 视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098043805441286146.json
name: 高质量高速度Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098043805441286146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098043805441286146.json
hash: 8b947c2b69862952
coverage: 0.869565
learned_at: 2026-10-15 22:49:09
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, LayerUtility: PurgeVRAM V2, H3SigmaRefiner, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxChunkFeedForward, VAELoader, VAELoader, LoraLoaderModelOnly, LoadImage, MarkdownNote, PrimitiveStringMultiline, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, SelfLiftH3Sampler, ResolutionSelector, PrimitiveFloat, UNETLoader, MiniMaxLowVRAMAttention, MiniMaxH3AudioConditioningT8]
patterns: []
missing: []
---

# 视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098043805441286146.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高质量高速度Minimax+H3-self-lift双采-BF16+sage+4步加速lora_2098043805441286146.json`

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
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `MiniMaxLowVRAMAttention`
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`LayerUtility: PurgeVRAM V2`、`H3SigmaRefiner`、`CLIPLoader`、`ComfyMathExpression`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImage`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`SelfLiftH3Sampler`、`ResolutionSelector`、`UNETLoader`、`MiniMaxLowVRAMAttention`、`MiniMaxH3AudioConditioningT8`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
