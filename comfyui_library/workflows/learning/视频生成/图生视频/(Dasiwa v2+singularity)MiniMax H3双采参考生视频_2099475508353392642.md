---
key: 视频生成/图生视频/(Dasiwa v2+singularity)MiniMax H3双采参考生视频_2099475508353392642.json
name: (Dasiwa v2+singularity)MiniMax H3双采参考生视频_2099475508353392642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Dasiwa v2+singularity)MiniMax H3双采参考生视频_2099475508353392642.json
hash: 41e0974b8eae3e9b
coverage: 0.960784
learned_at: 2026-10-17 01:44:18
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, VAELoader, CLIPLoader, SolAttnMiniMax, VAELoader, UNETLoader, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, RandomNoise, BasicGuider, ComfyMathExpression, PrimitiveFloat, MiniMaxH3AudioConditioningT8, LoadImage, LoadImage, ConcatTextOfUtils, CR Prompt Text, MiniMaxH3AudioConditioningT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, SamplerCustomAdvanced, BasicGuider, MiniMaxH3TwoPassDetailMixerT8Advanced, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, VHS_VideoCombine, ResolutionSelector, CR Prompt Text, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/(Dasiwa v2+singularity)MiniMax H3双采参考生视频_2099475508353392642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Dasiwa v2+singularity)MiniMax H3双采参考生视频_2099475508353392642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（51 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `VAELoader`
- `CLIPLoader`
- `SolAttnMiniMax`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `RandomNoise`
- `BasicGuider`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `LoadImage`
- `ConcatTextOfUtils`
- `CR Prompt Text`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `CR Prompt Text`
- `MarkdownNote`

## 知识

覆盖率 **96%**（49/51）

**有卡**：`LoadImage`、`LoraLoaderModelOnly`、`LoraLoaderBypassModelOnly`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`VAELoader`、`CLIPLoader`、`SolAttnMiniMax`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`RandomNoise`、`BasicGuider`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`ConcatTextOfUtils`、`CR Prompt Text`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`SamplerCustomAdvanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`ResolutionSelector`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
