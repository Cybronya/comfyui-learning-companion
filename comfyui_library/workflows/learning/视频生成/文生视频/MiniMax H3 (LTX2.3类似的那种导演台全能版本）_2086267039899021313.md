---
key: 视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json
name: MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json
hash: 1f84aadf1e62dcb9
coverage: 0.75
learned_at: 2026-10-11 20:53:39
nodes: [CLIPLoader, VAELoader, VAELoader, PreviewAny, CreateVideo, MarkdownNote, SaveVideo, UNETLoader, PathchSageAttentionKJ, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, MiniMaxH3Director]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 (LTX2.3类似的那种导演台全能版本）_2086267039899021313.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（12 个）：
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PreviewAny`
- `CreateVideo`
- `MarkdownNote`
- `SaveVideo`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `MiniMaxH3Director`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`CLIPLoader`、`VAELoader`、`CreateVideo`、`SaveVideo`、`UNETLoader`、`PathchSageAttentionKJ`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3Director`

**用到的条目**：VAELoader、CLIPLoader、UNETLoader、SaveVideo、CreateVideo、MiniMaxH3MemoryEfficientSageAttentionPatch、PathchSageAttentionKJ、MiniMaxH3Director
