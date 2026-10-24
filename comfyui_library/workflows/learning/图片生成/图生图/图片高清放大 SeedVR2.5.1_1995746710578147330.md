---
key: 图片生成/图生图/图片高清放大 SeedVR2.5.1_1995746710578147330.json
name: 图片高清放大 SeedVR2.5.1_1995746710578147330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片高清放大 SeedVR2.5.1_1995746710578147330.json
hash: 8c467575b5e04bd5
coverage: 0.7
learned_at: 2026-10-23 12:42:02
nodes: [PreviewImage, SeedVR2LoadDiTModel, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), LoadImage, Note, ImpactInt]
patterns: []
missing: []
---

# 图片生成/图生图/图片高清放大 SeedVR2.5.1_1995746710578147330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片高清放大 SeedVR2.5.1_1995746710578147330.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Note`
- `ImpactInt`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`LoadImage`、`ImpactInt`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、ImpactInt、sd15-t2i-basic
