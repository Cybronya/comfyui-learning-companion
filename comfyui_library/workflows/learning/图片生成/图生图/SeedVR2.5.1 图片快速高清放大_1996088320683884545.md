---
key: 图片生成/图生图/SeedVR2.5.1 图片快速高清放大_1996088320683884545.json
name: SeedVR2.5.1 图片快速高清放大_1996088320683884545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5.1 图片快速高清放大_1996088320683884545.json
hash: fbd4dff65a5481ae
coverage: 0.777778
learned_at: 2026-10-23 11:25:00
nodes: [SaveImage, SeedVR2LoadVAEModel, PreviewImage, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, ImageScaleToTotalPixels, Image Comparer (rgthree), ImpactInt, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5.1 图片快速高清放大_1996088320683884545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5.1 图片快速高清放大_1996088320683884545.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `LoadImage`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`ImpactInt`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、ImpactInt、sd15-t2i-basic
