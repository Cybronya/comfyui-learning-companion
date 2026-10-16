---
key: 视频生成/图生视频/Wan3.0图生视频-带音效AI视频生成工作流_2094296509524307969.json
name: Wan3.0图生视频-带音效AI视频生成工作流_2094296509524307969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan3.0图生视频-带音效AI视频生成工作流_2094296509524307969.json
hash: ecd4c7ecd2bc1e3c
coverage: 0.875
learned_at: 2026-10-16 23:42:31
nodes: [LoadImage, PrimitiveStringMultiline, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, RHMiniMaxH3VideoGen, CreateVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan3.0图生视频-带音效AI视频生成工作流_2094296509524307969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan3.0图生视频-带音效AI视频生成工作流_2094296509524307969.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `RHMiniMaxH3ModelLoader`
- `RHMiniMaxH3TextEncoderLoader`
- `RHMiniMaxH3VAELoader`
- `RHMiniMaxH3VideoGen`
- `CreateVideo`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LoadImage`、`SaveVideo`、`RHMiniMaxH3ModelLoader`、`RHMiniMaxH3TextEncoderLoader`、`RHMiniMaxH3VAELoader`、`RHMiniMaxH3VideoGen`、`CreateVideo`

**用到的条目**：LoadImage、RHMiniMaxH3TextEncoderLoader、RHMiniMaxH3VAELoader、SaveVideo、CreateVideo、RHMiniMaxH3ModelLoader、RHMiniMaxH3VideoGen、sd15-t2i-basic
