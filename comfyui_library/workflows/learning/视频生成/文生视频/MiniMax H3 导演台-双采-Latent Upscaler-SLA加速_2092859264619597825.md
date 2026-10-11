---
key: 视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json
name: MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json
hash: 6554d3d097d08750
coverage: 0.862069
learned_at: 2026-10-11 21:30:21
nodes: [VAELoader, VAELoader, MarkdownNote, PathchSageAttentionKJ, CLIPLoader, PreviewAny, CreateVideo, SaveVideo, CreateVideo, MiniMaxH3Director, UNETLoader, UNETLoader, UNETLoader, LoraLoaderBypassModelOnly, ModelAttentionBackend, SolAttnMiniMax, EasyCache, SaveVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, MarkdownNote, MiniMaxH3DirectorRefine, MiniMaxH3DirectorRefine, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, easy anythingIndexSwitch]
patterns: []
missing: [easy anythingIndexSwitch]
discoveries: [次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（29 个）：
- `VAELoader`
- `VAELoader`
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `PreviewAny`
- `CreateVideo`
- `SaveVideo`
- `CreateVideo`
- `MiniMaxH3Director`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `EasyCache`
- `SaveVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `MarkdownNote`
- `MiniMaxH3DirectorRefine`
- `MiniMaxH3DirectorRefine`
- `BasicScheduler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy anythingIndexSwitch`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`VAELoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`CreateVideo`、`SaveVideo`、`MiniMaxH3Director`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`ModelAttentionBackend`、`SolAttnMiniMax`、`EasyCache`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`MiniMaxH3DirectorRefine`、`LoraLoaderModelOnly`

**缺卡**（1）：`easy anythingIndexSwitch`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、LoraLoaderBypassModelOnly、SaveVideo、BasicScheduler、CreateVideo

## 学习发现

- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
