---
key: 视频生成/文生视频/高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666.json
name: 高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/高质量打斗Minimax H3-self-lift双采-BF16+sage加速25步max_2098058673221361666.json
hash: ff9092abf3004c8c
coverage: 0.875
learned_at: 2026-10-15 22:49:08
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, H3SigmaRefiner, CLIPLoader, VAELoader, VAELoader, MarkdownNote, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, ComfyMathExpression, SelfLiftH3Sampler, BasicScheduler, KSamplerSelect, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, ResolutionSelector, PrimitiveFloat]
patterns: []
missing: []
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

覆盖率 **88%**（21/24）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`H3SigmaRefiner`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`ComfyMathExpression`、`SelfLiftH3Sampler`、`BasicScheduler`、`KSamplerSelect`、`LoraLoaderModelOnly`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`ResolutionSelector`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
