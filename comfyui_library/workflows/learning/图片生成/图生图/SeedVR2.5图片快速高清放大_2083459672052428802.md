---
key: 图片生成/图生图/SeedVR2.5图片快速高清放大_2083459672052428802.json
name: SeedVR2.5图片快速高清放大_2083459672052428802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5图片快速高清放大_2083459672052428802.json
hash: 8675f4cdad779466
coverage: 0.75
learned_at: 2026-10-23 11:25:07
nodes: [SeedVR2LoadVAEModel, Image Comparer (rgthree), SaveImage, Note, LoadImage, SeedVR2LoadDiTModel, easy clearCacheAll, easy cleanGpuUsed, SeedVR2VideoUpscaler, ResizeImagesByLongerEdge, easy int, MarkdownNote]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5图片快速高清放大_2083459672052428802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5图片快速高清放大_2083459672052428802.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（12 个）：
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Note`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `ResizeImagesByLongerEdge`
- `easy int`
- `MarkdownNote`

## 知识

覆盖率 **75%**（9/12）

**有卡**：`SeedVR2LoadVAEModel`、`SaveImage`、`LoadImage`、`SeedVR2LoadDiTModel`、`easy clearCacheAll`、`easy cleanGpuUsed`、`SeedVR2VideoUpscaler`、`ResizeImagesByLongerEdge`、`easy int`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、ResizeImagesByLongerEdge、SaveImage、easy cleanGpuUsed、easy clearCacheAll
