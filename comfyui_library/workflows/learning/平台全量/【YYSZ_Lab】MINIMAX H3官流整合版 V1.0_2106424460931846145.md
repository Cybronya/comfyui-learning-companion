---
key: 平台全量/【YYSZ_Lab】MINIMAX H3官流整合版 V1.0_2106424460931846145.json
name: 【YYSZ_Lab】MINIMAX H3官流整合版 V1.0_2106424460931846145
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【YYSZ_Lab】MINIMAX H3官流整合版 V1.0_2106424460931846145.json
hash: b63832734076f04f
coverage: 0.772152
learned_at: 2026-11-14 01:22:28
nodes: [VAELoader, VAELoader, BasicGuider, ComfyMathExpression, PrimitiveFloat, ResolutionSelector, RandomNoise, VAEDecode, VAEDecodeAudio, LoadImage, ModelAttentionBackend, KSamplerSelect, SamplerCustomAdvanced, ModelPreviewOverrideKJ, ManualSigmas, BasicScheduler, BlockSparseAttention, LoadImage, VHS_LoadVideo, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SemanticBridgeApplyT8, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, Label (rgthree), MiniMaxH3TopazEnvironmentEXPT8, MiniMaxH3TopazVideoEXPT8, LoadVideo, MarkdownNote, LTXVSeparateAVLatent, Reroute, BasicScheduler, SamplerCustomAdvanced, VAEDecode, SetNode, Reroute, Reroute, GetNode, VHS_VideoCombine, GetNode, 忽略多组孤海, Note, VAEDecodeAudio, SetNode, 忽略多组孤海, 忽略多组孤海, Note, 忽略多组孤海, Label (rgthree), PrimitiveStringMultiline, LoadImage, LoadAudioUI, LoadImage, MarkdownNote, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, SelfLiftH3TST, Note, Note, MarkdownNote, SelfLiftH3TST, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, LTXVConcatAVLatent, Note, Seed (rgthree), MinimaxH3LatentUpscaler3D, CLIPLoader, VHS_VideoCombine, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 平台全量/【YYSZ_Lab】MINIMAX H3官流整合版 V1.0_2106424460931846145.json

> 来源文件 `comfyui_library/workflows/平台全量/【YYSZ_Lab】MINIMAX H3官流整合版 V1.0_2106424460931846145.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（79 个）：
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `ResolutionSelector`
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoadImage`
- `ModelAttentionBackend`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelPreviewOverrideKJ`
- `ManualSigmas`
- `BasicScheduler`
- `BlockSparseAttention`
- `LoadImage`
- `VHS_LoadVideo`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `MiniMaxH3TopazEnvironmentEXPT8`
- `MiniMaxH3TopazVideoEXPT8`
- `LoadVideo`
- `MarkdownNote`
- `LTXVSeparateAVLatent`
- `Reroute`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `忽略多组孤海`
- `Note`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `忽略多组孤海`
- `忽略多组孤海`
- `Note`
- `忽略多组孤海`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadAudioUI`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SelfLiftH3TST`
- `Note`
- `Note`
- `MarkdownNote`
- `SelfLiftH3TST`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ReferenceToVideo`
- `LTXVConcatAVLatent`
- `Note`
- `Seed (rgthree)`
- `MinimaxH3LatentUpscaler3D`
- `CLIPLoader`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **77%**（61/79）

**有卡**：`VAELoader`、`BasicGuider`、`ComfyMathExpression`、`ResolutionSelector`、`RandomNoise`、`VAEDecode`、`VAEDecodeAudio`、`LoadImage`、`ModelAttentionBackend`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ModelPreviewOverrideKJ`、`ManualSigmas`、`BasicScheduler`、`BlockSparseAttention`、`VHS_LoadVideo`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3SemanticBridgeApplyT8`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`Label (rgthree)`、`MiniMaxH3TopazEnvironmentEXPT8`、`MiniMaxH3TopazVideoEXPT8`、`LoadVideo`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`忽略多组孤海`、`LoadAudioUI`、`UNETLoader`、`SelfLiftH3TST`、`MiniMaxH3ReferenceToVideo`、`LTXVConcatAVLatent`、`Seed (rgthree)`、`MinimaxH3LatentUpscaler3D`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
