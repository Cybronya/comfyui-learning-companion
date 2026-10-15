---
key: 视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json
name: Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json
hash: 1a62b86e6d7cc9ba
coverage: 0.888889
learned_at: 2026-10-15 22:46:34
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, LayerUtility: PurgeVRAM V2, H3SigmaRefiner, ComfyMathExpression, KSamplerSelect, MiniMaxChunkFeedForward, VAELoader, VAELoader, MarkdownNote, VHS_VideoCombine, MiniMaxLowVRAMAttention, BasicScheduler, SelfLiftH3Sampler, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, CLIPLoader, MiniMaxH3AudioConditioningT8, PrimitiveFloat, ResolutionSelector, LoadImage, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Other

**节点**（27 个）：
- `ConditioningZeroOut`
- `MiniMaxH3AVDecodeT8`
- `LayerUtility: PurgeVRAM V2`
- `H3SigmaRefiner`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `VAELoader`
- `MarkdownNote`
- `VHS_VideoCombine`
- `MiniMaxLowVRAMAttention`
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadImage`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`LayerUtility: PurgeVRAM V2`、`H3SigmaRefiner`、`ComfyMathExpression`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`VAELoader`、`VHS_VideoCombine`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3AudioConditioningT8`、`ResolutionSelector`、`LoadImage`、`LoadAudio`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SelfLiftH3Sampler
