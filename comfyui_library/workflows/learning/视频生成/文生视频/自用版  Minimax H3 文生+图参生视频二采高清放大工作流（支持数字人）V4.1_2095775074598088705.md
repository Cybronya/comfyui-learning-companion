---
key: 视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json
name: 自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json
hash: 02ac84dd802a5304
coverage: 0.427481
learned_at: 2026-10-15 22:48:59
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, 孤海注释, 孤海注释, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxLowVRAMAttention, SetNode, SetNode, VAEDecodeAudio, GetNode, SetNode, GetNode, CreateVideo, GetNode, GetNode, VAEDecode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, 忽略多组孤海, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, GetNode, SolAttnPatch, ResolutionSelector, PrimitiveFloat, 忽略多组孤海, MarkdownNote, 孤海注释, GetNode, SetNode, Any Switch (rgthree), GetNode, BasicScheduler, KSamplerSelect, MiniMaxH3SigmaShift, GetNode, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, SetNode, RandomNoise, ModelAttentionBackend, GetNode, SetNode, GetNode, Int, PrimitiveStringMultiline, PrimitiveFloat, MiniMaxH3ImageToVideo, 孤海注释, GetNode, GetNode, Any Switch (rgthree), Any Switch (rgthree), VAEDecodeAudio, MiniMaxH3ReferenceToVideo, SetNode, GetNode, GetNode, VAEDecode, BasicGuider, SetNode, BasicGuider, BasicScheduler, VAEDecode, VAEDecodeAudio, SetNode, SetNode, GetNode, GetNode, SaveVideo, GetNode, GetNode, Any Switch (rgthree), GetNode, BasicGuider, SamplerCustomAdvanced, CreateVideo, MinimaxH3LatentUpscaler3D, LTXVSeparateAVLatent, CreateVideo, LTXVConcatAVLatent, SamplerCustomAdvanced, BasicScheduler, 孤海注释, Any Switch (rgthree), SaveVideo, SetNode, SetNode, VRGDG_MiniMaxH3AudioDrive, LoadAudio, UNETLoader, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/自用版  Minimax H3 文生+图参生视频二采高清放大工作流（支持数字人）V4.1_2095775074598088705.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `孤海注释`
- `孤海注释`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
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
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SolAttnPatch`
- `ResolutionSelector`
- `PrimitiveFloat`
- `忽略多组孤海`
- `MarkdownNote`
- `孤海注释`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `MiniMaxH3SigmaShift`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `RandomNoise`
- `ModelAttentionBackend`
- `GetNode`
- `SetNode`
- `GetNode`
- `Int`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `MiniMaxH3ImageToVideo`
- `孤海注释`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `VAEDecodeAudio` ★核心
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `BasicGuider`
- `SetNode`
- `BasicGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveVideo`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `MinimaxH3LatentUpscaler3D`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `孤海注释`
- `Any Switch (rgthree)`
- `SaveVideo`
- `SetNode`
- `SetNode`
- `VRGDG_MiniMaxH3AudioDrive`
- `LoadAudio`
- `UNETLoader` ★核心
- `LoadImage`

## 知识

覆盖率 **43%**（56/131）

**有卡**：`ComfyMathExpression`、`MiniMaxLowVRAMAttention`、`VAEDecodeAudio`、`CreateVideo`、`VAEDecode`、`LoadImage`、`VHS_LoadVideo`、`忽略多组孤海`、`MiniMaxChunkFeedForward`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`SolAttnPatch`、`ResolutionSelector`、`BasicScheduler`、`KSamplerSelect`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`ModelAttentionBackend`、`Int`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ReferenceToVideo`、`BasicGuider`、`SaveVideo`、`MinimaxH3LatentUpscaler3D`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`VRGDG_MiniMaxH3AudioDrive`、`LoadAudio`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
