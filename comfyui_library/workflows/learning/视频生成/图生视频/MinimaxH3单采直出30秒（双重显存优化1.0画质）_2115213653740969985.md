---
key: 视频生成/图生视频/MinimaxH3单采直出30秒（双重显存优化1.0画质）_2115213653740969985.json
name: MinimaxH3单采直出30秒（双重显存优化1.0画质）_2115213653740969985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3单采直出30秒（双重显存优化1.0画质）_2115213653740969985.json
hash: 18cbab7cbe411ae1
coverage: 0.458333
learned_at: 2026-10-30 17:58:28
nodes: [SetNode, SetNode, SetNode, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, VHS_LoadVideo, 忽略多组孤海, SetNode, 忽略多组孤海, GetNode, MarkdownNote, RandomNoise, SetNode, MiniMaxH3ReferenceToVideo, CLIPLoader, VAELoader, VAELoader, SetNode, ManualSigmas, BasicGuider, KSamplerSelect, UNETLoader, VAEDecodeAudio, BlockSparseAttention, ModelAttentionBackend, SetNode, SamplerCustomAdvanced, VHS_VideoCombine, VAEDecode, LoadImage, 忽略多组孤海, LoadImage, LoadImage, LoadImage, MiniMaxH3LowVRAMAttentionT8Advanced, MiniMaxH3ChunkFeedForwardT8Advanced, ModelPreviewOverrideKJ, ResolutionSelector, PrimitiveStringMultiline, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/MinimaxH3单采直出30秒（双重显存优化1.0画质）_2115213653740969985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3单采直出30秒（双重显存优化1.0画质）_2115213653740969985.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（72 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `VHS_LoadVideo`
- `忽略多组孤海`
- `SetNode`
- `忽略多组孤海`
- `GetNode`
- `MarkdownNote`
- `RandomNoise`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `ManualSigmas`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `VAEDecodeAudio` ★核心
- `BlockSparseAttention`
- `ModelAttentionBackend`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LoadImage`
- `忽略多组孤海`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3LowVRAMAttentionT8Advanced`
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`

## 知识

覆盖率 **46%**（33/72）

**有卡**：`LoadAudio`、`LoadImage`、`ComfyMathExpression`、`VHS_LoadVideo`、`忽略多组孤海`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`CLIPLoader`、`VAELoader`、`ManualSigmas`、`BasicGuider`、`KSamplerSelect`、`UNETLoader`、`VAEDecodeAudio`、`BlockSparseAttention`、`ModelAttentionBackend`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`MiniMaxH3LowVRAMAttentionT8Advanced`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`ModelPreviewOverrideKJ`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
