---
key: 视频生成/图生视频/Minimax+H3+Zs05+双采+加速+Lantent+Upscaler参考生视频_2092271863945846785.json
name: Minimax+H3+Zs05+双采+加速+Lantent+Upscaler参考生视频_2092271863945846785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax+H3+Zs05+双采+加速+Lantent+Upscaler参考生视频_2092271863945846785.json
hash: 566133fbee7d1b47
coverage: 0.944444
learned_at: 2026-10-16 22:59:15
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, SolAttnMiniMax, ResolutionSelector, PrimitiveFloat, ComfyMathExpression, BasicGuider, MiniMaxH3AudioConditioningT8, VAELoader, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3AudioConditioningT8, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3DualClockSamplerT8, CR Prompt Text, MarkdownNote, RandomNoise, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, LoraLoaderBypassModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax+H3+Zs05+双采+加速+Lantent+Upscaler参考生视频_2092271863945846785.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax+H3+Zs05+双采+加速+Lantent+Upscaler参考生视频_2092271863945846785.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（36 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SolAttnMiniMax`
- `ResolutionSelector`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `BasicGuider`
- `MiniMaxH3AudioConditioningT8`
- `VAELoader`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3AudioConditioningT8`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `CR Prompt Text`
- `MarkdownNote`
- `RandomNoise`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `LoraLoaderBypassModelOnly` ★核心

## 知识

覆盖率 **94%**（34/36）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SolAttnMiniMax`、`ResolutionSelector`、`ComfyMathExpression`、`BasicGuider`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`SamplerCustomAdvanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3DualClockSamplerT8`、`CR Prompt Text`、`RandomNoise`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`LoraLoaderBypassModelOnly`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
