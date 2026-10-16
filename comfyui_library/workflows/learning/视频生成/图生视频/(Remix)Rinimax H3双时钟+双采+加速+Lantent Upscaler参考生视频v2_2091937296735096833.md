---
key: 视频生成/图生视频/(Remix)Rinimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091937296735096833.json
name: (Remix)Rinimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091937296735096833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Remix)Rinimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091937296735096833.json
hash: 3ddc9c87b8672877
coverage: 0.829268
learned_at: 2026-10-16 22:30:22
nodes: [MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, SolAttnMiniMax, ModelAttentionBackend, BasicGuider, ResolutionSelector, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3AudioConditioningT8, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3TwoPassDetailMixerT8Advanced, VAELoader, LoraLoaderBypassModelOnly, CR Prompt Text, CLIPLoader, UNETLoader, SamplerCustomAdvanced]
patterns: []
missing: []
---

# 视频生成/图生视频/(Remix)Rinimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091937296735096833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Remix)Rinimax H3双时钟+双采+加速+Lantent Upscaler参考生视频v2_2091937296735096833.json`

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
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心
- `CR Prompt Text`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心

## 知识

覆盖率 **83%**（34/41）

**有卡**：`MiniMaxH3DualClockSamplerT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`BasicGuider`、`ResolutionSelector`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RandomNoise`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`LoraLoaderBypassModelOnly`、`CR Prompt Text`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
