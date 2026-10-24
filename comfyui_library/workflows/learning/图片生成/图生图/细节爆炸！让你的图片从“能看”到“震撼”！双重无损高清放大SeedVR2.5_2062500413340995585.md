---
key: 图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！双重无损高清放大SeedVR2.5_2062500413340995585.json
name: 细节爆炸！让你的图片从“能看”到“震撼”！双重无损高清放大SeedVR2.5_2062500413340995585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！双重无损高清放大SeedVR2.5_2062500413340995585.json
hash: 91d9dc9f02c21c0e
coverage: 0.8
learned_at: 2026-10-23 13:21:42
nodes: [LayerUtility: PurgeVRAM V2, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM V2, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, Image Comparer (rgthree), easy int, Note, SaveImage, Image Comparer (rgthree), SeedVR2LoadDiTModel, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！双重无损高清放大SeedVR2.5_2062500413340995585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/细节爆炸！让你的图片从“能看”到“震撼”！双重无损高清放大SeedVR2.5_2062500413340995585.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（15 个）：
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `easy int`
- `Note`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `LoadImage`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`easy int`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、easy int、LayerUtility: PurgeVRAM V2、sd15-t2i-basic
