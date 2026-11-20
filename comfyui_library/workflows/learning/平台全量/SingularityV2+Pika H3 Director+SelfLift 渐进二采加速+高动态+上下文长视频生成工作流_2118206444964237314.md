---
key: 平台全量/SingularityV2+Pika H3 Director+SelfLift 渐进二采加速+高动态+上下文长视频生成工作流_2118206444964237314.json
name: SingularityV2+Pika H3 Director+SelfLift 渐进二采加速+高动态+上下文长视频生成工作流_2118206444964237314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SingularityV2+Pika H3 Director+SelfLift 渐进二采加速+高动态+上下文长视频生成工作流_2118206444964237314.json
hash: ead2888376293d4f
coverage: 0.864865
learned_at: 2026-11-14 01:00:41
nodes: [CLIPLoader, VAELoader, VAELoader, PreviewAny, MarkdownNote, MiniMaxH3MemoryEfficientSageAttentionPatch, CreateVideo, CreateVideo, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, SaveVideo, SaveVideo, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3Director, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3DirectorSelfLift, SetNode, GetNode, H3SigmaRefiner, Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/SingularityV2+Pika H3 Director+SelfLift 渐进二采加速+高动态+上下文长视频生成工作流_2118206444964237314.json

> 来源文件 `comfyui_library/workflows/平台全量/SingularityV2+Pika H3 Director+SelfLift 渐进二采加速+高动态+上下文长视频生成工作流_2118206444964237314.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PreviewAny`
- `MarkdownNote`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `CreateVideo`
- `CreateVideo`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `SaveVideo`
- `SaveVideo`
- `BasicScheduler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3Director`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3DirectorSelfLift`
- `SetNode`
- `GetNode`
- `H3SigmaRefiner`
- `Label (rgthree)`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CreateVideo`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`SaveVideo`、`BasicScheduler`、`MiniMaxH3Director`、`MiniMaxH3DirectorSelfLift`、`H3SigmaRefiner`、`Label (rgthree)`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、SaveVideo、BasicScheduler、CreateVideo、H3SigmaRefiner
