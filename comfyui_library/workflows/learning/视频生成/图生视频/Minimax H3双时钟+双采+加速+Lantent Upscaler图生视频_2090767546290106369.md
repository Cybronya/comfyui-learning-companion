---
key: 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090767546290106369.json
name: Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090767546290106369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090767546290106369.json
hash: b110d0bb16fb1521
coverage: 0.787879
learned_at: 2026-10-16 22:30:40
nodes: [CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, ComfyMathExpression, MarkdownNote, ResolutionSelector, MiniMaxH3TwoPassDetailMixerT8Advanced, PrimitiveFloat, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, SolAttnMiniMax, ModelAttentionBackend, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, RandomNoise, CR Prompt Text, BasicGuider, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3LearnedLatentUpscaleT8Advanced]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090767546290106369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090767546290106369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（33 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `ComfyMathExpression`
- `MarkdownNote`
- `ResolutionSelector`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `PrimitiveFloat`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AudioConditioningT8`
- `VHS_VideoCombine`
- `RandomNoise`
- `CR Prompt Text`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`LoadImage`、`ComfyMathExpression`、`ResolutionSelector`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`SolAttnMiniMax`、`ModelAttentionBackend`、`MiniMaxH3AudioConditioningT8`、`VHS_VideoCombine`、`RandomNoise`、`CR Prompt Text`、`BasicGuider`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
