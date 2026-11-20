---
key: 平台全量/小云雀seedance2.0水印去除+高清化（16 _ 9 横板）_2020691299023720449.json
name: 小云雀seedance2.0水印去除+高清化（16 _ 9 横板）_2020691299023720449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除+高清化（16 _ 9 横板）_2020691299023720449.json
hash: a3dd9389aaf3094b
coverage: 0.885714
learned_at: 2026-11-14 02:01:11
nodes: [ImageFromBatch+, ImageResizeKJv2, PreviewImage, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, easy showAnything, RepeatImageBatch, DiffuEraserSampler, LayerUtility: PurgeVRAM V2, ImageConcanate, DiffuEraserLoader, VHS_VideoCombine, VHS_VideoCombine, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, FlashVSR_SM_Model, FlashVSR_SM_KSampler, GetVideoComponents, CreateVideo, ImageConcanate, CreateVideo, Note, MaskToImage, VHS_LoadVideo, VHS_VideoCombine, SaveVideo, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, LoadImage, JWInteger]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 401710656}
---

# 平台全量/小云雀seedance2.0水印去除+高清化（16 _ 9 横板）_2020691299023720449.json

> 来源文件 `comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除+高清化（16 _ 9 横板）_2020691299023720449.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `RepeatImageBatch`
- `DiffuEraserSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageConcanate`
- `DiffuEraserLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `GetVideoComponents`
- `CreateVideo`
- `ImageConcanate`
- `CreateVideo`
- `Note`
- `MaskToImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `SaveVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `LoadImage`
- `JWInteger`

## 关键参数

- `seed` = `1280`
- `steps` = `401710656`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`ImageFromBatch+`、`ImageResizeKJv2`、`VHS_VideoInfo`、`MathExpression|pysssss`、`RepeatImageBatch`、`DiffuEraserSampler`、`LayerUtility: PurgeVRAM V2`、`ImageConcanate`、`DiffuEraserLoader`、`VHS_VideoCombine`、`GetVideoComponents`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`CreateVideo`、`MaskToImage`、`VHS_LoadVideo`、`SaveVideo`、`SaveImage`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
