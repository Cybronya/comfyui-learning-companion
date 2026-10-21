---
key: 图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json
name: SeedVR2.5双重无损高清放大_2064919630879223810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json
hash: 902f8e8e6d068975
coverage: 0.857143
learned_at: 2026-10-21 00:44:24
nodes: [LayerUtility: PurgeVRAM V2, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, LayerUtility: PurgeVRAM V2, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM V2, SeedVR2VideoUpscaler, Image Comparer (rgthree), easy int, SaveImage, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadDiTModel, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2.5双重无损高清放大_2064919630879223810.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（14 个）：
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `easy int`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadDiTModel`
- `LoadImage`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`easy int`、`SaveImage`、`SeedVR2LoadDiTModel`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、SaveImage、easy int、LayerUtility: PurgeVRAM V2、sd15-t2i-basic
