---
key: 视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json
name: MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json
hash: 569e71ccb7d88ba1
coverage: 0.745098
learned_at: 2026-10-15 22:46:31
nodes: [ModelAttentionBackend, KSamplerSelect, MarkdownNote, MiniMaxChunkFeedForward, H3SigmaRefiner, MiniMaxLowVRAMAttention, ConditioningZeroOut, CLIPLoader, ComfyMathExpression, ModelPreviewOverrideKJ, VAELoader, VAELoader, BasicScheduler, SelfLiftH3Sampler, Reroute, Reroute, Reroute, easy MiniMaxH3ReferenceToVideoBridge, UNETLoader, LoraLoaderModelOnly, VAEDecode, MarkdownNote, MarkdownNote, JWInteger, JWInteger, RH_Astra, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, PrimitiveFloat, Reroute, PrimitiveStringMultiline, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, SaveVideoNode, RH_Astra, SaveVideoNode, SaveVideoNode, CreateVideo, SaveVideo, VAEDecodeAudio]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2099681234111787009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
- `ModelAttentionBackend`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MiniMaxChunkFeedForward`
- `H3SigmaRefiner`
- `MiniMaxLowVRAMAttention`
- `ConditioningZeroOut`
- `CLIPLoader`
- `ComfyMathExpression`
- `ModelPreviewOverrideKJ`
- `VAELoader`
- `VAELoader`
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `easy MiniMaxH3ReferenceToVideoBridge`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `JWInteger`
- `JWInteger`
- `RH_Astra`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PrimitiveFloat`
- `Reroute`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `SaveVideoNode`
- `RH_Astra`
- `SaveVideoNode`
- `SaveVideoNode`
- `CreateVideo`
- `SaveVideo`
- `VAEDecodeAudio` ★核心

## 知识

覆盖率 **75%**（38/51）

**有卡**：`ModelAttentionBackend`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`H3SigmaRefiner`、`MiniMaxLowVRAMAttention`、`ConditioningZeroOut`、`CLIPLoader`、`ComfyMathExpression`、`ModelPreviewOverrideKJ`、`VAELoader`、`BasicScheduler`、`SelfLiftH3Sampler`、`easy MiniMaxH3ReferenceToVideoBridge`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`JWInteger`、`RH_Astra`、`easy cleanGpuUsed`、`LoadAudio`、`LoadImage`、`ResolutionSelector`、`SaveVideoNode`、`CreateVideo`、`SaveVideo`、`VAEDecodeAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
