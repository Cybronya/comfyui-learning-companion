---
key: 视频生成/图生视频/(Hybird-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107064053121249282.json
name: (Hybird-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107064053121249282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Hybird-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107064053121249282.json
hash: 02b055cb37274a82
coverage: 0.939394
learned_at: 2026-10-17 22:17:07
nodes: [ComfyMathExpression, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3ChunkFeedForwardT8Advanced, SolAttnMiniMax, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, BasicGuider, Float, Note, MarkdownNote, Note, Float, VAELoader, LoraLoaderBypassModelOnly, MiniMaxH3SemanticBridgeApplyT8, SamplerCustomAdvanced, LoadImage, LoadImage, LoadImage, ResolutionSelector, MiniMaxH3AudioConditioningT8, ComfyMathExpression, PrimitiveFloat, LoadImage, RunningHub Deepcleaner, ComfyMathExpression, MiniMaxH3SemanticBridgeApplyT8, LoraLoaderModelOnly, MiniMaxH3LearnedLatentUpscaleT8Advanced, easy anythingIndexSwitch, Float, CR Prompt Text, LoraLoaderModelOnly, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3AVDecodeT8, easy cleanGpuUsed, CreateVideo, Astra, SaveVideo, MiniMaxH3DualClockSamplerT8, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, LoraLoaderBypassModelOnly, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(Hybird-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107064053121249282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Hybird-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107064053121249282.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Output → Other

**节点**（66 个）：
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
- `ModelAttentionBackend`
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
- `Note`
- `MarkdownNote`
- `Note`
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
- `ComfyMathExpression`
- `PrimitiveFloat`
- `LoadImage`
- `RunningHub Deepcleaner`
- `ComfyMathExpression`
- `MiniMaxH3SemanticBridgeApplyT8`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `easy anythingIndexSwitch`
- `Float`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3AVDecodeT8`
- `easy cleanGpuUsed`
- `CreateVideo`
- `Astra`
- `SaveVideo`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `LoraLoaderBypassModelOnly` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（62/66）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`LoadImage`、`VAELoader`、`LoraLoaderModelOnly`、`LoraLoaderBypassModelOnly`、`ModelAttentionBackend`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`SolAttnMiniMax`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`BasicGuider`、`RandomNoise`、`Float`、`MiniMaxH3SemanticBridgeApplyT8`、`SamplerCustomAdvanced`、`ResolutionSelector`、`RunningHub Deepcleaner`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`easy anythingIndexSwitch`、`CR Prompt Text`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3AVDecodeT8`、`easy cleanGpuUsed`、`CreateVideo`、`Astra`、`SaveVideo`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
