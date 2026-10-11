---
key: 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417.json
name: 自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417.json
hash: dfb088f856647124
coverage: 0.348624
learned_at: 2026-10-11 21:20:00
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, 孤海注释, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Fast Groups Bypasser (rgthree), MarkdownNote, 孤海注释, 孤海注释, 孤海注释, SetNode, ComfyMathExpression, GetNode, SetNode, GetNode, GetNode, 忽略多组孤海, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ImageToVideo, SetNode, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, SetNode, SetNode, LoadImage, SetNode, MiniMaxH3ReferenceToVideo, GetNode, BasicScheduler, GetNode, LoadImage, LTXVConcatAVLatent, PrimitiveFloat, H3SigmaRefiner, SamplerCustomAdvanced, GetNode, MiniMaxH3HybridLoader, CLIPLoader, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, MiniMaxH3SigmaShift, LoraLoaderModelOnly, ModelAttentionBackend, SolAttnPatch, PrimitiveStringMultiline, H3SigmaRefiner, RandomNoise, SetNode, SetNode, BasicGuider, KSamplerSelect, SetNode, SetNode, SetNode, KSamplerSelect, BasicGuider, RandomNoise, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, Any Switch (rgthree), GetNode, BasicScheduler, SplitSigmas, SetNode, SetNode, SplitSigmas, Any Switch (rgthree), Any Switch (rgthree), GetNode, Any Switch (rgthree), GetNode, GetNode, Any Switch (rgthree), LTXVSeparateAVLatent, SamplerCustomAdvanced, CreateVideo, PrimitiveFloat, ResolutionSelector, SaveVideo, MinimaxH3LatentUpscaler3D, GetNode, 孤海注释]
patterns: []
missing: [忽略多组孤海]
discoveries: [次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V3.0_2089952119318204417.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（109 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `孤海注释`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `忽略多组孤海`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ImageToVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `LoadImage`
- `LTXVConcatAVLatent`
- `PrimitiveFloat`
- `H3SigmaRefiner`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `MiniMaxH3HybridLoader`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `MiniMaxH3SigmaShift`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SolAttnPatch`
- `PrimitiveStringMultiline`
- `H3SigmaRefiner`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `Any Switch (rgthree)`
- `GetNode`
- `BasicScheduler`
- `SplitSigmas`
- `SetNode`
- `SetNode`
- `SplitSigmas`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SaveVideo`
- `MinimaxH3LatentUpscaler3D`
- `GetNode`
- `孤海注释`

## 知识

覆盖率 **35%**（38/109）

**有卡**：`ComfyMathExpression`、`MiniMaxH3ImageToVideo`、`VAEDecode`、`VAEDecodeAudio`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`LTXVConcatAVLatent`、`H3SigmaRefiner`、`SamplerCustomAdvanced`、`MiniMaxH3HybridLoader`、`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`SolAttnPatch`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SplitSigmas`、`LTXVSeparateAVLatent`、`CreateVideo`、`ResolutionSelector`、`SaveVideo`、`MinimaxH3LatentUpscaler3D`

**缺卡**（1）：`忽略多组孤海`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
