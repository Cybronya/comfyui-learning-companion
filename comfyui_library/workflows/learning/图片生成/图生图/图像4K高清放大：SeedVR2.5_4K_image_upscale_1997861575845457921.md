---
key: 图片生成/图生图/图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921.json
name: 图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921.json
hash: 42f411edaccc9629
coverage: 0.714286
learned_at: 2026-10-23 12:37:59
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, easy int, JoinImageWithAlpha, easy int, Note, Note, Image Comparer (rgthree), PreviewImage, ImageScaleRestore_UTK, SaveImage, SeedVR2VideoUpscaler, LoadImage, Label (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像4K高清放大：SeedVR2.5_4K_image_upscale_1997861575845457921.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（14 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `easy int`
- `JoinImageWithAlpha`
- `easy int`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ImageScaleRestore_UTK`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `Label (rgthree)`

## 知识

覆盖率 **71%**（10/14）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`easy int`、`JoinImageWithAlpha`、`ImageScaleRestore_UTK`、`SaveImage`、`SeedVR2VideoUpscaler`、`LoadImage`、`Label (rgthree)`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、JoinImageWithAlpha、easy int、Label (rgthree)
