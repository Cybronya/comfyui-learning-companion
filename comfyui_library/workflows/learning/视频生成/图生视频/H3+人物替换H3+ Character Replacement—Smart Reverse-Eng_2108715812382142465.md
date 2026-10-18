---
key: 视频生成/图生视频/H3+人物替换H3+ Character Replacement—Smart Reverse-Eng_2108715812382142465.json
name: H3+人物替换H3+ Character Replacement—Smart Reverse-Eng_2108715812382142465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3+人物替换H3+ Character Replacement—Smart Reverse-Eng_2108715812382142465.json
hash: 4b204de8f3c45772
coverage: 0.521739
learned_at: 2026-10-17 22:49:35
nodes: [CLIPLoader, VAELoader, VAELoader, GetNode, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecodeAudio, CreateVideo, SetNode, MiniMaxH3ReferenceToVideo, BasicScheduler, GetNode, GetNode, SetNode, ComfyMathExpression, SetNode, MarkdownNote, SetNode, SetNode, SetNode, ResolutionSelector, SetNode, PrimitiveInt, GetNode, LoraLoaderModelOnly, VAEDecode, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, EasyCache, GetNode, SaveVideo, GetNode, MarkdownNote, LoadVideo, Fast Groups Bypasser (rgthree), MarkdownNote, RHHiddenNodes, easy showAnything, LoadImage, LoadImage, GetNode, VHS_LoadVideo, Fast Groups Bypasser (rgthree), PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/图生视频/H3+人物替换H3+ Character Replacement—Smart Reverse-Eng_2108715812382142465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3+人物替换H3+ Character Replacement—Smart Reverse-Eng_2108715812382142465.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `EasyCache`
- `GetNode`
- `SaveVideo`
- `GetNode`
- `MarkdownNote`
- `LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `RHHiddenNodes`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveFloat`

## 知识

覆盖率 **52%**（24/46）

**有卡**：`CLIPLoader`、`VAELoader`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`CreateVideo`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`ComfyMathExpression`、`ResolutionSelector`、`LoraLoaderModelOnly`、`VAEDecode`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`EasyCache`、`SaveVideo`、`LoadVideo`、`RHHiddenNodes`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
