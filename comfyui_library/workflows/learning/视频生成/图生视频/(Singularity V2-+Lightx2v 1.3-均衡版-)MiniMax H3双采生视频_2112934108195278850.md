---
key: 视频生成/图生视频/(Singularity V2-+Lightx2v 1.3-均衡版-)MiniMax H3双采生视频_2112934108195278850.json
name: (Singularity V2-+Lightx2v 1.3-均衡版-)MiniMax H3双采生视频_2112934108195278850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(Singularity V2-+Lightx2v 1.3-均衡版-)MiniMax H3双采生视频_2112934108195278850.json
hash: 060a9625d73d6aa5
coverage: 0.941176
learned_at: 2026-10-26 22:11:00
nodes: [ComfyMathExpression, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3ChunkFeedForwardT8Advanced, SolAttnMiniMax, MiniMaxH3AudioConditioningT8, MiniMaxH3TwoPassDetailMixerT8Advanced, BasicGuider, LoraLoaderModelOnly, RandomNoise, BasicGuider, Float, Note, MarkdownNote, Note, Float, VAELoader, MiniMaxH3SemanticBridgeApplyT8, SamplerCustomAdvanced, LoadImage, LoadImage, LoadImage, ResolutionSelector, MiniMaxH3AudioConditioningT8, ComfyMathExpression, PrimitiveFloat, LoadImage, RunningHub Deepcleaner, ComfyMathExpression, MiniMaxH3SemanticBridgeApplyT8, LoraLoaderModelOnly, MiniMaxH3LearnedLatentUpscaleT8Advanced, easy anythingIndexSwitch, CR Prompt Text, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, easy cleanGpuUsed, CreateVideo, Astra, SaveVideo, MiniMaxH3DualClockSamplerT8, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, Float, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/(Singularity V2-+Lightx2v 1.3-均衡版-)MiniMax H3双采生视频_2112934108195278850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/(Singularity V2-+Lightx2v 1.3-均衡版-)MiniMax H3双采生视频_2112934108195278850.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Output → Other

**节点**（68 个）：
- `ComfyMathExpression`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `SolAttnMiniMax`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `BasicGuider`
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
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `easy anythingIndexSwitch`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
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
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Float`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **94%**（64/68）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`LoadImage`、`VAELoader`、`LoraLoaderModelOnly`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`SolAttnMiniMax`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`BasicGuider`、`RandomNoise`、`Float`、`MiniMaxH3SemanticBridgeApplyT8`、`SamplerCustomAdvanced`、`ResolutionSelector`、`RunningHub Deepcleaner`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`easy anythingIndexSwitch`、`CR Prompt Text`、`MiniMaxH3AVDecodeT8`、`easy cleanGpuUsed`、`CreateVideo`、`Astra`、`SaveVideo`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`LoraLoaderBypassModelOnly`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`VHS_VideoCombine`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3DualClockSamplerT8
