---
key: 视频生成/图生视频/(10Eros Beta3)Minimax H3+加速+Lantent Upscaler参考生视频_2092293690407608321.json
name: (10Eros Beta3)Minimax H3+加速+Lantent Upscaler参考生视频_2092293690407608321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(10Eros Beta3)Minimax H3+加速+Lantent Upscaler参考生视频_2092293690407608321.json
hash: 9c7916e7515c274f
coverage: 0.829268
learned_at: 2026-10-16 22:58:48
nodes: [MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, SolAttnMiniMax, ModelAttentionBackend, BasicGuider, ResolutionSelector, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3TwoPassDetailMixerT8Advanced, VAELoader, CLIPLoader, SamplerCustomAdvanced, CR Prompt Text, MiniMaxH3AVDecodeT8, VHS_VideoCombine, UNETLoader, LoraLoaderBypassModelOnly, MiniMaxH3AudioConditioningT8]
patterns: []
missing: []
---

# 视频生成/图生视频/(10Eros Beta3)Minimax H3+加速+Lantent Upscaler参考生视频_2092293690407608321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(10Eros Beta3)Minimax H3+加速+Lantent Upscaler参考生视频_2092293690407608321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（41 个）：
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `MarkdownNote`
- `VAELoader`
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `BasicGuider`
- `ResolutionSelector`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `VAELoader`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `CR Prompt Text`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3AudioConditioningT8`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`MiniMaxH3DualClockSamplerT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`BasicGuider`、`ResolutionSelector`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RandomNoise`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`CLIPLoader`、`CR Prompt Text`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderBypassModelOnly`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
