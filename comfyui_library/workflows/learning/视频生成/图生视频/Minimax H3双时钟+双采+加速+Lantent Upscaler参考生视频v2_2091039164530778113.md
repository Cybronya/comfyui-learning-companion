---
key: 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113.json
name: Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113.json
hash: 82ff84e044563c2f
coverage: 0.8
learned_at: 2026-10-16 22:30:40
nodes: [CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, BasicGuider, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3AVDecodeT8, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, MiniMaxH3AudioConditioningT8, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, SolAttnMiniMax, ModelAttentionBackend, ResolutionSelector, BasicGuider, SamplerCustomAdvanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, CR Prompt Text, PrimitiveFloat, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, RandomNoise, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091039164530778113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（35 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `MarkdownNote`
- `MiniMaxH3AudioConditioningT8`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `CR Prompt Text`
- `PrimitiveFloat`
- `MiniMaxH3AudioConditioningT8`
- `VHS_VideoCombine`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`SolAttnMiniMax`、`ModelAttentionBackend`、`ResolutionSelector`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`CR Prompt Text`、`VHS_VideoCombine`、`RandomNoise`、`LoadImage`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
