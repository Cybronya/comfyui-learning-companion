---
key: 视频生成/图生视频/202610-minimax-h3-导演台-V2.0_2109257515652444161.json
name: 202610-minimax-h3-导演台-V2.0_2109257515652444161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/202610-minimax-h3-导演台-V2.0_2109257515652444161.json
hash: fe15d12d81a6fd65
coverage: 0.916667
learned_at: 2026-10-30 17:57:10
nodes: [VAELoader, CreateVideo, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, CLIPLoader, SolAttnMiniMax, MarkdownNote, ModelAttentionBackend, LoraLoaderModelOnly, SaveVideo, UNETLoader, MiniMaxH3Director]
patterns: []
missing: []
---

# 视频生成/图生视频/202610-minimax-h3-导演台-V2.0_2109257515652444161.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/202610-minimax-h3-导演台-V2.0_2109257515652444161.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（12 个）：
- `VAELoader`
- `CreateVideo`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `CLIPLoader`
- `SolAttnMiniMax`
- `MarkdownNote`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `UNETLoader` ★核心
- `MiniMaxH3Director`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`VAELoader`、`CreateVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CLIPLoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`SaveVideo`、`UNETLoader`、`MiniMaxH3Director`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、SaveVideo、CreateVideo、MiniMaxH3MemoryEfficientSageAttentionPatch、ModelAttentionBackend
