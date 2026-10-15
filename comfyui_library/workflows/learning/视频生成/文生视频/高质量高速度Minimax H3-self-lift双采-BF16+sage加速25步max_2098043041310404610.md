---
key: 视频生成/文生视频/高质量高速度Minimax H3-self-lift双采-BF16+sage加速25步max_2098043041310404610.json
name: 高质量高速度Minimax H3-self-lift双采-BF16+sage加速25步max_2098043041310404610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高质量高速度Minimax H3-self-lift双采-BF16+sage加速25步max_2098043041310404610.json
hash: 68d5b3b8875ce54b
coverage: 0.85
learned_at: 2026-10-15 22:49:09
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, H3SigmaRefiner, CLIPLoader, VAELoader, VAELoader, LoadImage, MarkdownNote, PrimitiveStringMultiline, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, LayerUtility: PurgeVRAM V2, ComfyMathExpression, SelfLiftH3Sampler, UNETLoader, ResolutionSelector, PrimitiveFloat, BasicScheduler, KSamplerSelect, MiniMaxH3AudioConditioningT8]
patterns: []
missing: []
---

# 视频生成/文生视频/高质量高速度Minimax H3-self-lift双采-BF16+sage加速25步max_2098043041310404610.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高质量高速度Minimax H3-self-lift双采-BF16+sage加速25步max_2098043041310404610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（20 个）：
- `ConditioningZeroOut`
- `MiniMaxH3AVDecodeT8`
- `H3SigmaRefiner`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LayerUtility: PurgeVRAM V2`
- `ComfyMathExpression`
- `SelfLiftH3Sampler` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`H3SigmaRefiner`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LayerUtility: PurgeVRAM V2`、`ComfyMathExpression`、`SelfLiftH3Sampler`、`UNETLoader`、`ResolutionSelector`、`BasicScheduler`、`KSamplerSelect`、`MiniMaxH3AudioConditioningT8`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SelfLiftH3Sampler
