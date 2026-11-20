---
key: 平台全量/SeedVR2.5.1图像高清放大_1991838615928107010.json
name: SeedVR2.5.1图像高清放大_1991838615928107010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5.1图像高清放大_1991838615928107010.json
hash: d6245980aee5d0f3
coverage: 0.714286
learned_at: 2026-11-14 00:59:31
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, LoadImage, Image Comparer (rgthree), PrimitiveInt]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5.1图像高清放大_1991838615928107010.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5.1图像高清放大_1991838615928107010.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PrimitiveInt`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler
