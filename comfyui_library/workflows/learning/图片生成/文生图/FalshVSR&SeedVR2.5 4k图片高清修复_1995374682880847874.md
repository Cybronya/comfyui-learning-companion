---
key: 图片生成/文生图/FalshVSR&SeedVR2.5 4k图片高清修复_1995374682880847874.json
name: FalshVSR&SeedVR2.5 4k图片高清修复_1995374682880847874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FalshVSR&SeedVR2.5 4k图片高清修复_1995374682880847874.json
hash: 2d2efa64beae65c3
coverage: 0.875
learned_at: 2026-10-19 21:32:30
nodes: [SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: PurgeVRAM, Image Comparer (rgthree), JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, Image Comparer (rgthree), GetImageRangeFromBatch, SaveImage, SaveImage, SeedVR2VideoUpscaler, FlashVSR_SM_Model, FlashVSR_SM_KSampler, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 847202090}
---

# 图片生成/文生图/FalshVSR&SeedVR2.5 4k图片高清修复_1995374682880847874.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FalshVSR&SeedVR2.5 4k图片高清修复_1995374682880847874.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（16 个）：
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerUtility: PurgeVRAM`
- `Image Comparer (rgthree)`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `Image Comparer (rgthree)`
- `GetImageRangeFromBatch`
- `SaveImage`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `847202090`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LayerUtility: PurgeVRAM`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`SaveImage`、`SeedVR2VideoUpscaler`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、FlashVSR_SM_KSampler、SaveImage、GetImageRangeFromBatch、FlashVSR_SM_Model
