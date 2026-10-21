---
key: 图片生成/图生图/image2.5异步循环批量出layout_2108376170386513922.json
name: image2.5异步循环批量出layout_2108376170386513922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image2.5异步循环批量出layout_2108376170386513922.json
hash: f668adb4505501d2
coverage: 0.666667
learned_at: 2026-10-21 00:45:30
nodes: [easy forLoopEnd, easy batchAnything, PreviewImage, ImageScale, LoadImage, RHUploadZip, PreviewAny, PreviewImage, SaveImage, RH_LLMAPI_Pro_Node, ShowText|pysssss, RH_RhartImageG25SunburstImageToImage, RH_RhartImageG2OfficialImageToImage, PreviewImage, PreviewImage, easy forLoopStart, BatchCount+, RHExtractImage]
patterns: []
missing: []
---

# 图片生成/图生图/image2.5异步循环批量出layout_2108376170386513922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image2.5异步循环批量出layout_2108376170386513922.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（18 个）：
- `easy forLoopEnd`
- `easy batchAnything`
- `PreviewImage`
- `ImageScale`
- `LoadImage`
- `RHUploadZip`
- `PreviewAny`
- `PreviewImage`
- `SaveImage`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `RH_RhartImageG25SunburstImageToImage`
- `RH_RhartImageG2OfficialImageToImage`
- `PreviewImage`
- `PreviewImage`
- `easy forLoopStart`
- `BatchCount+`
- `RHExtractImage`

## 知识

覆盖率 **67%**（12/18）

**有卡**：`easy forLoopEnd`、`easy batchAnything`、`ImageScale`、`LoadImage`、`RHUploadZip`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`RH_RhartImageG25SunburstImageToImage`、`RH_RhartImageG2OfficialImageToImage`、`easy forLoopStart`、`BatchCount+`、`RHExtractImage`

**用到的条目**：LoadImage、SaveImage、ImageScale、RH_LLMAPI_Pro_Node、RH_RhartImageG25SunburstImageToImage、RH_RhartImageG2OfficialImageToImage、RHUploadZip、RHExtractImage
