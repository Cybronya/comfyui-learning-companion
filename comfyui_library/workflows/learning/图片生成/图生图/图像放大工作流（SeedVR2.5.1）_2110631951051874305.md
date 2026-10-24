---
key: 图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json
name: 图像放大工作流（SeedVR2.5.1）_2110631951051874305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json
hash: 6d2f4cac45e1b414
coverage: 0.636364
learned_at: 2026-10-23 12:38:40
nodes: [SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, PreviewImage, LoadImage, Note, SeedVR2LoadDiTModel, VRAM_Debug, Image Comparer (rgthree), Note, SaveImage, ImageScaleToTotalPixels]
patterns: []
missing: []
---

# 图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像放大工作流（SeedVR2.5.1）_2110631951051874305.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（11 个）：
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `LoadImage`
- `Note`
- `SeedVR2LoadDiTModel`
- `VRAM_Debug`
- `Image Comparer (rgthree)`
- `Note`
- `SaveImage`
- `ImageScaleToTotalPixels`

## 知识

覆盖率 **64%**（7/11）

**有卡**：`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`LoadImage`、`SeedVR2LoadDiTModel`、`VRAM_Debug`、`SaveImage`、`ImageScaleToTotalPixels`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、VRAM_Debug、sd15-t2i-basic
