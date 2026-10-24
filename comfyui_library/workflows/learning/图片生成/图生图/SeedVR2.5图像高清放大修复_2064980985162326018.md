---
key: 图片生成/图生图/SeedVR2.5图像高清放大修复_2064980985162326018.json
name: SeedVR2.5图像高清放大修复_2064980985162326018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5图像高清放大修复_2064980985162326018.json
hash: f59f608fc697ccbd
coverage: 0.538462
learned_at: 2026-10-23 11:25:06
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, INTConstant, Note, Note, Note, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, MarkdownNote, Image Comparer (rgthree), SaveImage, PreviewImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5图像高清放大修复_2064980985162326018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5图像高清放大修复_2064980985162326018.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（13 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `LoadImage`

## 知识

覆盖率 **54%**（7/13）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`INTConstant`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、INTConstant、sd15-t2i-basic
