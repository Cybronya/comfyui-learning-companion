---
key: 图片生成/图生图/常用抠图工作流RMBG-2.0_2035960868583776257.json
name: 常用抠图工作流RMBG-2.0_2035960868583776257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/常用抠图工作流RMBG-2.0_2035960868583776257.json
hash: 908562631d50e7b3
coverage: 0.909091
learned_at: 2026-10-23 12:50:43
nodes: [SaveImage, RMBG, LayerMask: MaskPreview, LoadImage, AILab_ColorInput, LoadImage, AILab_ColorInput, SAM3Segment, LayerMask: MaskPreview, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/常用抠图工作流RMBG-2.0_2035960868583776257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/常用抠图工作流RMBG-2.0_2035960868583776257.json`

## 结构

**生成流程**：Output → Other

**节点**（11 个）：
- `SaveImage`
- `RMBG`
- `LayerMask: MaskPreview`
- `LoadImage`
- `AILab_ColorInput`
- `LoadImage`
- `AILab_ColorInput`
- `SAM3Segment`
- `LayerMask: MaskPreview`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`SaveImage`、`RMBG`、`LayerMask: MaskPreview`、`LoadImage`、`AILab_ColorInput`、`SAM3Segment`

**用到的条目**：LoadImage、SaveImage、LayerMask: MaskPreview、RMBG、SAM3Segment、AILab_ColorInput、sd15-t2i-basic、sd15-t2i-lora
