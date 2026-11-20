---
key: 平台全量/MiniMax_H3 终极篇 motion_speed_slider_mmh3_v1.1文武双全_2117515243374075906.json
name: MiniMax_H3 终极篇 motion_speed_slider_mmh3_v1.1文武双全_2117515243374075906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax_H3 终极篇 motion_speed_slider_mmh3_v1.1文武双全_2117515243374075906.json
hash: af5784548563fc3d
coverage: 0.465347
learned_at: 2026-11-14 00:44:59
nodes: [LoadImage, LoadImage, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, Note, Note, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, 忽略多组孤海, Note, SetNode, SetNode, LoadAudio, SetNode, 忽略多组孤海, LoadImage, 忽略多组孤海, GetNode, GetNode, SetNode, SetNode, SetNode, ModelAttentionBackend, ModelPreviewOverrideKJ, GetNode, SetNode, 忽略多组孤海, LoraLoaderModelOnly, ComfyMathExpression, SetNode, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAEDecode, VAEDecodeAudio, BlockSparseAttention, MiniMaxH3SigmaShift, ConditioningZeroOut, MiniMaxH3ReferenceToVideo, GetNode, Reroute, LoadImage, LoadImage, Text, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, SelfLiftH3Sampler, KSamplerSelect, BasicScheduler, GetNode, MarkdownNote, LoadImage, GoohaiUniversalSlider, LoadAudio, LoadAudio, ResolutionSelector, PrimitiveFloat, MiniMaxChunkFeedForward, Note, MiniMaxLowVRAMAttention]
patterns: []
missing: []
---

# 平台全量/MiniMax_H3 终极篇 motion_speed_slider_mmh3_v1.1文武双全_2117515243374075906.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax_H3 终极篇 motion_speed_slider_mmh3_v1.1文武双全_2117515243374075906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（101 个）：
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `忽略多组孤海`
- `Note`
- `SetNode`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `忽略多组孤海`
- `LoadImage`
- `忽略多组孤海`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `SetNode`
- `忽略多组孤海`
- `LoraLoaderModelOnly` ★核心
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `BlockSparseAttention`
- `MiniMaxH3SigmaShift`
- `ConditioningZeroOut`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `Text`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SelfLiftH3Sampler` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `MarkdownNote`
- `LoadImage`
- `GoohaiUniversalSlider`
- `LoadAudio`
- `LoadAudio`
- `ResolutionSelector`
- `PrimitiveFloat`
- `MiniMaxChunkFeedForward`
- `Note`
- `MiniMaxLowVRAMAttention`

## 知识

覆盖率 **47%**（47/101）

**有卡**：`LoadImage`、`VAELoader`、`VHS_LoadVideo`、`忽略多组孤海`、`LoadAudio`、`ModelAttentionBackend`、`ModelPreviewOverrideKJ`、`LoraLoaderModelOnly`、`ComfyMathExpression`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`VAEDecodeAudio`、`BlockSparseAttention`、`MiniMaxH3SigmaShift`、`ConditioningZeroOut`、`MiniMaxH3ReferenceToVideo`、`Text`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`KSamplerSelect`、`BasicScheduler`、`GoohaiUniversalSlider`、`ResolutionSelector`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
