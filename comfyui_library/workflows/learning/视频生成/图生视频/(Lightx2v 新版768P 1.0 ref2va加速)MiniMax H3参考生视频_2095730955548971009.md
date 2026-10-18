---
key: 视频生成/图生视频/(Lightx2v 新版768P 1.0 ref2va加速)MiniMax H3参考生视频_2095730955548971009.json
name: (Lightx2v 新版768P 1.0 ref2va加速)MiniMax H3参考生视频_2095730955548971009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Lightx2v 新版768P 1.0 ref2va加速)MiniMax H3参考生视频_2095730955548971009.json
hash: a53aa8c1f4167c94
coverage: 0.847826
learned_at: 2026-10-17 01:09:10
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, BasicGuider, PrimitiveFloat, LoadImage, MiniMaxH3TwoPassLatentReconcileT8Advanced, VAELoader, CLIPLoader, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, CR Prompt Text, VHS_VideoCombine, MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, MiniMaxH3AudioConditioningT8, SolAttnMiniMax, LoraLoaderModelOnly, BasicGuider, MiniMaxH3AudioConditioningT8, RandomNoise, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderBypassModelOnly, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, VAELoader, MarkdownNote, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, UNETLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/(Lightx2v 新版768P 1.0 ref2va加速)MiniMax H3参考生视频_2095730955548971009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Lightx2v 新版768P 1.0 ref2va加速)MiniMax H3参考生视频_2095730955548971009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（46 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `MarkdownNote`
- `BasicGuider`
- `PrimitiveFloat`
- `LoadImage`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `VAELoader`
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
- `VHS_VideoCombine`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AudioConditioningT8`
- `SolAttnMiniMax`
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `VAELoader`
- `MarkdownNote`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心

## 知识

覆盖率 **85%**（39/46）

**有卡**：`ComfyMathExpression`、`BasicGuider`、`LoadImage`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`VAELoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`ResolutionSelector`、`CR Prompt Text`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3AudioConditioningT8`、`SolAttnMiniMax`、`LoraLoaderModelOnly`、`RandomNoise`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`ModelAttentionBackend`、`LoraLoaderBypassModelOnly`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
