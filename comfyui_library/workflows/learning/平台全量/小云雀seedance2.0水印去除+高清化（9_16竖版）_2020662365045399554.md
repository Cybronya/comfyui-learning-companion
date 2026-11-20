---
key: 平台全量/小云雀seedance2.0水印去除+高清化（9_16竖版）_2020662365045399554.json
name: 小云雀seedance2.0水印去除+高清化（9_16竖版）_2020662365045399554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除+高清化（9_16竖版）_2020662365045399554.json
hash: e8b54775dd712687
coverage: 0.885714
learned_at: 2026-11-14 02:01:11
nodes: [ImageFromBatch+, ImageResizeKJv2, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, easy showAnything, RepeatImageBatch, DiffuEraserSampler, LayerUtility: PurgeVRAM V2, ImageConcanate, DiffuEraserLoader, VHS_VideoCombine, VHS_VideoCombine, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, FlashVSR_SM_Model, FlashVSR_SM_KSampler, GetVideoComponents, CreateVideo, ImageConcanate, JWInteger, VHS_LoadVideo, CreateVideo, VHS_VideoCombine, SaveImage, LoadImage, Note, MaskToImage, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1023328264}
---

# 平台全量/小云雀seedance2.0水印去除+高清化（9_16竖版）_2020662365045399554.json

> 来源文件 `comfyui_library/workflows/平台全量/小云雀seedance2.0水印去除+高清化（9_16竖版）_2020662365045399554.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `JWInteger`
- `VHS_LoadVideo`
- `CreateVideo`
- `VHS_VideoCombine`
- `SaveImage`
- `LoadImage`
- `Note`
- `MaskToImage`
- `SaveVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1023328264`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`ImageFromBatch+`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfo`、`MathExpression|pysssss`、`RepeatImageBatch`、`DiffuEraserSampler`、`LayerUtility: PurgeVRAM V2`、`ImageConcanate`、`DiffuEraserLoader`、`VHS_VideoCombine`、`GetVideoComponents`、`JWInteger`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`CreateVideo`、`VHS_LoadVideo`、`SaveImage`、`LoadImage`、`MaskToImage`、`SaveVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
