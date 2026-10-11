---
key: 视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json
name: Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json
hash: a99d50599274b3c7
coverage: 0.892857
learned_at: 2026-10-11 21:19:47
nodes: [CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, BasicGuider, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MarkdownNote, RandomNoise, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, SolAttnMiniMax, ModelAttentionBackend, ResolutionSelector, VHS_VideoCombine, BasicGuider, SamplerCustomAdvanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3AudioConditioningT8, VAELoader, LoadImage, PrimitiveFloat, CR Prompt Text, MiniMaxH3AudioConditioningT8]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3横版文生视频Lantent Upscaler2_2091802068486025218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（28 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `ComfyMathExpression`
- `MarkdownNote`
- `RandomNoise`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `VAELoader`
- `LoadImage`
- `PrimitiveFloat`
- `CR Prompt Text`
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`RandomNoise`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`SolAttnMiniMax`、`ModelAttentionBackend`、`ResolutionSelector`、`VHS_VideoCombine`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3AudioConditioningT8`、`LoadImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
