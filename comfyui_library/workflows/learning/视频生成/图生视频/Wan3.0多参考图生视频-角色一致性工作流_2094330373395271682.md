---
key: 视频生成/图生视频/Wan3.0多参考图生视频-角色一致性工作流_2094330373395271682.json
name: Wan3.0多参考图生视频-角色一致性工作流_2094330373395271682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan3.0多参考图生视频-角色一致性工作流_2094330373395271682.json
hash: 2d577a4aad7cf9da
coverage: 0.888889
learned_at: 2026-10-10 22:54:21
nodes: [LoadImage, LoadImage, PrimitiveStringMultiline, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, RHMiniMaxH3RefGen, CreateVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan3.0多参考图生视频-角色一致性工作流_2094330373395271682.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan3.0多参考图生视频-角色一致性工作流_2094330373395271682.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（9 个）：
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `RHMiniMaxH3ModelLoader`
- `RHMiniMaxH3TextEncoderLoader`
- `RHMiniMaxH3VAELoader`
- `RHMiniMaxH3RefGen`
- `CreateVideo`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`LoadImage`、`SaveVideo`、`RHMiniMaxH3ModelLoader`、`RHMiniMaxH3TextEncoderLoader`、`RHMiniMaxH3VAELoader`、`RHMiniMaxH3RefGen`、`CreateVideo`

**用到的条目**：LoadImage、RHMiniMaxH3TextEncoderLoader、RHMiniMaxH3VAELoader、SaveVideo、CreateVideo、RHMiniMaxH3RefGen、RHMiniMaxH3ModelLoader、sd15-t2i-basic
