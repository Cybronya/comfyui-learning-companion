---
key: 平台全量/（动态版）豆包官方版seedance2.0水印去除+高清化V3（9_16竖版）_2024885131164520449.json
name: （动态版）豆包官方版seedance2.0水印去除+高清化V3（9_16竖版）_2024885131164520449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（动态版）豆包官方版seedance2.0水印去除+高清化V3（9_16竖版）_2024885131164520449.json
hash: 87252cf251748096
coverage: 0.870968
learned_at: 2026-11-14 02:53:53
nodes: [easy showAnything, MaskToImage, PreviewImage, ImageResizeKJv2, JWInteger, Note, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, DiffuEraserSampler, CreateVideo, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, VHS_VideoCombine, MathExpression|pysssss, RepeatImageBatch, easy showAnything, MathExpression|pysssss, VHS_VideoInfo, VHS_VideoCombine, FlashVSR_SM_KSampler, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, ImageFromBatch+, LoadImage, ImageConcanate]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1540561519}
---

# 平台全量/（动态版）豆包官方版seedance2.0水印去除+高清化V3（9_16竖版）_2024885131164520449.json

> 来源文件 `comfyui_library/workflows/平台全量/（动态版）豆包官方版seedance2.0水印去除+高清化V3（9_16竖版）_2024885131164520449.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（31 个）：
- `easy showAnything`
- `MaskToImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `JWInteger`
- `Note`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetVideoComponents`
- `DiffuEraserSampler` ★核心
- `CreateVideo`
- `LayerUtility: PurgeVRAM V2`
- `DiffuEraserLoader`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `FlashVSR_SM_KSampler` ★核心
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `ImageFromBatch+`
- `LoadImage`
- `ImageConcanate`

## 关键参数

- `seed` = `1280`
- `steps` = `1540561519`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`MaskToImage`、`ImageResizeKJv2`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`DiffuEraserSampler`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`VHS_VideoCombine`、`MathExpression|pysssss`、`RepeatImageBatch`、`VHS_VideoInfo`、`FlashVSR_SM_KSampler`、`VHS_LoadVideo`、`SaveImage`、`LoadImage`、`ImageConcanate`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、CreateVideo、DiffuEraserLoader
