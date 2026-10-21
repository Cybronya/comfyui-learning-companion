---
key: 图片生成/文生图/lora1.0，match，二采0.35，一采turbo4_2092441692577288193.json
name: lora1.0，match，二采0.35，一采turbo4_2092441692577288193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/lora1.0，match，二采0.35，一采turbo4_2092441692577288193.json
hash: d513e1f2ae266caf
coverage: 0.469136
learned_at: 2026-10-20 01:19:46
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadAudio, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, KSamplerSelect, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, VAEEncode, PT_H3ConcatAVLatent, RandomNoise, SetNode, SetNode, SetNode, SetNode, BasicGuider, KSamplerSelect, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), SetNode, LoadImage, LoadImage, ImageFromBatch, ResolutionSelector, BasicGuider, VHS_VideoCombine, CLIPLoader, VAELoader, VAELoader, SetNode, SetNode, ComfyMathExpression, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, ImageResizeKJv2, ResolutionSelector, MiniMaxH3ReferenceToVideo, MarkdownNote, ImageFromBatch, ImageFromBatch, BasicScheduler, RandomNoise, BasicScheduler, LoraLoaderBypassModelOnly, VHS_LoadVideo, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/文生图/lora1.0，match，二采0.35，一采turbo4_2092441692577288193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/lora1.0，match，二采0.35，一采turbo4_2092441692577288193.json`

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
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `ImageFromBatch`
- `ResolutionSelector`
- `BasicGuider`
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `ImageResizeKJv2`
- `ResolutionSelector`
- `MiniMaxH3ReferenceToVideo`
- `MarkdownNote`
- `ImageFromBatch`
- `ImageFromBatch`
- `BasicScheduler`
- `RandomNoise`
- `BasicScheduler`
- `LoraLoaderBypassModelOnly` ★核心
- `VHS_LoadVideo`
- `CR Prompt Text`

## 知识

覆盖率 **47%**（38/81）

**有卡**：`LoadAudio`、`VHS_VideoCombine`、`KSamplerSelect`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`VAEEncode`、`PT_H3ConcatAVLatent`、`RandomNoise`、`BasicGuider`、`LoadImage`、`ImageFromBatch`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ImageResizeKJv2`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`LoraLoaderBypassModelOnly`、`VHS_LoadVideo`、`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEEncode
