---
key: 平台全量/图片高清修复SeedVR2.5_2013935198743830529.json
name: 图片高清修复SeedVR2.5_2013935198743830529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图片高清修复SeedVR2.5_2013935198743830529.json
hash: e64dece19d92a18c
coverage: 0.7
learned_at: 2026-11-14 01:55:52
nodes: [ImageScaleBy, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, Int, PreviewImage, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), LoadImage]
patterns: []
missing: []
---

# 平台全量/图片高清修复SeedVR2.5_2013935198743830529.json

> 来源文件 `comfyui_library/workflows/平台全量/图片高清修复SeedVR2.5_2013935198743830529.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `ImageScaleBy`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `Int`
- `PreviewImage`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`ImageScaleBy`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`Int`、`SeedVR2VideoUpscaler`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleBy、Int、image_to_image_controlnet_face_detailer_lora
