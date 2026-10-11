---
key: 视频生成/文生视频/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2098339836649369602.json
name: 视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2098339836649369602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2098339836649369602.json
hash: 44d7177666967720
coverage: 1
learned_at: 2026-10-11 21:42:03
nodes: [VHS_LoadVideo, SubtitleDetectorRapidOCR, SubtitleEraserProPainter, FlashVSRNode, CreateVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2098339836649369602.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2098339836649369602.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `VHS_LoadVideo`
- `SubtitleDetectorRapidOCR`
- `SubtitleEraserProPainter`
- `FlashVSRNode`
- `CreateVideo`
- `SaveVideo`

## 知识

覆盖率 **100%**（6/6）

**有卡**：`VHS_LoadVideo`、`SubtitleDetectorRapidOCR`、`SubtitleEraserProPainter`、`FlashVSRNode`、`CreateVideo`、`SaveVideo`

**用到的条目**：SaveVideo、CreateVideo、VHS_LoadVideo、FlashVSRNode、SubtitleDetectorRapidOCR、SubtitleEraserProPainter、sd15-t2i-basic、sd15-t2i-lora
