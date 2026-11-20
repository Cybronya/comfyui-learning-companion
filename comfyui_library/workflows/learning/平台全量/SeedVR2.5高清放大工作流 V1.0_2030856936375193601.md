---
key: 平台全量/SeedVR2.5高清放大工作流 V1.0_2030856936375193601.json
name: SeedVR2.5高清放大工作流 V1.0_2030856936375193601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5高清放大工作流 V1.0_2030856936375193601.json
hash: 7a559200a597334a
coverage: 0.714286
learned_at: 2026-11-14 00:59:40
nodes: [SeedVR2LoadVAEModel, Image Comparer (rgthree), SaveImage, easy clearCacheAll, easy cleanGpuUsed, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, MarkdownNote, LoadImage, MarkdownNote, PreviewImage, ImageScaleToTotalPixels, JoinImageWithAlpha, easy int]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5高清放大工作流 V1.0_2030856936375193601.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5高清放大工作流 V1.0_2030856936375193601.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（14 个）：
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `SaveImage`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `JoinImageWithAlpha`
- `easy int`

## 知识

覆盖率 **71%**（10/14）

**有卡**：`SeedVR2LoadVAEModel`、`SaveImage`、`easy clearCacheAll`、`easy cleanGpuUsed`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`LoadImage`、`ImageScaleToTotalPixels`、`JoinImageWithAlpha`、`easy int`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、easy cleanGpuUsed、easy clearCacheAll、easy int
