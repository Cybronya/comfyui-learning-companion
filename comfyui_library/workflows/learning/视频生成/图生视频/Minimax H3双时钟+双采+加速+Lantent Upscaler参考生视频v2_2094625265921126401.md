---
key: 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401.json
name: Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401.json
hash: 8bff31beb15b2584
coverage: 0.787879
learned_at: 2026-10-17 00:02:30
nodes: [CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, BasicGuider, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3AVDecodeT8, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, MiniMaxH3AudioConditioningT8, RandomNoise, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, SolAttnMiniMax, ModelAttentionBackend, CR Prompt Text, VHS_VideoCombine, BasicGuider, SamplerCustomAdvanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3AudioConditioningT8, LoadImage, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2094625265921126401.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（33 个）：
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
- `RandomNoise`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`RandomNoise`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`SolAttnMiniMax`、`ModelAttentionBackend`、`CR Prompt Text`、`VHS_VideoCombine`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`LoadImage`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
