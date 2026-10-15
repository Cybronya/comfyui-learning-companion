---
key: 视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json
name: MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 导演台-双采-Latent Upscaler-SLA加速_2092859264619597825.json
hash: 6554d3d097d08750
coverage: 0.896552
learned_at: 2026-10-15 22:45:39
nodes: [VAELoader, VAELoader, MarkdownNote, PathchSageAttentionKJ, CLIPLoader, PreviewAny, CreateVideo, SaveVideo, CreateVideo, MiniMaxH3Director, UNETLoader, UNETLoader, UNETLoader, LoraLoaderBypassModelOnly, ModelAttentionBackend, SolAttnMiniMax, EasyCache, SaveVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, MarkdownNote, MiniMaxH3DirectorRefine, MiniMaxH3DirectorRefine, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, easy anythingIndexSwitch]
patterns: []
missing: []
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

覆盖率 **90%**（26/29）

**有卡**：`VAELoader`、`PathchSageAttentionKJ`、`CLIPLoader`、`CreateVideo`、`SaveVideo`、`MiniMaxH3Director`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`ModelAttentionBackend`、`SolAttnMiniMax`、`EasyCache`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`MiniMaxH3DirectorRefine`、`LoraLoaderModelOnly`、`easy anythingIndexSwitch`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、LoraLoaderBypassModelOnly、SaveVideo、BasicScheduler、CreateVideo
