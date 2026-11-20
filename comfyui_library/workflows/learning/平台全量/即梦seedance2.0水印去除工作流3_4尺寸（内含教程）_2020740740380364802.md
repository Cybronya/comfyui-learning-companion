---
key: 平台全量/即梦seedance2.0水印去除工作流3_4尺寸（内含教程）_2020740740380364802.json
name: 即梦seedance2.0水印去除工作流3_4尺寸（内含教程）_2020740740380364802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/即梦seedance2.0水印去除工作流3_4尺寸（内含教程）_2020740740380364802.json
hash: 3d369c462939bb15
coverage: 1
learned_at: 2026-11-14 01:49:10
nodes: [CreateVideo, ImageResizeKJv2, MaskToImage, FlashVSR_SM_KSampler, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, VHS_VideoInfo, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss, RepeatImageBatch, DiffuEraserSampler, DiffuEraserLoader, LoadImage, VHS_LoadVideo, VHS_VideoCombine, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 201907779}
---

# 平台全量/即梦seedance2.0水印去除工作流3_4尺寸（内含教程）_2020740740380364802.json

> 来源文件 `comfyui_library/workflows/平台全量/即梦seedance2.0水印去除工作流3_4尺寸（内含教程）_2020740740380364802.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（22 个）：
- `CreateVideo`
- `ImageResizeKJv2`
- `MaskToImage`
- `FlashVSR_SM_KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `GetVideoComponents`
- `CreateVideo`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoInfo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `DiffuEraserSampler` ★核心
- `DiffuEraserLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `SaveVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `201907779`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`CreateVideo`、`ImageResizeKJv2`、`MaskToImage`、`FlashVSR_SM_KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_Model`、`GetVideoComponents`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoInfo`、`MathExpression|pysssss`、`RepeatImageBatch`、`DiffuEraserSampler`、`DiffuEraserLoader`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`、`SaveVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、DiffuEraserLoader
