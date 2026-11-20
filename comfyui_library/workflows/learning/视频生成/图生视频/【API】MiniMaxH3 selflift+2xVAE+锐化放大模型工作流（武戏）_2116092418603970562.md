---
key: 视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（武戏）_2116092418603970562.json
name: 【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（武戏）_2116092418603970562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（武戏）_2116092418603970562.json
hash: f08ee8bc005cef1d
coverage: 0.515625
learned_at: 2026-11-02 19:19:11
nodes: [MarkdownNote, ConditioningZeroOut, ModelAttentionBackend, ComfyMathExpression, KSamplerSelect, BasicScheduler, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, H3SigmaRefiner, VAELoader, CLIPLoader, RunningHub Deepcleaner, LTXVSeparateAVLatent, VAELoader, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ResolutionSelector, VAEDecodeAudio, MarkdownNote, LoadImage, LoadImage, LoadImage, MiniMaxH3VAEDecodeFast, VHS_VideoCombine, VAELoader, Fast Groups Muter (rgthree), LoraLoaderModelOnly, SelfLiftAvatarH3Sampler, BlockSparseAttention, UNETLoader, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, LoraLoaderModelOnly, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（武戏）_2116092418603970562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【API】MiniMaxH3 selflift+2xVAE+锐化放大模型工作流（武戏）_2116092418603970562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（64 个）：
- `MarkdownNote`
- `ConditioningZeroOut`
- `ModelAttentionBackend`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `H3SigmaRefiner`
- `VAELoader`
- `CLIPLoader`
- `RunningHub Deepcleaner`
- `LTXVSeparateAVLatent`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `ResolutionSelector`
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3VAEDecodeFast` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `Fast Groups Muter (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `BlockSparseAttention`
- `UNETLoader` ★核心
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`

## 知识

覆盖率 **52%**（33/64）

**有卡**：`ConditioningZeroOut`、`ModelAttentionBackend`、`ComfyMathExpression`、`KSamplerSelect`、`BasicScheduler`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`H3SigmaRefiner`、`VAELoader`、`CLIPLoader`、`RunningHub Deepcleaner`、`LTXVSeparateAVLatent`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`VAEDecodeAudio`、`LoadImage`、`MiniMaxH3VAEDecodeFast`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`SelfLiftAvatarH3Sampler`、`BlockSparseAttention`、`UNETLoader`、`LoadAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
