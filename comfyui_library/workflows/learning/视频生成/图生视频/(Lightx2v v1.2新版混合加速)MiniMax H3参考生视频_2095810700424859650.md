---
key: 视频生成/图生视频/(Lightx2v v1.2新版混合加速)MiniMax H3参考生视频_2095810700424859650.json
name: (Lightx2v v1.2新版混合加速)MiniMax H3参考生视频_2095810700424859650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Lightx2v v1.2新版混合加速)MiniMax H3参考生视频_2095810700424859650.json
hash: 27491ff8fe6d7bea
coverage: 0.854167
learned_at: 2026-10-17 01:09:10
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, MarkdownNote, BasicGuider, PrimitiveFloat, LoadImage, MiniMaxH3TwoPassLatentReconcileT8Advanced, VAELoader, CLIPLoader, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, CR Prompt Text, VHS_VideoCombine, SamplerCustomAdvanced, MiniMaxH3AudioConditioningT8, BasicGuider, MiniMaxH3AudioConditioningT8, RandomNoise, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassDetailMixerT8Advanced, ModelAttentionBackend, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, VAELoader, MarkdownNote, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, SolAttnMiniMax, MiniMaxH3DualClockSamplerT8, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/(Lightx2v v1.2新版混合加速)MiniMax H3参考生视频_2095810700424859650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Lightx2v v1.2新版混合加速)MiniMax H3参考生视频_2095810700424859650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（48 个）：
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
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AudioConditioningT8`
- `BasicGuider`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `ModelAttentionBackend`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `VAELoader`
- `MarkdownNote`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SolAttnMiniMax`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **85%**（41/48）

**有卡**：`ComfyMathExpression`、`BasicGuider`、`LoadImage`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`VAELoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`ResolutionSelector`、`CR Prompt Text`、`MiniMaxH3AudioConditioningT8`、`RandomNoise`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`ModelAttentionBackend`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`LoraLoaderModelOnly`、`SolAttnMiniMax`、`MiniMaxH3DualClockSamplerT8`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
