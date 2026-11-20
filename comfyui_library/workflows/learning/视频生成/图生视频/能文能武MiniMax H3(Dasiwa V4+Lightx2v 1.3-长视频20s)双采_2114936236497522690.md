---
key: 视频生成/图生视频/能文能武MiniMax H3(Dasiwa V4+Lightx2v 1.3-长视频20s)双采_2114936236497522690.json
name: 能文能武MiniMax H3(Dasiwa V4+Lightx2v 1.3-长视频20s)双采_2114936236497522690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/能文能武MiniMax H3(Dasiwa V4+Lightx2v 1.3-长视频20s)双采_2114936236497522690.json
hash: cc29a403d7d4cf9c
coverage: 0.75
learned_at: 2026-10-30 18:01:36
nodes: [ComfyMathExpression, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3ChunkFeedForwardT8Advanced, SolAttnMiniMax, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, BasicGuider, Float, MarkdownNote, Float, VAELoader, LoraLoaderBypassModelOnly, MiniMaxH3SemanticBridgeApplyT8, SamplerCustomAdvanced, LoadImage, LoadImage, LoadImage, ResolutionSelector, MiniMaxH3AudioConditioningT8, PrimitiveFloat, LoadImage, RunningHub Deepcleaner, MiniMaxH3SemanticBridgeApplyT8, LoraLoaderModelOnly, MiniMaxH3LearnedLatentUpscaleT8Advanced, easy anythingIndexSwitch, Float, CR Prompt Text, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, easy cleanGpuUsed, MiniMaxH3DualClockSamplerT8, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, LoraLoaderBypassModelOnly, VHS_VideoCombine, UNETLoader, LoraLoaderBypassModelOnly, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, 孤海注释, CR Prompt Text, ConcatTextOfUtils, Note, PrimitiveInt, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, 孤海注释, 孤海注释]
patterns: []
missing: []
---

# 视频生成/图生视频/能文能武MiniMax H3(Dasiwa V4+Lightx2v 1.3-长视频20s)双采_2114936236497522690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/能文能武MiniMax H3(Dasiwa V4+Lightx2v 1.3-长视频20s)双采_2114936236497522690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（80 个）：
- `ComfyMathExpression`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `SolAttnMiniMax`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `BasicGuider`
- `Float`
- `MarkdownNote`
- `Float`
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3SemanticBridgeApplyT8`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `MiniMaxH3AudioConditioningT8`
- `PrimitiveFloat`
- `LoadImage`
- `RunningHub Deepcleaner`
- `MiniMaxH3SemanticBridgeApplyT8`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `easy anythingIndexSwitch`
- `Float`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `easy cleanGpuUsed`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `LoraLoaderBypassModelOnly` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `CR Prompt Text`
- `ConcatTextOfUtils`
- `Note`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **75%**（60/80）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`LoadImage`、`VAELoader`、`LoraLoaderModelOnly`、`LoraLoaderBypassModelOnly`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`SolAttnMiniMax`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`BasicGuider`、`RandomNoise`、`Float`、`MiniMaxH3SemanticBridgeApplyT8`、`SamplerCustomAdvanced`、`ResolutionSelector`、`RunningHub Deepcleaner`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`easy anythingIndexSwitch`、`CR Prompt Text`、`MiniMaxH3AVDecodeT8`、`easy cleanGpuUsed`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`VHS_VideoCombine`、`UNETLoader`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ConcatTextOfUtils`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
