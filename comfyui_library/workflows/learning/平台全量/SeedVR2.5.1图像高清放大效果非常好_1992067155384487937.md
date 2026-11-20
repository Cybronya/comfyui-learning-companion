---
key: 平台全量/SeedVR2.5.1图像高清放大效果非常好_1992067155384487937.json
name: SeedVR2.5.1图像高清放大效果非常好_1992067155384487937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5.1图像高清放大效果非常好_1992067155384487937.json
hash: 90a2bb2a1a933c29
coverage: 0.714286
learned_at: 2026-11-14 00:59:32
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Image Comparer (rgthree), PrimitiveInt, SeedVR2VideoUpscaler, SaveImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5.1图像高清放大效果非常好_1992067155384487937.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5.1图像高清放大效果非常好_1992067155384487937.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `PrimitiveInt`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **71%**（5/7）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler
