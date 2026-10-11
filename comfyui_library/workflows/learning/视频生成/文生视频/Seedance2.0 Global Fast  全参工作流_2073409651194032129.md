---
key: 视频生成/文生视频/Seedance2.0 Global Fast  全参工作流_2073409651194032129.json
name: Seedance2.0 Global Fast  全参工作流_2073409651194032129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.0 Global Fast  全参工作流_2073409651194032129.json
hash: 7503c6b642f08e43
coverage: 0.894737
learned_at: 2026-10-11 20:38:42
nodes: [PreviewAny, PreviewAny, LoadVideo, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadVideo, LoadVideo, RH_BytedanceSeedance20GlobalFastMultimodalVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/Seedance2.0 Global Fast  全参工作流_2073409651194032129.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.0 Global Fast  全参工作流_2073409651194032129.json`

## 结构

**生成流程**：Output → Other

**节点**（19 个）：
- `PreviewAny`
- `PreviewAny`
- `LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadVideo`
- `LoadVideo`
- `RH_BytedanceSeedance20GlobalFastMultimodalVideo`
- `SaveVideo`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`LoadVideo`、`LoadAudio`、`LoadImage`、`RH_BytedanceSeedance20GlobalFastMultimodalVideo`、`SaveVideo`

**用到的条目**：LoadImage、RH_BytedanceSeedance20GlobalFastMultimodalVideo、SaveVideo、LoadAudio、LoadVideo、sd15-t2i-basic、sd15-t2i-lora、Seed
