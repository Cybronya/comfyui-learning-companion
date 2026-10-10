---
key: 视频生成/图生视频/Seedance2.5图生视频工作流｜一张图动起来最长30秒_2095480606539997185.json
name: Seedance2.5图生视频工作流｜一张图动起来最长30秒_2095480606539997185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Seedance2.5图生视频工作流｜一张图动起来最长30秒_2095480606539997185.json
hash: a42018bb5a3361f0
coverage: 0.875
learned_at: 2026-10-10 22:54:17
nodes: [LoadImage, PrimitiveStringMultiline, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, CreateVideo, RHMiniMaxH3VideoGen]
patterns: []
missing: []
---

# 视频生成/图生视频/Seedance2.5图生视频工作流｜一张图动起来最长30秒_2095480606539997185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Seedance2.5图生视频工作流｜一张图动起来最长30秒_2095480606539997185.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `RHMiniMaxH3ModelLoader`
- `RHMiniMaxH3TextEncoderLoader`
- `RHMiniMaxH3VAELoader`
- `CreateVideo`
- `RHMiniMaxH3VideoGen`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LoadImage`、`SaveVideo`、`RHMiniMaxH3ModelLoader`、`RHMiniMaxH3TextEncoderLoader`、`RHMiniMaxH3VAELoader`、`CreateVideo`、`RHMiniMaxH3VideoGen`

**用到的条目**：LoadImage、RHMiniMaxH3TextEncoderLoader、RHMiniMaxH3VAELoader、SaveVideo、CreateVideo、RHMiniMaxH3ModelLoader、RHMiniMaxH3VideoGen、sd15-t2i-basic
