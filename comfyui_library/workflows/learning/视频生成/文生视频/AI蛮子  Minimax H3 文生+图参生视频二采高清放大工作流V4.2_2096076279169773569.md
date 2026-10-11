---
key: 视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json
name: AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json
hash: d79aa98154a45dfd
coverage: 0.384615
learned_at: 2026-10-11 21:41:33
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, 孤海注释, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, 忽略多组孤海, MarkdownNote, 孤海注释, GetNode, SetNode, SetNode, GetNode, MiniMaxH3ImageToVideo, 孤海注释, BasicGuider, BasicScheduler, RandomNoise, SolAttnPatch, KSamplerSelect, GetNode, MiniMaxLowVRAMAttention, MiniMaxH3SigmaShift, ModelAttentionBackend, GetNode, SetNode, 忽略多组孤海, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, Any Switch (rgthree), LTXVConcatAVLatent, GetNode, GetNode, Any Switch (rgthree), GetNode, SetNode, Fast Groups Bypasser (rgthree), VAEDecode, VAEDecodeAudio, CreateVideo, MiniMaxChunkFeedForward, GetNode, GetNode, PrimitiveStringMultiline, SetNode, GetNode, GetNode, GetNode, SetNode, ResolutionSelector, SetNode, PrimitiveFloat, SaveVideo, SetNode, SetNode, GetNode, easy ifElse, SetNode, SetNode, SamplerCustomAdvanced, BasicGuider, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), VAEDecode, VAEDecodeAudio, 孤海注释, CreateVideo, ModelPreviewOverrideKJ, SamplerCustomAdvanced, SetNode, GetNode, MiniMaxH3ReferenceToVideo, BasicScheduler, Int, SamplerCustomAdvanced, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, PathchSageAttentionKJ, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, PrimitiveFloat, 忽略多组孤海, BasicScheduler, BasicGuider, GetNode, Any Switch (rgthree), easy ifElse, SetNode, SetNode, LoadAudio, MinimaxH3LatentUpscaler3D, SaveVideo, easy boolean, VRGDG_MiniMaxH3AudioDrive, LoadImage]
patterns: []
missing: [easy boolean, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海]
discoveries: [次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI蛮子  Minimax H3 文生+图参生视频二采高清放大工作流V4.2_2096076279169773569.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（143 个）：
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
- `孤海注释`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `忽略多组孤海`
- `MarkdownNote`
- `孤海注释`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MiniMaxH3ImageToVideo`
- `孤海注释`
- `BasicGuider`
- `BasicScheduler`
- `RandomNoise`
- `SolAttnPatch`
- `KSamplerSelect` ★核心
- `GetNode`
- `MiniMaxLowVRAMAttention`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `GetNode`
- `SetNode`
- `忽略多组孤海`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `Any Switch (rgthree)`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `MiniMaxChunkFeedForward`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `PrimitiveFloat`
- `SaveVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `孤海注释`
- `CreateVideo`
- `ModelPreviewOverrideKJ`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `BasicScheduler`
- `Int`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
- `PrimitiveFloat`
- `忽略多组孤海`
- `BasicScheduler`
- `BasicGuider`
- `GetNode`
- `Any Switch (rgthree)`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `MinimaxH3LatentUpscaler3D`
- `SaveVideo`
- `easy boolean`
- `VRGDG_MiniMaxH3AudioDrive`
- `LoadImage`

## 知识

覆盖率 **38%**（55/143）

**有卡**：`ComfyMathExpression`、`LoadImage`、`VHS_LoadVideo`、`MiniMaxH3ImageToVideo`、`BasicGuider`、`BasicScheduler`、`RandomNoise`、`SolAttnPatch`、`KSamplerSelect`、`MiniMaxLowVRAMAttention`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`MiniMaxChunkFeedForward`、`ResolutionSelector`、`SaveVideo`、`SamplerCustomAdvanced`、`ModelPreviewOverrideKJ`、`MiniMaxH3ReferenceToVideo`、`Int`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadAudio`、`MinimaxH3LatentUpscaler3D`、`VRGDG_MiniMaxH3AudioDrive`

**缺卡**（4）：`easy boolean`、`忽略多组孤海`、`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
