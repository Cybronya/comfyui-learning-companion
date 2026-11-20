---
key: 平台全量/SeedVR2(2.5)图像高清放大_2002019927261364225.json
name: SeedVR2(2.5)图像高清放大_2002019927261364225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2(2.5)图像高清放大_2002019927261364225.json
hash: dd2549ee1e8c38a3
coverage: 0.833333
learned_at: 2026-11-14 00:59:01
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, LoadImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, SaveImage]
patterns: []
missing: []
---

# 平台全量/SeedVR2(2.5)图像高清放大_2002019927261364225.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2(2.5)图像高清放大_2002019927261364225.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SaveImage`

## 知识

覆盖率 **83%**（5/6）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`、`SeedVR2VideoUpscaler`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2、image_to_image_controlnet_face_detailer_sampler
