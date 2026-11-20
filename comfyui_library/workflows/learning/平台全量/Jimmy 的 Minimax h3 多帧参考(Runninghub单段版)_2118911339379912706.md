---
key: 平台全量/Jimmy 的 Minimax h3 多帧参考(Runninghub单段版)_2118911339379912706.json
name: Jimmy 的 Minimax h3 多帧参考(Runninghub单段版)_2118911339379912706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Jimmy 的 Minimax h3 多帧参考(Runninghub单段版)_2118911339379912706.json
hash: 942974cf4af348cd
coverage: 0.649485
learned_at: 2026-11-14 00:33:07
nodes: [SetNode, VAELoader, CLIPLoader, KSamplerSelect, SetNode, ResolutionSelector, Fast Bypasser (rgthree), LoadImage, LoadImage, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CreateVideo, ComfyMathExpression, SetNode, Any Switch (rgthree), Any Switch (rgthree), MiniMaxH3AddGuide, VAEDecode, BasicGuider, MarkdownNote, MarkdownNote, VRGDG_MiniMaxH3AudioDrive, PrimitiveFloat, GetNode, VAEDecodeAudio, GetNode, RandomNoise, SetNode, VAELoader, SetNode, LoadAudio, LoadImage, LoadImage, LoadImage, TrimAudioDuration, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, SamplerCustomAdvanced, Reroute, MiniMaxH3AddGuide, BasicScheduler, MiniMaxH3AddGuide, LoadImage, GetNode, SetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, LoadImage, LoadImage, GetNode, ModelPreviewOverrideKJ, GetNode, GetNode, SetNode, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SemanticBridgeApplyT8, ManualSigmas, MarkdownNote, MarkdownNote, ManualSigmas, ManualSigmas, LoraLoaderModelOnly, 忽略多组孤海, 忽略多组孤海, 3000688f-5a2b-435a-9a09-b8b8cf4dfda5, TrimAudioDuration, LoadAudio, 忽略多组孤海, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, BlockSparseAttention, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GoohaiUniversalSlider, 忽略多组孤海, MiniMaxH3SigmaShift, UNETLoader, VHS_LoadVideo, VHS_LoadVideo, SaveVideo, Text, LoraLoaderModelOnly, Fast Groups Muter (rgthree), LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/Jimmy 的 Minimax h3 多帧参考(Runninghub单段版)_2118911339379912706.json

> 来源文件 `comfyui_library/workflows/平台全量/Jimmy 的 Minimax h3 多帧参考(Runninghub单段版)_2118911339379912706.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（97 个）：
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `SetNode`
- `ResolutionSelector`
- `Fast Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `ComfyMathExpression`
- `SetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `MiniMaxH3AddGuide`
- `VAEDecode` ★核心
- `BasicGuider`
- `MarkdownNote`
- `MarkdownNote`
- `VRGDG_MiniMaxH3AudioDrive`
- `PrimitiveFloat`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `RandomNoise`
- `SetNode`
- `VAELoader`
- `SetNode`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TrimAudioDuration`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `MiniMaxH3AddGuide`
- `BasicScheduler`
- `MiniMaxH3AddGuide`
- `LoadImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SemanticBridgeApplyT8`
- `ManualSigmas`
- `MarkdownNote`
- `MarkdownNote`
- `ManualSigmas`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `忽略多组孤海`
- `忽略多组孤海`
- `3000688f-5a2b-435a-9a09-b8b8cf4dfda5`
- `TrimAudioDuration`
- `LoadAudio`
- `忽略多组孤海`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GoohaiUniversalSlider`
- `忽略多组孤海`
- `MiniMaxH3SigmaShift`
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `SaveVideo`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Muter (rgthree)`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **65%**（63/97）

**有卡**：`VAELoader`、`CLIPLoader`、`KSamplerSelect`、`ResolutionSelector`、`Fast Bypasser (rgthree)`、`LoadImage`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3AddGuide`、`VAEDecode`、`BasicGuider`、`VRGDG_MiniMaxH3AudioDrive`、`VAEDecodeAudio`、`RandomNoise`、`LoadAudio`、`TrimAudioDuration`、`MiniMaxH3ReferenceToVideo`、`SamplerCustomAdvanced`、`BasicScheduler`、`VHS_VideoCombine`、`ModelPreviewOverrideKJ`、`MiniMaxH3SemanticBridgeConfigT8`、`MiniMaxH3SemanticBridgeApplyT8`、`ManualSigmas`、`LoraLoaderModelOnly`、`忽略多组孤海`、`3000688f-5a2b-435a-9a09-b8b8cf4dfda5`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`GoohaiUniversalSlider`、`MiniMaxH3SigmaShift`、`UNETLoader`、`VHS_LoadVideo`、`SaveVideo`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
