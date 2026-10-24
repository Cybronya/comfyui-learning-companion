---
key: 图片生成/图生图/无损超清双倍增强器eedVR2.5_1995105861876035586.json
name: 无损超清双倍增强器eedVR2.5_1995105861876035586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/无损超清双倍增强器eedVR2.5_1995105861876035586.json
hash: 234f26b6142de764
coverage: 0.857143
learned_at: 2026-10-23 13:04:19
nodes: [LayerUtility: PurgeVRAM V2, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM V2, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, easy int, SeedVR2LoadDiTModel, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/无损超清双倍增强器eedVR2.5_1995105861876035586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/无损超清双倍增强器eedVR2.5_1995105861876035586.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（14 个）：
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `easy int`
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`easy int`、`LoadImage`、`SaveImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、easy int、LayerUtility: PurgeVRAM V2、sd15-t2i-basic
