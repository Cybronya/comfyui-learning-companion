---
key: 图片生成/文生图/一采lora1.0 turbo4 8步 0.5 match 二采8步0.3 -时长修正版_2092183943792648194.json
name: 一采lora1.0 turbo4 8步 0.5 match 二采8步0.3 -时长修正版_2092183943792648194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/一采lora1.0 turbo4 8步 0.5 match 二采8步0.3 -时长修正版_2092183943792648194.json
hash: ba3412a0aec45db5
coverage: 0.469136
learned_at: 2026-10-20 01:19:54
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadAudio, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, KSamplerSelect, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, VAEEncode, PT_H3ConcatAVLatent, SetNode, SetNode, SetNode, RandomNoise, SetNode, BasicGuider, KSamplerSelect, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, MiniMaxH3AVDecodeT8, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), SetNode, ImageFromBatch, ResolutionSelector, BasicGuider, VHS_VideoCombine, CLIPLoader, VAELoader, VAELoader, SetNode, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, ImageResizeKJv2, ResolutionSelector, MiniMaxH3ReferenceToVideo, MarkdownNote, ImageFromBatch, UNETLoader, CR Prompt Text, LoadImage, LoadImage, LoraLoaderBypassModelOnly, ComfyMathExpression, RandomNoise, BasicScheduler, SamplerCustomAdvanced, BasicScheduler, ImageFromBatch, VHS_LoadVideo]
patterns: []
missing: []
---

# 图片生成/文生图/一采lora1.0 turbo4 8步 0.5 match 二采8步0.3 -时长修正版_2092183943792648194.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/一采lora1.0 turbo4 8步 0.5 match 二采8步0.3 -时长修正版_2092183943792648194.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Process → Other

**节点**（81 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `PT_H3ConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `SetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MiniMaxH3AVDecodeT8`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `ImageFromBatch`
- `ResolutionSelector`
- `BasicGuider`
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `ImageResizeKJv2`
- `ResolutionSelector`
- `MiniMaxH3ReferenceToVideo`
- `MarkdownNote`
- `ImageFromBatch`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoraLoaderBypassModelOnly` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `ImageFromBatch`
- `VHS_LoadVideo`

## 知识

覆盖率 **47%**（38/81）

**有卡**：`LoadAudio`、`VHS_VideoCombine`、`KSamplerSelect`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`VAEEncode`、`PT_H3ConcatAVLatent`、`RandomNoise`、`BasicGuider`、`LoadImage`、`ImageFromBatch`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ImageResizeKJv2`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`CR Prompt Text`、`LoraLoaderBypassModelOnly`、`ComfyMathExpression`、`BasicScheduler`、`VHS_LoadVideo`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEEncode
