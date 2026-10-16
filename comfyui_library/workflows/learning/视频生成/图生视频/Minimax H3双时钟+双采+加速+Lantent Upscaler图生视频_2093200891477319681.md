---
key: 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2093200891477319681.json
name: Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2093200891477319681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2093200891477319681.json
hash: 6da7453efc00d94c
coverage: 0.8
learned_at: 2026-10-16 23:42:19
nodes: [VAELoader, UNETLoader, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, VAELoader, ComfyMathExpression, MiniMaxH3LearnedLatentUpscaleT8Advanced, BasicGuider, VHS_VideoCombine, LoraLoaderBypassModelOnly, CLIPLoader, LoadImage, LoadImage, CR Prompt Text, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, PrimitiveFloat, ResolutionSelector, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2093200891477319681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3双时钟+双采+加速+Lantent Upscaler图生视频_2093200891477319681.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（35 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
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
- `ComfyMathExpression`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `BasicGuider`
- `VHS_VideoCombine`
- `LoraLoaderBypassModelOnly` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `ResolutionSelector`
- `MarkdownNote`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`VAELoader`、`UNETLoader`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`ComfyMathExpression`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`VHS_VideoCombine`、`LoraLoaderBypassModelOnly`、`CLIPLoader`、`LoadImage`、`CR Prompt Text`、`MiniMaxH3AudioConditioningT8`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
