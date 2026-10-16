---
key: 视频生成/图生视频/Minimax H3横版文生视频Lantent Upscaler2_2091776496015863809.json
name: Minimax H3横版文生视频Lantent Upscaler2_2091776496015863809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3横版文生视频Lantent Upscaler2_2091776496015863809.json
hash: d8d3f714b110bbcd
coverage: 0.928571
learned_at: 2026-10-16 22:30:40
nodes: [CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, BasicGuider, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3AVDecodeT8, ComfyMathExpression, MarkdownNote, MiniMaxH3AudioConditioningT8, RandomNoise, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, SolAttnMiniMax, ModelAttentionBackend, ResolutionSelector, VHS_VideoCombine, BasicGuider, SamplerCustomAdvanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3AudioConditioningT8, VAELoader, CR Prompt Text, LoadImage, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3横版文生视频Lantent Upscaler2_2091776496015863809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3横版文生视频Lantent Upscaler2_2091776496015863809.json`

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
- `MiniMaxH3AudioConditioningT8`
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
- `CR Prompt Text`
- `LoadImage`
- `PrimitiveFloat`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`RandomNoise`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`SolAttnMiniMax`、`ModelAttentionBackend`、`ResolutionSelector`、`VHS_VideoCombine`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`CR Prompt Text`、`LoadImage`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
