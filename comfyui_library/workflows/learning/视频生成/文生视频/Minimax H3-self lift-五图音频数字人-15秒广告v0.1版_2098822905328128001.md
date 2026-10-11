---
key: 视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json
name: Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3-self lift-五图音频数字人-15秒广告v0.1版_2098822905328128001.json
hash: 1a62b86e6d7cc9ba
coverage: 0.851852
learned_at: 2026-10-11 21:41:49
nodes: [ConditioningZeroOut, MiniMaxH3AVDecodeT8, LayerUtility: PurgeVRAM V2, H3SigmaRefiner, ComfyMathExpression, KSamplerSelect, MiniMaxChunkFeedForward, VAELoader, VAELoader, MarkdownNote, VHS_VideoCombine, MiniMaxLowVRAMAttention, BasicScheduler, SelfLiftH3Sampler, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, CLIPLoader, MiniMaxH3AudioConditioningT8, PrimitiveFloat, ResolutionSelector, LoadImage, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: [LayerUtility: PurgeVRAM V2]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
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

覆盖率 **85%**（23/27）

**有卡**：`ConditioningZeroOut`、`MiniMaxH3AVDecodeT8`、`H3SigmaRefiner`、`ComfyMathExpression`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`VAELoader`、`VHS_VideoCombine`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3AudioConditioningT8`、`ResolutionSelector`、`LoadImage`、`LoadAudio`

**缺卡**（1）：`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SelfLiftH3Sampler

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
