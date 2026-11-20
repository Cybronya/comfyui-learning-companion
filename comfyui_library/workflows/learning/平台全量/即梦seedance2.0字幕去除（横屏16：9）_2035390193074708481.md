---
key: 平台全量/即梦seedance2.0字幕去除（横屏16：9）_2035390193074708481.json
name: 即梦seedance2.0字幕去除（横屏16：9）_2035390193074708481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/即梦seedance2.0字幕去除（横屏16：9）_2035390193074708481.json
hash: 88fd2e0b07615853
coverage: 0.724138
learned_at: 2026-11-14 01:49:08
nodes: [VHS_LoadVideo, SaveImage, ImageFromBatch+, Note, easy showAnything, DiffuEraserSampler, RepeatImageBatch, VHS_VideoInfo, MathExpression_UTK, easy showAnything, easy showAnything, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, PreviewImage, GetVideoComponents, DiffuEraserLoader, CreateVideo, FlashVSRNode, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_KSampler, VHS_VideoCombine, PrimitiveFloat, LoadImage, Note, JWInteger, Note]
patterns: []
missing: []
parameters: {"cfg": "fixed", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 723423500}
---

# 平台全量/即梦seedance2.0字幕去除（横屏16：9）_2035390193074708481.json

> 来源文件 `comfyui_library/workflows/平台全量/即梦seedance2.0字幕去除（横屏16：9）_2035390193074708481.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `VHS_LoadVideo`
- `SaveImage`
- `ImageFromBatch+`
- `Note`
- `easy showAnything`
- `DiffuEraserSampler` ★核心
- `RepeatImageBatch`
- `VHS_VideoInfo`
- `MathExpression_UTK`
- `easy showAnything`
- `easy showAnything`
- `MaskToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `PreviewImage`
- `GetVideoComponents`
- `DiffuEraserLoader`
- `CreateVideo`
- `FlashVSRNode`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_KSampler` ★核心
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `LoadImage`
- `Note`
- `JWInteger`
- `Note`

## 关键参数

- `seed` = `1280`
- `steps` = `723423500`
- `cfg` = `fixed`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **72%**（21/29）

**有卡**：`VHS_LoadVideo`、`SaveImage`、`ImageFromBatch+`、`DiffuEraserSampler`、`RepeatImageBatch`、`VHS_VideoInfo`、`MathExpression_UTK`、`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`GetVideoComponents`、`DiffuEraserLoader`、`CreateVideo`、`FlashVSRNode`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`VHS_VideoCombine`、`LoadImage`、`JWInteger`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、CreateVideo、DiffuEraserLoader
