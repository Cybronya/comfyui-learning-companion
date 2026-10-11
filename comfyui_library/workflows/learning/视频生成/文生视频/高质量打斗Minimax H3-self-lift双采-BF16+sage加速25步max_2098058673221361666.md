---
key: 视频生成/文生视频/高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666.json
name: 高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666.json
hash: ff9092abf3004c8c
coverage: 0.833333
learned_at: 2026-10-11 21:42:03
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, H3SigmaRefiner, CLIPLoader, VAELoader, VAELoader, MarkdownNote, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, ComfyMathExpression, SelfLiftH3Sampler, BasicScheduler, KSamplerSelect, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, ResolutionSelector, PrimitiveFloat]
patterns: []
missing: [LayerUtility: PurgeVRAM V2]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（24 个）：
- `ConditioningZeroOut`
- `MiniMaxH3AVDecodeT8`
- `H3SigmaRefiner`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `ComfyMathExpression`
- `SelfLiftH3Sampler` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveFloat`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`H3SigmaRefiner`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`、`ComfyMathExpression`、`SelfLiftH3Sampler`、`BasicScheduler`、`KSamplerSelect`、`LoraLoaderModelOnly`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`ResolutionSelector`

**缺卡**（1）：`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
