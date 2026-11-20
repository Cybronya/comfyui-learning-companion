---
key: 平台全量/Seedance2.0去字幕+高清放大（可手动调整蒙版）_2045831897707716610.json
name: Seedance2.0去字幕+高清放大（可手动调整蒙版）_2045831897707716610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedance2.0去字幕+高清放大（可手动调整蒙版）_2045831897707716610.json
hash: 1773f04e74a3b568
coverage: 0.815789
learned_at: 2026-11-14 01:00:27
nodes: [MaskToImage, PreviewImage, ImageResizeKJv2, JWInteger, SaveImage, Note, ImageConcanate, JWInteger, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, DiffuEraserSampler, DiffuEraserLoader, MathExpression|pysssss, RepeatImageBatch, easy showAnything, MathExpression|pysssss, FlashVSR_SM_KSampler, LayerUtility: PurgeVRAM V2, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfo, easy showAnything, ImageFromBatch+, VHS_LoadVideo, GetVideoComponents, GetVideoComponents, RunningHub Deepcleaner, LayerUtility: PurgeVRAM V2, CreateVideo, RunningHub Deepcleaner, VHS_VideoCombine, RunningHub Deepcleaner, Reroute, Reroute, Reroute, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 997371043}
---

# 平台全量/Seedance2.0去字幕+高清放大（可手动调整蒙版）_2045831897707716610.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedance2.0去字幕+高清放大（可手动调整蒙版）_2045831897707716610.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
- `MaskToImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `JWInteger`
- `SaveImage`
- `Note`
- `ImageConcanate`
- `JWInteger`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `DiffuEraserSampler` ★核心
- `DiffuEraserLoader`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `FlashVSR_SM_KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfo`
- `easy showAnything`
- `ImageFromBatch+`
- `VHS_LoadVideo`
- `GetVideoComponents`
- `GetVideoComponents`
- `RunningHub Deepcleaner`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `RunningHub Deepcleaner`
- `VHS_VideoCombine`
- `RunningHub Deepcleaner`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `997371043`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **82%**（31/38）

**有卡**：`MaskToImage`、`ImageResizeKJv2`、`JWInteger`、`SaveImage`、`ImageConcanate`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`DiffuEraserSampler`、`DiffuEraserLoader`、`MathExpression|pysssss`、`RepeatImageBatch`、`FlashVSR_SM_KSampler`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoInfo`、`VHS_LoadVideo`、`GetVideoComponents`、`RunningHub Deepcleaner`、`CreateVideo`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、CreateVideo、DiffuEraserLoader
