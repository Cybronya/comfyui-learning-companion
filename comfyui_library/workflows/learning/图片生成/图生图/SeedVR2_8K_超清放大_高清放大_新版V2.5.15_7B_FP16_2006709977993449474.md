---
key: 图片生成/图生图/SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474.json
name: SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474.json
hash: 7e0212cafdd83427
coverage: 0.8
learned_at: 2026-10-23 11:25:13
nodes: [easy int, SimpleMath+, Image Comparer (rgthree), easy cleanGpuUsed, easy int, PreviewImage, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, LoadImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM, Note, SeedVR2LoadVAEModel, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2_8K_超清放大_高清放大_新版V2.5.15_7B_FP16_2006709977993449474.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（15 个）：
- `easy int`
- `SimpleMath+`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `easy int`
- `PreviewImage`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM`
- `Note`
- `SeedVR2LoadVAEModel`
- `SaveImage`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`easy int`、`SimpleMath+`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LayerUtility: PurgeVRAM`、`SeedVR2LoadVAEModel`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、easy cleanGpuUsed、easy int、LayerUtility: PurgeVRAM
