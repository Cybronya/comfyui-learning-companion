---
key: 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json
name: 自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json
hash: 4fff8ecdfcf9382c
coverage: 0.427481
learned_at: 2026-10-15 22:48:59
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, 孤海注释, 孤海注释, 孤海注释, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, Any Switch (rgthree), MiniMaxLowVRAMAttention, SetNode, SetNode, VAEDecodeAudio, GetNode, SetNode, SetNode, GetNode, CreateVideo, ManualSigmas, ManualSigmas, GetNode, GetNode, VAEDecode, 孤海注释, ManualSigmas, GetNode, GetNode, LTXVSeparateAVLatent, Any Switch (rgthree), BasicGuider, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, LoadAudio, 忽略多组孤海, GetNode, MiniMaxH3ReferenceToVideo, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, GetNode, SetNode, GetNode, SetNode, SamplerCustomAdvanced, VAEDecodeAudio, SetNode, VAEDecode, SolAttnPatch, ResolutionSelector, PrimitiveFloat, 忽略多组孤海, MarkdownNote, 孤海注释, GetNode, SetNode, GetNode, Any Switch (rgthree), GetNode, GetNode, BasicScheduler, KSamplerSelect, MiniMaxH3SigmaShift, 忽略多组孤海, BasicGuider, LTXVConcatAVLatent, GetNode, BasicGuider, SamplerCustomAdvanced, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, SetNode, RandomNoise, GetNode, SetNode, VAEDecode, Any Switch (rgthree), Any Switch (rgthree), GetNode, GetNode, VHS_VideoCombine, ModelAttentionBackend, GetNode, GetNode, BasicScheduler, SetNode, GetNode, Int, PrimitiveStringMultiline, PrimitiveFloat, MiniMaxH3ImageToVideo, VAEDecodeAudio, MinimaxH3LatentUpscaler3D, SaveVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/自用版  Minimax H3 文生+图参多合一生视频二采高清放大工作流V4.0_2094319638514593793.json`

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
- `SetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CreateVideo`
- `ManualSigmas`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `孤海注释`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `Any Switch (rgthree)`
- `BasicGuider`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `LoadAudio`
- `忽略多组孤海`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `SolAttnPatch`
- `ResolutionSelector`
- `PrimitiveFloat`
- `忽略多组孤海`
- `MarkdownNote`
- `孤海注释`
- `GetNode`
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `MiniMaxH3SigmaShift`
- `忽略多组孤海`
- `BasicGuider`
- `LTXVConcatAVLatent`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ModelAttentionBackend`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `SetNode`
- `GetNode`
- `Int`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `MiniMaxH3ImageToVideo`
- `VAEDecodeAudio` ★核心
- `MinimaxH3LatentUpscaler3D`
- `SaveVideo`
- `LoadImage`

## 知识

覆盖率 **43%**（56/131）

**有卡**：`ComfyMathExpression`、`MiniMaxLowVRAMAttention`、`VAEDecodeAudio`、`CreateVideo`、`ManualSigmas`、`VAEDecode`、`LTXVSeparateAVLatent`、`BasicGuider`、`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`忽略多组孤海`、`MiniMaxH3ReferenceToVideo`、`MiniMaxChunkFeedForward`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`SolAttnPatch`、`ResolutionSelector`、`BasicScheduler`、`KSamplerSelect`、`MiniMaxH3SigmaShift`、`LTXVConcatAVLatent`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`VHS_VideoCombine`、`ModelAttentionBackend`、`Int`、`MiniMaxH3ImageToVideo`、`MinimaxH3LatentUpscaler3D`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
