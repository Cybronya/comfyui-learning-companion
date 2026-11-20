---
key: 平台全量/（随变）去水印-seedance2.0视频局部消除+高清修复250213（9_16竖版）_2022333696119934978.json
name: （随变）去水印-seedance2.0视频局部消除+高清修复250213（9_16竖版）_2022333696119934978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（随变）去水印-seedance2.0视频局部消除+高清修复250213（9_16竖版）_2022333696119934978.json
hash: 22f9983057c3aed3
coverage: 0.794118
learned_at: 2026-11-14 02:54:17
nodes: [VHS_LoadVideo, Note, MaskToImage, MathExpression|pysssss, easy showAnything, RepeatImageBatch, CreateVideo, JWInteger, LayerUtility: PurgeVRAM V2, VHS_VideoInfo, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, PreviewImage, MathExpression|pysssss, easy showAnything, DiffuEraserLoader, ImageFromBatch+, GetVideoComponents, LayerUtility: ImageScaleByAspectRatio V2, DiffuEraserSampler, easy cleanGpuUsed, GetVideoComponents, FlashVSR_SM_Model, easy cleanGpuUsed, Reroute, Reroute, Reroute, LoadImage, SaveVideo, CreateVideo, VHS_VideoCombine, easy cleanGpuUsed, FlashVSR_SM_KSampler, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1439949734}
---

# 平台全量/（随变）去水印-seedance2.0视频局部消除+高清修复250213（9_16竖版）_2022333696119934978.json

> 来源文件 `comfyui_library/workflows/平台全量/（随变）去水印-seedance2.0视频局部消除+高清修复250213（9_16竖版）_2022333696119934978.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（34 个）：
- `VHS_LoadVideo`
- `Note`
- `MaskToImage`
- `MathExpression|pysssss`
- `easy showAnything`
- `RepeatImageBatch`
- `CreateVideo`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoInfo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `PreviewImage`
- `MathExpression|pysssss`
- `easy showAnything`
- `DiffuEraserLoader`
- `ImageFromBatch+`
- `GetVideoComponents`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DiffuEraserSampler` ★核心
- `easy cleanGpuUsed`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoadImage`
- `SaveVideo`
- `CreateVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `FlashVSR_SM_KSampler` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `1439949734`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`VHS_LoadVideo`、`MaskToImage`、`MathExpression|pysssss`、`RepeatImageBatch`、`CreateVideo`、`JWInteger`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoInfo`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`DiffuEraserLoader`、`ImageFromBatch+`、`GetVideoComponents`、`DiffuEraserSampler`、`easy cleanGpuUsed`、`FlashVSR_SM_Model`、`LoadImage`、`SaveVideo`、`VHS_VideoCombine`、`FlashVSR_SM_KSampler`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、DiffuEraserLoader
