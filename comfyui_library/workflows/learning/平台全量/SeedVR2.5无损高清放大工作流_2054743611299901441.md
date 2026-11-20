---
key: 平台全量/SeedVR2.5无损高清放大工作流_2054743611299901441.json
name: SeedVR2.5无损高清放大工作流_2054743611299901441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5无损高清放大工作流_2054743611299901441.json
hash: 221b77bbf1b3d183
coverage: 0.777778
learned_at: 2026-11-14 00:59:35
nodes: [Image Comparer (rgthree), LoadImage, SaveImage, ResizeImagesByLongerEdge, SeedVR2LoadDiTModel, MarkdownNote, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, easy int]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5无损高清放大工作流_2054743611299901441.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5无损高清放大工作流_2054743611299901441.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `ResizeImagesByLongerEdge`
- `SeedVR2LoadDiTModel`
- `MarkdownNote`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `easy int`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`LoadImage`、`SaveImage`、`ResizeImagesByLongerEdge`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`easy int`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、ResizeImagesByLongerEdge、SaveImage、easy int、image_to_image_controlnet_face_detailer_lora
