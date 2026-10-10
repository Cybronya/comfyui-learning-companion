---
key: 视频生成/图生视频/Seedance2.0过场动画-多参考转场视频工作流_2094425486511398914.json
name: Seedance2.0过场动画-多参考转场视频工作流_2094425486511398914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Seedance2.0过场动画-多参考转场视频工作流_2094425486511398914.json
hash: 7ff44f55a77cc4b7
coverage: 0.888889
learned_at: 2026-10-10 22:54:16
nodes: [PrimitiveStringMultiline, LoadImage, LoadImage, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, RHMiniMaxH3RefGen, CreateVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Seedance2.0过场动画-多参考转场视频工作流_2094425486511398914.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Seedance2.0过场动画-多参考转场视频工作流_2094425486511398914.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（9 个）：
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
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
