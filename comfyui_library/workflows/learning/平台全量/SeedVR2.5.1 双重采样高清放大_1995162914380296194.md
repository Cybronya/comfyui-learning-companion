---
key: 平台全量/SeedVR2.5.1 双重采样高清放大_1995162914380296194.json
name: SeedVR2.5.1 双重采样高清放大_1995162914380296194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5.1 双重采样高清放大_1995162914380296194.json
hash: 7a5e824a698b9a47
coverage: 0.631579
learned_at: 2026-11-14 00:59:27
nodes: [PreviewImage, ImageScaleToTotalPixels, ImpactInt, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), Note, SaveImage, Note, SaveImage, Image Comparer (rgthree), ImpactInt, SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5.1 双重采样高清放大_1995162914380296194.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5.1 双重采样高清放大_1995162914380296194.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `ImpactInt`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `SaveImage`
- `Note`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **63%**（12/19）

**有卡**：`ImageScaleToTotalPixels`、`ImpactInt`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2LoadDiTModel`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、ImpactInt、image_to_image_controlnet_face_detailer_lora
