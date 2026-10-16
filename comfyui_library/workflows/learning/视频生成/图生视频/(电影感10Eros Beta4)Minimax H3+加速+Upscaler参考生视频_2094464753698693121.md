---
key: 视频生成/图生视频/(电影感10Eros Beta4)Minimax H3+加速+Upscaler参考生视频_2094464753698693121.json
name: (电影感10Eros Beta4)Minimax H3+加速+Upscaler参考生视频_2094464753698693121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(电影感10Eros Beta4)Minimax H3+加速+Upscaler参考生视频_2094464753698693121.json
hash: 263bd0853dd17425
coverage: 0.945946
learned_at: 2026-10-17 00:01:59
nodes: [ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, VAELoader, BasicGuider, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3DualClockSamplerT8, SolAttnMiniMax, MiniMaxH3AudioConditioningT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, LoadImage, VHS_VideoCombine, ComfyMathExpression, PrimitiveFloat, MarkdownNote, LoadImage, LoadImage, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, ResolutionSelector, RandomNoise, UNETLoader, LoraLoaderBypassModelOnly, CLIPLoader, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/(电影感10Eros Beta4)Minimax H3+加速+Upscaler参考生视频_2094464753698693121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(电影感10Eros Beta4)Minimax H3+加速+Upscaler参考生视频_2094464753698693121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（37 个）：
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SolAttnMiniMax`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `LoadImage`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `RandomNoise`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `CLIPLoader`
- `CR Prompt Text`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`VAELoader`、`BasicGuider`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3DualClockSamplerT8`、`SolAttnMiniMax`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`VHS_VideoCombine`、`ComfyMathExpression`、`ResolutionSelector`、`RandomNoise`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`CLIPLoader`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
