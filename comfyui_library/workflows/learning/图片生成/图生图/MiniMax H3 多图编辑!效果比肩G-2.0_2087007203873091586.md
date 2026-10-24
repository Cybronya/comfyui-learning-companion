---
key: 图片生成/图生图/MiniMax H3 多图编辑!效果比肩G-2.0_2087007203873091586.json
name: MiniMax H3 多图编辑!效果比肩G-2.0_2087007203873091586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/MiniMax H3 多图编辑!效果比肩G-2.0_2087007203873091586.json
hash: a380c2cb9562800a
coverage: 0.958333
learned_at: 2026-10-23 11:09:21
nodes: [VAELoader, PathchSageAttentionKJ, EasyCache, CLIPLoader, VAEDecode, KSamplerSelect, BasicScheduler, VAELoader, MiniMaxH3ReferenceToVideo, BasicGuider, RandomNoise, MiniMaxH3MemoryEfficientSageAttentionPatch, SamplerCustomAdvanced, ImageFromBatch, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, LoadImage, LoadImage, LoadImage, SaveImage, ResolutionSelector, JjkText, SaveImage, UNETLoader]
patterns: []
missing: []
---

# 图片生成/图生图/MiniMax H3 多图编辑!效果比肩G-2.0_2087007203873091586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/MiniMax H3 多图编辑!效果比肩G-2.0_2087007203873091586.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAELoader`
- `PathchSageAttentionKJ`
- `EasyCache`
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `BasicGuider`
- `RandomNoise`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SamplerCustomAdvanced` ★核心
- `ImageFromBatch`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `ResolutionSelector`
- `JjkText`
- `SaveImage`
- `UNETLoader` ★核心

## 知识

覆盖率 **96%**（23/24）

**有卡**：`VAELoader`、`PathchSageAttentionKJ`、`EasyCache`、`CLIPLoader`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`MiniMaxH3ReferenceToVideo`、`BasicGuider`、`RandomNoise`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SamplerCustomAdvanced`、`ImageFromBatch`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`LoadImage`、`SaveImage`、`ResolutionSelector`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
