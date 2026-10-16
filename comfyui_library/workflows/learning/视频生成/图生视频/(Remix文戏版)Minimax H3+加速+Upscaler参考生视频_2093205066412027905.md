---
key: 视频生成/图生视频/(Remix文戏版)Minimax H3+加速+Upscaler参考生视频_2093205066412027905.json
name: (Remix文戏版)Minimax H3+加速+Upscaler参考生视频_2093205066412027905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Remix文戏版)Minimax H3+加速+Upscaler参考生视频_2093205066412027905.json
hash: 145c2383784c3432
coverage: 0.833333
learned_at: 2026-10-16 23:41:51
nodes: [SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, SolAttnMiniMax, ModelAttentionBackend, BasicGuider, ResolutionSelector, MiniMaxH3LearnedLatentUpscaleT8Advanced, PrimitiveFloat, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3TwoPassDetailMixerT8Advanced, CLIPLoader, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3AudioConditioningT8, CR Prompt Text, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, RandomNoise, MiniMaxH3DualClockSamplerT8, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/(Remix文戏版)Minimax H3+加速+Upscaler参考生视频_2093205066412027905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Remix文戏版)Minimax H3+加速+Upscaler参考生视频_2093205066412027905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（42 个）：
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
- `PrimitiveFloat`
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
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `MiniMaxH3AudioConditioningT8`
- `CR Prompt Text`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `RandomNoise`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心

## 知识

覆盖率 **83%**（35/42）

**有卡**：`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`BasicGuider`、`ResolutionSelector`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`CLIPLoader`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`CR Prompt Text`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`RandomNoise`、`MiniMaxH3DualClockSamplerT8`、`LoraLoaderBypassModelOnly`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
