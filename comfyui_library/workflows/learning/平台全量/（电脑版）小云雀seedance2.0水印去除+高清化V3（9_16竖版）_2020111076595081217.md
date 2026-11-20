---
key: 平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（9_16竖版）_2020111076595081217.json
name: （电脑版）小云雀seedance2.0水印去除+高清化V3（9_16竖版）_2020111076595081217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（9_16竖版）_2020111076595081217.json
hash: b0a31c9dfdad1054
coverage: 0.888889
learned_at: 2026-11-14 02:54:10
nodes: [easy showAnything, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, RepeatImageBatch, JWInteger, SaveImage, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, GetVideoComponents, VHS_VideoCombine, DiffuEraserSampler, CreateVideo, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, ImageFromBatch+, VHS_VideoCombine, PreviewImage, MaskToImage, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, VHS_LoadVideo, LoadImage, Note, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, SaveVideo, FlashVSR_SM_KSampler, CreateVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 2145065276}
---

# 平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（9_16竖版）_2020111076595081217.json

> 来源文件 `comfyui_library/workflows/平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（9_16竖版）_2020111076595081217.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatImageBatch`
- `JWInteger`
- `SaveImage`
- `ImageConcanate`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageConcanate`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `CreateVideo`
- `LayerUtility: PurgeVRAM V2`
- `DiffuEraserLoader`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `PreviewImage`
- `MaskToImage`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `LoadImage`
- `Note`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SaveVideo`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `2145065276`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatImageBatch`、`JWInteger`、`SaveImage`、`ImageConcanate`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`VHS_VideoCombine`、`DiffuEraserSampler`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`MaskToImage`、`VHS_VideoInfo`、`MathExpression|pysssss`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJv2`、`SaveVideo`、`FlashVSR_SM_KSampler`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
