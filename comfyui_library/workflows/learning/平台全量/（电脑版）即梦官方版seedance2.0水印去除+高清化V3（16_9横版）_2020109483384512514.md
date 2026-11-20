---
key: 平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（16_9横版）_2020109483384512514.json
name: （电脑版）即梦官方版seedance2.0水印去除+高清化V3（16_9横版）_2020109483384512514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（16_9横版）_2020109483384512514.json
hash: 99b363d18f6a04fa
coverage: 0.888889
learned_at: 2026-11-14 02:54:08
nodes: [RepeatImageBatch, ImageConcanate, PreviewImage, Note, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, LayerUtility: PurgeVRAM V2, CreateVideo, VHS_VideoCombine, ImageFromBatch+, JWInteger, VHS_VideoCombine, LoadImage, VHS_VideoCombine, ImageResizeKJv2, MaskToImage, DiffuEraserLoader, SaveImage, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, DiffuEraserSampler, VHS_VideoInfo, MathExpression|pysssss, easy showAnything, easy showAnything, MathExpression|pysssss, VHS_VideoCombine, FlashVSR_SM_KSampler, SaveVideo, CreateVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1144723809}
---

# 平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（16_9横版）_2020109483384512514.json

> 来源文件 `comfyui_library/workflows/平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（16_9横版）_2020109483384512514.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `RepeatImageBatch`
- `ImageConcanate`
- `PreviewImage`
- `Note`
- `ImageConcanate`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetVideoComponents`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `MaskToImage`
- `DiffuEraserLoader`
- `SaveImage`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DiffuEraserSampler` ★核心
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `FlashVSR_SM_KSampler` ★核心
- `SaveVideo`
- `CreateVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1144723809`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`RepeatImageBatch`、`ImageConcanate`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`CreateVideo`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`MaskToImage`、`DiffuEraserLoader`、`SaveImage`、`VHS_LoadVideo`、`DiffuEraserSampler`、`VHS_VideoInfo`、`MathExpression|pysssss`、`FlashVSR_SM_KSampler`、`SaveVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
