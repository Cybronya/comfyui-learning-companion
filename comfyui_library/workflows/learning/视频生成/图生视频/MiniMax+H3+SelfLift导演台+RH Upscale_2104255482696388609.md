---
key: 视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json
name: MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json
hash: ed50aa40d5296747
coverage: 0.852941
learned_at: 2026-10-17 02:43:56
nodes: [VAELoader, PreviewAny, MiniMaxH3DirectorFaceRefine, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelAttentionBackend, LoraLoaderModelOnly, GetImageSize, PreviewAny, PreviewAny, SaveImage, MarkdownNote, UNETLoader, CreateVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3ChunkFeedForwardT8Advanced, kkVideoFirstLastFrames, SaveVideo, SaveVideo, Astra, easy imageChooser, PlaySound|pysssss, RH_Upscale, MiniMaxH3Director, MiniMaxH3DirectorSelfLift]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（34 个）：
- `VAELoader`
- `PreviewAny`
- `MiniMaxH3DirectorFaceRefine`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `PreviewAny`
- `PreviewAny`
- `SaveImage`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ChunkFeedForwardT8Advanced`
- `kkVideoFirstLastFrames`
- `SaveVideo`
- `SaveVideo`
- `Astra`
- `easy imageChooser`
- `PlaySound|pysssss`
- `RH_Upscale`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorSelfLift`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`VAELoader`、`MiniMaxH3DirectorFaceRefine`、`LoraLoaderBypassModelOnly`、`LoraLoaderModelOnly`、`CLIPLoader`、`ModelAttentionBackend`、`GetImageSize`、`SaveImage`、`UNETLoader`、`CreateVideo`、`MiniMaxH3ChunkFeedForwardT8Advanced`、`kkVideoFirstLastFrames`、`SaveVideo`、`Astra`、`easy imageChooser`、`PlaySound|pysssss`、`RH_Upscale`、`MiniMaxH3Director`、`MiniMaxH3DirectorSelfLift`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、LoraLoaderBypassModelOnly、RH_Upscale、GetImageSize、GetImageSize
