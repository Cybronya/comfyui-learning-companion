---
key: 视频生成/图生视频/MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370.json
name: MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370.json
hash: 7e96b66d31d643fd
coverage: 0.945946
learned_at: 2026-10-17 00:02:17
nodes: [ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, VAELoader, BasicGuider, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3DualClockSamplerT8, SolAttnMiniMax, LoadImage, VHS_VideoCombine, ComfyMathExpression, PrimitiveFloat, MarkdownNote, CLIPLoader, LoadImage, VHS_VideoCombine, RandomNoise, MiniMaxH3LearnedLatentUpscaleT8Advanced, LoraLoaderBypassModelOnly, SamplerCustomAdvanced, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, UNETLoader, ResolutionSelector, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Dasiwa HybirdV1turboV1+600EMA参考生视频V1_2094425009153466370.json`

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
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SolAttnMiniMax`
- `LoadImage`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MarkdownNote`
- `CLIPLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `RandomNoise`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `LoraLoaderBypassModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`VAELoader`、`BasicGuider`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3DualClockSamplerT8`、`SolAttnMiniMax`、`VHS_VideoCombine`、`ComfyMathExpression`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`LoraLoaderBypassModelOnly`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`UNETLoader`、`ResolutionSelector`、`MiniMaxH3AudioConditioningT8`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
