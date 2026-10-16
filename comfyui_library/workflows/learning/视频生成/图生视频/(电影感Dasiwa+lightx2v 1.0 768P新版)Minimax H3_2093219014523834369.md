---
key: 视频生成/图生视频/(电影感Dasiwa+lightx2v 1.0 768P新版)Minimax H3_2093219014523834369.json
name: (电影感Dasiwa+lightx2v 1.0 768P新版)Minimax H3_2093219014523834369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(电影感Dasiwa+lightx2v 1.0 768P新版)Minimax H3_2093219014523834369.json
hash: edc0a934579f1289
coverage: 0.833333
learned_at: 2026-10-16 23:41:52
nodes: [MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, SolAttnMiniMax, ModelAttentionBackend, BasicGuider, ResolutionSelector, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, MiniMaxH3AudioConditioningT8, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassDetailMixerT8Advanced, CLIPLoader, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, VHS_VideoCombine, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, RandomNoise, LoraLoaderBypassModelOnly, UNETLoader, VAELoader, LoraLoaderBypassModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/(电影感Dasiwa+lightx2v 1.0 768P新版)Minimax H3_2093219014523834369.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(电影感Dasiwa+lightx2v 1.0 768P新版)Minimax H3_2093219014523834369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（42 个）：
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
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `LoraLoaderBypassModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心

## 知识

覆盖率 **83%**（35/42）

**有卡**：`MiniMaxH3DualClockSamplerT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`BasicGuider`、`ResolutionSelector`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`CLIPLoader`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`CR Prompt Text`、`RandomNoise`、`LoraLoaderBypassModelOnly`、`UNETLoader`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
