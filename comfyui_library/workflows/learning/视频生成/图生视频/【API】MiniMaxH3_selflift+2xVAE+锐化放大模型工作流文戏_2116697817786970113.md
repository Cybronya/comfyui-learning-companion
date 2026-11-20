---
key: 视频生成/图生视频/【API】MiniMaxH3_selflift+2xVAE+锐化放大模型工作流文戏_2116697817786970113.json
name: 【API】MiniMaxH3_selflift+2xVAE+锐化放大模型工作流文戏_2116697817786970113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【API】MiniMaxH3_selflift+2xVAE+锐化放大模型工作流文戏_2116697817786970113.json
hash: 99d75773deec0874
coverage: 0.864865
learned_at: 2026-11-02 19:19:11
nodes: [MarkdownNote, ConditioningZeroOut, ModelAttentionBackend, ComfyMathExpression, KSamplerSelect, BasicScheduler, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, H3SigmaRefiner, VAELoader, CLIPLoader, RunningHub Deepcleaner, LTXVSeparateAVLatent, VAELoader, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ResolutionSelector, VAEDecodeAudio, MarkdownNote, LoadImage, LoadImage, LoadImage, MiniMaxH3VAEDecodeFast, VHS_VideoCombine, VAELoader, Fast Groups Muter (rgthree), LoraLoaderModelOnly, SelfLiftAvatarH3Sampler, BlockSparseAttention, UNETLoader, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/【API】MiniMaxH3_selflift+2xVAE+锐化放大模型工作流文戏_2116697817786970113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【API】MiniMaxH3_selflift+2xVAE+锐化放大模型工作流文戏_2116697817786970113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（37 个）：
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

## 知识

覆盖率 **86%**（32/37）

**有卡**：`ConditioningZeroOut`、`ModelAttentionBackend`、`ComfyMathExpression`、`KSamplerSelect`、`BasicScheduler`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`H3SigmaRefiner`、`VAELoader`、`CLIPLoader`、`RunningHub Deepcleaner`、`LTXVSeparateAVLatent`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`VAEDecodeAudio`、`LoadImage`、`MiniMaxH3VAEDecodeFast`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`SelfLiftAvatarH3Sampler`、`BlockSparseAttention`、`UNETLoader`、`LoadAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
