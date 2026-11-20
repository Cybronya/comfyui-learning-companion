---
key: 平台全量/SeedVR2-2.5.1图像高清放大_2019450498465665025.json
name: SeedVR2-2.5.1图像高清放大_2019450498465665025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2-2.5.1图像高清放大_2019450498465665025.json
hash: f7c824870a13368c
coverage: 0.857143
learned_at: 2026-11-14 00:59:07
nodes: [SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, Image Comparer (rgthree), LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, SaveImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/SeedVR2-2.5.1图像高清放大_2019450498465665025.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2-2.5.1图像高清放大_2019450498465665025.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（7 个）：
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM V2`、`SeedVR2VideoUpscaler`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、LayerUtility: PurgeVRAM V2、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2
