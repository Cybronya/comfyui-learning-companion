---
key: 视频生成/图生视频/(Remix0.8-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107054072120565762.json
name: (Remix0.8-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107054072120565762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Remix0.8-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107054072120565762.json
hash: c58bc90c87327dcd
coverage: 0.935484
learned_at: 2026-10-17 22:17:09
nodes: [ComfyMathExpression, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, ModelAttentionBackend, MiniMaxH3ChunkFeedForwardT8Advanced, SolAttnMiniMax, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, BasicGuider, Float, Note, MarkdownNote, Note, Float, VAELoader, MiniMaxH3SemanticBridgeApplyT8, SamplerCustomAdvanced, LoadImage, LoadImage, LoadImage, ResolutionSelector, MiniMaxH3AudioConditioningT8, ComfyMathExpression, PrimitiveFloat, LoadImage, RunningHub Deepcleaner, ComfyMathExpression, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, Float, CR Prompt Text, MiniMaxH3AVDecodeT8, easy cleanGpuUsed, CreateVideo, Astra, SaveVideo, MiniMaxH3DualClockSamplerT8, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, easy anythingIndexSwitch, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/(Remix0.8-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107054072120565762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Remix0.8-DMAD长视频-均衡版-动修2-Vbvr后置)MiniMax H3双采生视频_2107054072120565762.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Output → Other

**节点**（62 个）：
- `ComfyMathExpression`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `ModelAttentionBackend`
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `SolAttnMiniMax`
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
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `Float`
- `CR Prompt Text`
- `MiniMaxH3AVDecodeT8`
- `easy cleanGpuUsed`
- `CreateVideo`
- `Astra`
- `SaveVideo`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `easy anythingIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **94%**（58/62）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`LoadImage`、`VAELoader`、`ModelAttentionBackend`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`SolAttnMiniMax`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`BasicGuider`、`LoraLoaderModelOnly`、`RandomNoise`、`Float`、`MiniMaxH3SemanticBridgeApplyT8`、`SamplerCustomAdvanced`、`ResolutionSelector`、`MiniMaxH3AudioConditioningT8`、`RunningHub Deepcleaner`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`CR Prompt Text`、`MiniMaxH3AVDecodeT8`、`easy cleanGpuUsed`、`CreateVideo`、`Astra`、`SaveVideo`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`easy anythingIndexSwitch`、`LoraLoaderBypassModelOnly`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
