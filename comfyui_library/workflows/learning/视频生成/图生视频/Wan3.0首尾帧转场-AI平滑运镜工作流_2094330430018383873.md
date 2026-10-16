---
key: 视频生成/图生视频/Wan3.0首尾帧转场-AI平滑运镜工作流_2094330430018383873.json
name: Wan3.0首尾帧转场-AI平滑运镜工作流_2094330430018383873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan3.0首尾帧转场-AI平滑运镜工作流_2094330430018383873.json
hash: 1fff28f501f5a1f1
coverage: 0.888889
learned_at: 2026-10-16 23:42:31
nodes: [LoadImage, LoadImage, PrimitiveStringMultiline, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, RHMiniMaxH3VideoGen, CreateVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan3.0首尾帧转场-AI平滑运镜工作流_2094330430018383873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan3.0首尾帧转场-AI平滑运镜工作流_2094330430018383873.json`

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
- `RHMiniMaxH3VideoGen`
- `CreateVideo`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`LoadImage`、`SaveVideo`、`RHMiniMaxH3ModelLoader`、`RHMiniMaxH3TextEncoderLoader`、`RHMiniMaxH3VAELoader`、`RHMiniMaxH3VideoGen`、`CreateVideo`

**用到的条目**：LoadImage、RHMiniMaxH3TextEncoderLoader、RHMiniMaxH3VAELoader、SaveVideo、CreateVideo、RHMiniMaxH3ModelLoader、RHMiniMaxH3VideoGen、sd15-t2i-basic
