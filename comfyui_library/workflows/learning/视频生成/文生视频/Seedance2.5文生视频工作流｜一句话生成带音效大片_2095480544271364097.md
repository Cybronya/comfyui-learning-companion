---
key: 视频生成/文生视频/Seedance2.5文生视频工作流｜一句话生成带音效大片_2095480544271364097.json
name: Seedance2.5文生视频工作流｜一句话生成带音效大片_2095480544271364097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.5文生视频工作流｜一句话生成带音效大片_2095480544271364097.json
hash: 716f7285cde3764c
coverage: 0.857143
learned_at: 2026-10-10 23:05:33
nodes: [PrimitiveStringMultiline, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, RHMiniMaxH3VideoGen, CreateVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/Seedance2.5文生视频工作流｜一句话生成带音效大片_2095480544271364097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.5文生视频工作流｜一句话生成带音效大片_2095480544271364097.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（7 个）：
- `PrimitiveStringMultiline`
- `SaveVideo`
- `RHMiniMaxH3ModelLoader`
- `RHMiniMaxH3TextEncoderLoader`
- `RHMiniMaxH3VAELoader`
- `RHMiniMaxH3VideoGen`
- `CreateVideo`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`SaveVideo`、`RHMiniMaxH3ModelLoader`、`RHMiniMaxH3TextEncoderLoader`、`RHMiniMaxH3VAELoader`、`RHMiniMaxH3VideoGen`、`CreateVideo`

**用到的条目**：RHMiniMaxH3TextEncoderLoader、RHMiniMaxH3VAELoader、SaveVideo、CreateVideo、RHMiniMaxH3ModelLoader、RHMiniMaxH3VideoGen、sd15-t2i-basic、sd15-t2i-lora
