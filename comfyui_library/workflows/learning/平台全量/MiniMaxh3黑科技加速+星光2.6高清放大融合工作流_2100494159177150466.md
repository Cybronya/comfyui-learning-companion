---
key: 平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100494159177150466.json
name: MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100494159177150466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100494159177150466.json
hash: bb344fb63704df6b
coverage: 0.745098
learned_at: 2026-11-14 00:45:12
nodes: [ModelAttentionBackend, KSamplerSelect, MarkdownNote, MiniMaxChunkFeedForward, H3SigmaRefiner, MiniMaxLowVRAMAttention, ConditioningZeroOut, CLIPLoader, ComfyMathExpression, ModelPreviewOverrideKJ, VAELoader, VAELoader, BasicScheduler, SelfLiftH3Sampler, Reroute, Reroute, Reroute, easy MiniMaxH3ReferenceToVideoBridge, UNETLoader, LoraLoaderModelOnly, VAEDecode, MarkdownNote, JWInteger, JWInteger, RH_Astra, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, PrimitiveFloat, Reroute, PrimitiveStringMultiline, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, RH_Astra, SaveVideoNode, SaveVideoNode, CreateVideo, VAEDecodeAudio, MarkdownNote, SaveVideoNode, SaveVideo]
patterns: []
missing: []
---

# 平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100494159177150466.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMaxh3黑科技加速+星光2.6高清放大融合工作流_2100494159177150466.json`

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
- `RH_Astra`
- `SaveVideoNode`
- `SaveVideoNode`
- `CreateVideo`
- `VAEDecodeAudio` ★核心
- `MarkdownNote`
- `SaveVideoNode`
- `SaveVideo`

## 知识

覆盖率 **75%**（38/51）

**有卡**：`ModelAttentionBackend`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`H3SigmaRefiner`、`MiniMaxLowVRAMAttention`、`ConditioningZeroOut`、`CLIPLoader`、`ComfyMathExpression`、`ModelPreviewOverrideKJ`、`VAELoader`、`BasicScheduler`、`SelfLiftH3Sampler`、`easy MiniMaxH3ReferenceToVideoBridge`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`JWInteger`、`RH_Astra`、`easy cleanGpuUsed`、`LoadAudio`、`LoadImage`、`ResolutionSelector`、`SaveVideoNode`、`CreateVideo`、`VAEDecodeAudio`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
