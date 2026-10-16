---
key: 视频生成/图生视频/(Dasiwa+Lightx2v 1.0 768P新)MiniMax H3参考生视频V1_2093206224304173058.json
name: (Dasiwa+Lightx2v 1.0 768P新)MiniMax H3参考生视频V1_2093206224304173058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Dasiwa+Lightx2v 1.0 768P新)MiniMax H3参考生视频V1_2093206224304173058.json
hash: 3b3d8a3948df858d
coverage: 0.833333
learned_at: 2026-10-16 23:41:50
nodes: [MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, VAELoader, ModelAttentionBackend, BasicGuider, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, MiniMaxH3AudioConditioningT8, LoadImage, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassDetailMixerT8Advanced, CLIPLoader, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, CR Prompt Text, SolAttnMiniMax, VHS_VideoCombine, LoraLoaderBypassModelOnly, UNETLoader, VAELoader]
patterns: []
missing: []
---

# 视频生成/图生视频/(Dasiwa+Lightx2v 1.0 768P新)MiniMax H3参考生视频V1_2093206224304173058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Dasiwa+Lightx2v 1.0 768P新)MiniMax H3参考生视频V1_2093206224304173058.json`

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
- `ModelAttentionBackend`
- `BasicGuider`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
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
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `CR Prompt Text`
- `SolAttnMiniMax`
- `VHS_VideoCombine`
- `LoraLoaderBypassModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`MiniMaxH3DualClockSamplerT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`ModelAttentionBackend`、`BasicGuider`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RandomNoise`、`MiniMaxH3AudioConditioningT8`、`LoadImage`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`CLIPLoader`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`ResolutionSelector`、`CR Prompt Text`、`SolAttnMiniMax`、`LoraLoaderBypassModelOnly`、`UNETLoader`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8、MiniMaxH3AVDecodeT8
