---
key: 图片生成/图生图/SeedVR2.5.1图像双采超分辨率高清放大｜极致超清｜细节拉满｜高清放大_2112171175697801218.json
name: SeedVR2.5.1图像双采超分辨率高清放大｜极致超清｜细节拉满｜高清放大_2112171175697801218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5.1图像双采超分辨率高清放大｜极致超清｜细节拉满｜高清放大_2112171175697801218.json
hash: 64edc185c69e313e
coverage: 0.857143
learned_at: 2026-10-23 11:25:03
nodes: [ImageScaleToTotalPixels, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, Fast Groups Bypasser (rgthree), PreviewImage, SaveImage, ImpactInt, ImpactInt, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5.1图像双采超分辨率高清放大｜极致超清｜细节拉满｜高清放大_2112171175697801218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5.1图像双采超分辨率高清放大｜极致超清｜细节拉满｜高清放大_2112171175697801218.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（14 个）：
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `SaveImage`
- `ImpactInt`
- `ImpactInt`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SaveImage`、`ImpactInt`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、ImpactInt、sd15-t2i-basic
