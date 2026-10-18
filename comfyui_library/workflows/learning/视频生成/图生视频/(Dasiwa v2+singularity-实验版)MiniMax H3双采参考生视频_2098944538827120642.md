---
key: 视频生成/图生视频/(Dasiwa v2+singularity-实验版)MiniMax H3双采参考生视频_2098944538827120642.json
name: (Dasiwa v2+singularity-实验版)MiniMax H3双采参考生视频_2098944538827120642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Dasiwa v2+singularity-实验版)MiniMax H3双采参考生视频_2098944538827120642.json
hash: b5d8f683fc3173d5
coverage: 0.962963
learned_at: 2026-10-17 01:44:18
nodes: [ComfyMathExpression, BasicGuider, PrimitiveFloat, LoadImage, MiniMaxH3TwoPassLatentReconcileT8Advanced, VAELoader, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SamplerCustomAdvanced, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, RandomNoise, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicGuider, LoraLoaderModelOnly, ConcatTextOfUtils, CR Prompt Text, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, CR Prompt Text, VHS_VideoCombine, MiniMaxH3LearnedLatentUpscaleT8Advanced, MarkdownNote, ResolutionSelector, UNETLoader, MiniMaxH3DualClockSamplerT8, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/(Dasiwa v2+singularity-实验版)MiniMax H3双采参考生视频_2098944538827120642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Dasiwa v2+singularity-实验版)MiniMax H3双采参考生视频_2098944538827120642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（54 个）：
- `ComfyMathExpression`
- `BasicGuider`
- `PrimitiveFloat`
- `LoadImage`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `LoraLoaderModelOnly` ★核心
- `ConcatTextOfUtils`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MarkdownNote`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **96%**（52/54）

**有卡**：`ComfyMathExpression`、`BasicGuider`、`LoadImage`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`VAELoader`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`MiniMaxH3AudioConditioningT8`、`RandomNoise`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`LoraLoaderModelOnly`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`SolAttnMiniMax`、`ConcatTextOfUtils`、`CR Prompt Text`、`VHS_VideoCombine`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`ResolutionSelector`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`CLIPLoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
