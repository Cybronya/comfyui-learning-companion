---
key: 视频生成/图生视频/啊癫 融合模型-self-lift工作流Cobijada_H3_Hybrid版_2116837093803642882.json
name: 啊癫 融合模型-self-lift工作流Cobijada_H3_Hybrid版_2116837093803642882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/啊癫 融合模型-self-lift工作流Cobijada_H3_Hybrid版_2116837093803642882.json
hash: 4f07ea71c7d9ddd1
coverage: 0.861111
learned_at: 2026-11-02 19:19:33
nodes: [ModelAttentionBackend, KSamplerSelect, ResolutionSelector, MarkdownNote, CLIPLoader, H3SigmaRefiner, ComfyMathExpression, BasicScheduler, ConditioningZeroOut, VAELoader, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, PrimitiveFloat, LoadImage, LoadImage, MarkdownNote, VHS_VideoCombine, VAEDecode, SelfLiftAvatarH3Sampler, UNETLoader, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, LoadImage, BlockSparseAttention, ModelPreviewOverrideKJ, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, VAELoader, VAEDecodeAudio, MarkdownNote, LoadAudio, LoadAudio, LoadAudio, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/啊癫 融合模型-self-lift工作流Cobijada_H3_Hybrid版_2116837093803642882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/啊癫 融合模型-self-lift工作流Cobijada_H3_Hybrid版_2116837093803642882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（36 个）：
- `ModelAttentionBackend`
- `KSamplerSelect` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `CLIPLoader`
- `H3SigmaRefiner`
- `ComfyMathExpression`
- `BasicScheduler`
- `ConditioningZeroOut`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BlockSparseAttention`
- `ModelPreviewOverrideKJ`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `VHS_VideoCombine`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`ModelAttentionBackend`、`KSamplerSelect`、`ResolutionSelector`、`CLIPLoader`、`H3SigmaRefiner`、`ComfyMathExpression`、`BasicScheduler`、`ConditioningZeroOut`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`LoadImage`、`VHS_VideoCombine`、`VAEDecode`、`SelfLiftAvatarH3Sampler`、`UNETLoader`、`BlockSparseAttention`、`ModelPreviewOverrideKJ`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`VAEDecodeAudio`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
