---
key: 平台全量/🦖小云雀seedance2.0去水印高清化_2026863874552631298.json
name: 🦖小云雀seedance2.0去水印高清化_2026863874552631298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🦖小云雀seedance2.0去水印高清化_2026863874552631298.json
hash: da50e21ce4f16940
coverage: 0.888889
learned_at: 2026-11-14 02:55:51
nodes: [DiffuEraserLoader, easy showAnything, ImageResizeKJv2, RepeatImageBatch, MaskToImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, LayerUtility: PurgeVRAM V2, CreateVideo, DiffuEraserSampler, ImageFromBatch+, easy showAnything, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, Note, LoadImage, TwoWaySwitch, TwoWaySwitch, JWInteger, ImageConcanate, FlashVSR_SM_KSampler, VHS_LoadVideo, Int, LoadImage, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1709528875}
---

# 平台全量/🦖小云雀seedance2.0去水印高清化_2026863874552631298.json

> 来源文件 `comfyui_library/workflows/平台全量/🦖小云雀seedance2.0去水印高清化_2026863874552631298.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `DiffuEraserLoader`
- `easy showAnything`
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `MaskToImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetVideoComponents`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `DiffuEraserSampler` ★核心
- `ImageFromBatch+`
- `easy showAnything`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `Note`
- `LoadImage`
- `TwoWaySwitch`
- `TwoWaySwitch`
- `JWInteger`
- `ImageConcanate`
- `FlashVSR_SM_KSampler` ★核心
- `VHS_LoadVideo`
- `Int`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `1709528875`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`DiffuEraserLoader`、`ImageResizeKJv2`、`RepeatImageBatch`、`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: PurgeVRAM V2`、`CreateVideo`、`DiffuEraserSampler`、`VHS_VideoInfo`、`MathExpression|pysssss`、`VHS_VideoCombine`、`LoadImage`、`TwoWaySwitch`、`ImageConcanate`、`FlashVSR_SM_KSampler`、`VHS_LoadVideo`、`Int`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、CreateVideo、DiffuEraserLoader
