---
key: 视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-AI短剧创作.json
name: MiniMax-H3-视频换背景-视频编辑-AI短剧创作
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-AI短剧创作.json
hash: d1052c5f03db2d37
coverage: 0.793103
learned_at: 2026-10-15 22:49:16
nodes: [PrimitiveFloat, SamplerCustomAdvanced, GetNode, ImageConcanate, LayerUtility: PurgeVRAM V2, BasicScheduler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, VHS_VideoCombine, SetNode, VRAM_Debug, RandomNoise, SetNode, GetNode, VAELoader, CLIPLoader, BasicGuider, KSamplerSelect, ComfyMathExpression, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, MiniMaxH3ReferenceToVideo, VHS_LoadVideo, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-AI短剧创作.json

> 来源文件 `comfyui_library/workflows/视频生成/视频生视频/MiniMax-H3-视频换背景-视频编辑-AI短剧创作.json`

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

覆盖率 **79%**（23/29）

**有卡**：`SamplerCustomAdvanced`、`ImageConcanate`、`LayerUtility: PurgeVRAM V2`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`VRAM_Debug`、`RandomNoise`、`VAELoader`、`CLIPLoader`、`BasicGuider`、`KSamplerSelect`、`ComfyMathExpression`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
