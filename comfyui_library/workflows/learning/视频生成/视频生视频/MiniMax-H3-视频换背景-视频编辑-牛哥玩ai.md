---
key: 视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-牛哥玩ai.json
name: MiniMax-H3-视频换背景-视频编辑-牛哥玩ai
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-牛哥玩ai.json
hash: ee39f12a3205c6a7
coverage: 0.758621
learned_at: 2026-10-07 00:37:57
nodes: [PrimitiveFloat, SamplerCustomAdvanced, GetNode, ImageConcanate, LayerUtility: PurgeVRAM V2, BasicScheduler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, VHS_VideoCombine, SetNode, VRAM_Debug, RandomNoise, SetNode, GetNode, VAELoader, CLIPLoader, BasicGuider, KSamplerSelect, ComfyMathExpression, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, MiniMaxH3ReferenceToVideo, VHS_LoadVideo, PrimitiveStringMultiline]
patterns: []
missing: [LayerUtility: PurgeVRAM V2]
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-牛哥玩ai.json

> 来源文件 `comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-牛哥玩ai.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（29 个）：
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM V2`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `VRAM_Debug`
- `RandomNoise`
- `SetNode`
- `GetNode`
- `VAELoader`
- `CLIPLoader`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `VHS_LoadVideo`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`SamplerCustomAdvanced`、`ImageConcanate`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`VRAM_Debug`、`RandomNoise`、`VAELoader`、`CLIPLoader`、`BasicGuider`、`KSamplerSelect`、`ComfyMathExpression`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`VHS_LoadVideo`

**缺卡**（1）：`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
