---
key: 视频生成/图生视频/MiniMax-H3-超自然服装细节展示-自动优化提示词-.json
name: MiniMax-H3-超自然服装细节展示-自动优化提示词-
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3-超自然服装细节展示-自动优化提示词-.json
hash: 00f1ff5c4351f6a3
coverage: 0.837838
learned_at: 2026-10-07 00:33:22
nodes: [CLIPLoader, VAELoader, VAELoader, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, RandomNoise, KSamplerSelect, BasicGuider, BasicScheduler, VAEDecode, VAEDecodeAudio, CreateVideo, LoraLoaderModelOnly, ModelPreviewOverrideKJ, UNETLoader, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, MarkdownNote, SamplerCustomAdvanced, LoadImage, ComfyMathExpression, BlockSparseAttention, ModelAttentionBackend, MiniMaxH3SigmaShift, MiniMaxChunkFeedForward, PrimitiveStringMultiline, SaveVideo, LoadImage, LoadImage, INTConstant, ResolutionSelector, easy seed, ShowText|pysssss, PrimitiveStringMultiline, PrimitiveStringMultiline, MiniMaxH3PromptEnhancerT8]
patterns: []
missing: [easy seed]
discoveries: [次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/MiniMax-H3-超自然服装细节展示-自动优化提示词-.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3-超自然服装细节展示-自动优化提示词-.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `ComfyMathExpression`
- `BlockSparseAttention`
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `MiniMaxChunkFeedForward`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `ResolutionSelector`
- `easy seed`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `MiniMaxH3PromptEnhancerT8`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderBypassModelOnly`、`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`ModelPreviewOverrideKJ`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`BlockSparseAttention`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`MiniMaxChunkFeedForward`、`SaveVideo`、`INTConstant`、`ResolutionSelector`、`MiniMaxH3PromptEnhancerT8`

**缺卡**（1）：`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
