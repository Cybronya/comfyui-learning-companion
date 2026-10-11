---
key: 视频生成/文生视频/一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153.json
name: 一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153.json
hash: 27d839915ac4fab5
coverage: 0.45679
learned_at: 2026-10-11 21:19:52
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadAudio, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, KSamplerSelect, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, VAEEncode, PT_H3ConcatAVLatent, RandomNoise, SetNode, SetNode, SetNode, RandomNoise, SetNode, BasicGuider, KSamplerSelect, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), SetNode, LoadImage, ImageFromBatch, ResolutionSelector, BasicGuider, VHS_VideoCombine, CLIPLoader, VAELoader, VAELoader, SetNode, SetNode, ComfyMathExpression, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, ImageResizeKJv2, ResolutionSelector, MiniMaxH3ReferenceToVideo, BasicScheduler, LoraLoaderBypassModelOnly, BasicScheduler, MarkdownNote, CR Prompt Text, ImageFromBatch, ImageFromBatch, LoadImage, VHS_LoadVideo]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153.json`

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
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
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
- `BasicScheduler`
- `LoraLoaderBypassModelOnly` ★核心
- `BasicScheduler`
- `MarkdownNote`
- `CR Prompt Text`
- `ImageFromBatch`
- `ImageFromBatch`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **46%**（37/81）

**有卡**：`LoadAudio`、`VHS_VideoCombine`、`KSamplerSelect`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`VAEEncode`、`PT_H3ConcatAVLatent`、`RandomNoise`、`BasicGuider`、`LoadImage`、`ImageFromBatch`、`ResolutionSelector`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ImageResizeKJv2`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`LoraLoaderBypassModelOnly`、`VHS_LoadVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEEncode

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
