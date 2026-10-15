---
key: 视频生成/文生视频/ComfyUI-RH-daVinci-MagiHuman 基础工作流_2037582254259572738.json
name: ComfyUI-RH-daVinci-MagiHuman 基础工作流_2037582254259572738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ComfyUI-RH-daVinci-MagiHuman 基础工作流_2037582254259572738.json
hash: 642905b440e91c82
coverage: 0.714286
learned_at: 2026-10-15 22:44:06
nodes: [RH_MagiHumanModelLoader, SaveVideo, RH_MagiHumanGenerate, PreviewAny, LoadImage, RH_LLMAPI_Pro_Node, JjkText]
patterns: []
missing: []
---

# 视频生成/文生视频/ComfyUI-RH-daVinci-MagiHuman 基础工作流_2037582254259572738.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ComfyUI-RH-daVinci-MagiHuman 基础工作流_2037582254259572738.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（7 个）：
- `RH_MagiHumanModelLoader`
- `SaveVideo`
- `RH_MagiHumanGenerate`
- `PreviewAny`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `JjkText`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`RH_MagiHumanModelLoader`、`SaveVideo`、`RH_MagiHumanGenerate`、`LoadImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoadImage、SaveVideo、RH_LLMAPI_Pro_Node、RH_MagiHumanGenerate、RH_MagiHumanModelLoader、sd15-t2i-basic、sd15-t2i-lora、node
