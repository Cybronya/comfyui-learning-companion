---
key: 图片生成/图生图/SeedVR 2.5 图像放大（合适模糊图片）_2092504146418159617.json
name: SeedVR 2.5 图像放大（合适模糊图片）_2092504146418159617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR 2.5 图像放大（合适模糊图片）_2092504146418159617.json
hash: 25cc82c70d78a15e
coverage: 0.875
learned_at: 2026-10-21 00:44:21
nodes: [Note, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, ImageScaleToTotalPixels, LoadImage, INTConstant]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR 2.5 图像放大（合适模糊图片）_2092504146418159617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR 2.5 图像放大（合适模糊图片）_2092504146418159617.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `Note`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `INTConstant`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`ImageScaleToTotalPixels`、`LoadImage`、`INTConstant`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、INTConstant、sd15-t2i-basic
