---
key: 平台全量/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2095203326672592897.json
name: 视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2095203326672592897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2095203326672592897.json
hash: b06b12b7f84890f5
coverage: 0.818182
learned_at: 2026-11-14 02:36:16
nodes: [VHS_LoadVideo, CreateVideo, PrimitiveFloat, PrimitiveFloat, Video Slice, GetVideoComponents, SubtitleDetectorRapidOCR, SubtitleEraserProPainter, FlashVSRNode, CreateVideo, SaveVideo]
patterns: []
missing: []
---

# 平台全量/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2095203326672592897.json

> 来源文件 `comfyui_library/workflows/平台全量/视频去水印+超分工作流｜OCR+ProPainter+FlashVSR_2095203326672592897.json`

## 结构

**生成流程**：Output → Other

**节点**（11 个）：
- `VHS_LoadVideo`
- `CreateVideo`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Video Slice`
- `GetVideoComponents`
- `SubtitleDetectorRapidOCR`
- `SubtitleEraserProPainter`
- `FlashVSRNode`
- `CreateVideo`
- `SaveVideo`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`VHS_LoadVideo`、`CreateVideo`、`Video Slice`、`GetVideoComponents`、`SubtitleDetectorRapidOCR`、`SubtitleEraserProPainter`、`FlashVSRNode`、`SaveVideo`

**用到的条目**：SaveVideo、CreateVideo、FlashVSRNode、GetVideoComponents、SubtitleDetectorRapidOCR、SubtitleEraserProPainter、VHS_LoadVideo、Video Slice
