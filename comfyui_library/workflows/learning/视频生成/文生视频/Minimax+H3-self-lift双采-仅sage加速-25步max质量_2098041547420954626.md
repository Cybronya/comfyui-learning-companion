---
key: 视频生成/文生视频/Minimax+H3-self-lift双采-仅sage加速-25步max质量_2098041547420954626.json
name: Minimax+H3-self-lift双采-仅sage加速-25步max质量_2098041547420954626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax+H3-self-lift双采-仅sage加速-25步max质量_2098041547420954626.json
hash: 1c01f193f411f198
coverage: 0.8
learned_at: 2026-10-11 21:41:50
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, H3SigmaRefiner, CLIPLoader, VAELoader, VAELoader, LoadImage, MarkdownNote, PrimitiveStringMultiline, VHS_VideoCombine, UNETLoader, PrimitiveFloat, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, LayerUtility: PurgeVRAM V2, ComfyMathExpression, KSamplerSelect, SelfLiftH3Sampler, BasicScheduler, MiniMaxH3AudioConditioningT8]
patterns: []
missing: [LayerUtility: PurgeVRAM V2]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Minimax+H3-self-lift双采-仅sage加速-25步max质量_2098041547420954626.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax+H3-self-lift双采-仅sage加速-25步max质量_2098041547420954626.json`

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
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `ResolutionSelector`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LayerUtility: PurgeVRAM V2`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `SelfLiftH3Sampler` ★核心
- `BasicScheduler`
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`H3SigmaRefiner`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_VideoCombine`、`UNETLoader`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ComfyMathExpression`、`KSamplerSelect`、`SelfLiftH3Sampler`、`BasicScheduler`、`MiniMaxH3AudioConditioningT8`

**缺卡**（1）：`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SelfLiftH3Sampler

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
