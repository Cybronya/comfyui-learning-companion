---
key: 视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json
name: AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json
hash: 3b3ea97bdd486601
coverage: 0.424658
learned_at: 2026-10-15 22:43:59
nodes: [MarkdownNote, BasicGuider, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, 孤海注释, LoadImage, LoadImage, 孤海注释, MiniMaxH3ImageToVideo, BasicScheduler, SetNode, GetNode, GetNode, SetNode, GetNode, Fast Groups Bypasser (rgthree), GetNode, Any Switch (rgthree), GetNode, GetNode, SetNode, GetNode, PrimitiveFloat, SetNode, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, 忽略多组孤海, GetNode, Any Switch (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, BasicGuider, BasicScheduler, SetNode, SetNode, GetNode, ImpactConditionalBranch, GetNode, SetNode, GetNode, ImpactConditionalBranch, Any Switch (rgthree), ImageResizeKJv2, ImageResizeKJv2, 忽略多组孤海, 孤海注释, 孤海注释, 孤海注释, CLIPLoader, VAELoader, VAELoader, ComfyMathExpression, SetNode, SetNode, RandomNoise, KSamplerSelect, SamplerCustomAdvanced, GetNode, GetNode, GetNode, ResolutionSelector, 孤海注释, MiniMaxH3ReferenceToVideo, GetNode, 孤海注释, SetNode, SetNode, SamplerCustomAdvanced, GetNode, 孤海注释, PrimitiveFloat, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, Int, MiniMaxH3MemoryEfficientSageAttentionPatch, SolAttnPatch, GetNode, MiniMaxH3SigmaShift, SetNode, ModelAttentionBackend, LTXVConcatAVLatent, BasicGuider, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, SaveVideo, PathchSageAttentionKJ, LTXVSeparateAVLatent, 孤海注释, 忽略多组孤海, LoadAudio, CreateVideo, VRGDG_MiniMaxH3AudioDrive, LoadImage, LoadImage, MinimaxH3LatentUpscaler3D, BasicScheduler, PrimitiveStringMultiline, 孤海注释, ModelPreviewOverrideKJ, UNETLoader, LoraLoaderModelOnly, 布尔孤海, 忽略多组孤海]
patterns: []
missing: []
---

# 视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI 蛮子   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V5.0_2096893867701399553.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
- `MarkdownNote`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `MiniMaxH3ImageToVideo`
- `BasicScheduler`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `忽略多组孤海`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `BasicGuider`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImpactConditionalBranch`
- `GetNode`
- `SetNode`
- `GetNode`
- `ImpactConditionalBranch`
- `Any Switch (rgthree)`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `忽略多组孤海`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ResolutionSelector`
- `孤海注释`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `孤海注释`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `孤海注释`
- `PrimitiveFloat`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `Int`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SolAttnPatch`
- `GetNode`
- `MiniMaxH3SigmaShift`
- `SetNode`
- `ModelAttentionBackend`
- `LTXVConcatAVLatent`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SaveVideo`
- `PathchSageAttentionKJ`
- `LTXVSeparateAVLatent`
- `孤海注释`
- `忽略多组孤海`
- `LoadAudio`
- `CreateVideo`
- `VRGDG_MiniMaxH3AudioDrive`
- `LoadImage`
- `LoadImage`
- `MinimaxH3LatentUpscaler3D`
- `BasicScheduler`
- `PrimitiveStringMultiline`
- `孤海注释`
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `布尔孤海`
- `忽略多组孤海`

## 知识

覆盖率 **42%**（62/146）

**有卡**：`BasicGuider`、`LoadImage`、`MiniMaxH3ImageToVideo`、`BasicScheduler`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`VHS_LoadVideo`、`忽略多组孤海`、`ImpactConditionalBranch`、`ImageResizeKJv2`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`Int`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SolAttnPatch`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`LTXVConcatAVLatent`、`SaveVideo`、`PathchSageAttentionKJ`、`LTXVSeparateAVLatent`、`LoadAudio`、`CreateVideo`、`VRGDG_MiniMaxH3AudioDrive`、`MinimaxH3LatentUpscaler3D`、`ModelPreviewOverrideKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`布尔孤海`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
