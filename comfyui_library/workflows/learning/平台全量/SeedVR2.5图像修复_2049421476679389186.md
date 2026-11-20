---
key: 平台全量/SeedVR2.5图像修复_2049421476679389186.json
name: SeedVR2.5图像修复_2049421476679389186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5图像修复_2049421476679389186.json
hash: 4eaaf6feffbaa757
coverage: 0.7
learned_at: 2026-11-14 00:59:35
nodes: [SeedVR2LoadVAEModel, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, Note, SeedVR2LoadDiTModel, LoadImage, Note, Note, INTConstant, SaveImage]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5图像修复_2049421476679389186.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5图像修复_2049421476679389186.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `Note`
- `SeedVR2LoadDiTModel`
- `LoadImage`
- `Note`
- `Note`
- `INTConstant`
- `SaveImage`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`LoadImage`、`INTConstant`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、ImageScaleToTotalPixels、INTConstant、image_to_image_controlnet_face_detailer_lora
