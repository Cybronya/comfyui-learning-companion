---
key: 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441.json
name: Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441.json
hash: 74a0a9100fbf6e3c
coverage: 0.787879
learned_at: 2026-10-16 22:30:40
nodes: [CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, BasicGuider, SamplerCustomAdvanced, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AVDecodeT8, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, MiniMaxH3TwoPassDetailMixerT8Advanced, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, SolAttnMiniMax, ModelAttentionBackend, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, RandomNoise, SamplerCustomAdvanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, MiniMaxH3TwoPassLatentReconcileT8Advanced, ResolutionSelector, PrimitiveFloat, CR Prompt Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频V2_2090981502527037441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（33 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3AVDecodeT8`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `MarkdownNote`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
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
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ResolutionSelector`
- `PrimitiveFloat`
- `CR Prompt Text`
- `LoadImage`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`BasicGuider`、`SamplerCustomAdvanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3AVDecodeT8`、`ComfyMathExpression`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`SolAttnMiniMax`、`ModelAttentionBackend`、`MiniMaxH3AudioConditioningT8`、`VHS_VideoCombine`、`RandomNoise`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`ResolutionSelector`、`CR Prompt Text`、`LoadImage`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
