---
key: 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090280306870931457.json
name: Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090280306870931457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090280306870931457.json
hash: 4ab13fb998873a96
coverage: 0.794118
learned_at: 2026-10-16 22:02:08
nodes: [VAELoader, UNETLoader, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, VAELoader, ResolutionSelector, MarkdownNote, PrimitiveFloat, ComfyMathExpression, CLIPLoader, MiniMaxH3LearnedLatentUpscaleT8Advanced, BasicGuider, VHS_VideoCombine, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3AudioConditioningT8, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090280306870931457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2090280306870931457.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（34 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `VAELoader`
- `ResolutionSelector`
- `MarkdownNote`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `CLIPLoader`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `BasicGuider`
- `VHS_VideoCombine`
- `LoadImage`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AudioConditioningT8`
- `CR Prompt Text`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`VAELoader`、`UNETLoader`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`ResolutionSelector`、`ComfyMathExpression`、`CLIPLoader`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`VHS_VideoCombine`、`LoadImage`、`LoraLoaderBypassModelOnly`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
