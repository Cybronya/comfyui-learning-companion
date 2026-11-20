---
key: 平台全量/（随变）seedance2.0水印去除+高清化V3（9_16竖版）_2021669365162188801.json
name: （随变）seedance2.0水印去除+高清化V3（9_16竖版）_2021669365162188801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（随变）seedance2.0水印去除+高清化V3（9_16竖版）_2021669365162188801.json
hash: 844cdaf900385c9a
coverage: 0.885714
learned_at: 2026-11-14 02:54:16
nodes: [easy showAnything, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, RepeatImageBatch, JWInteger, SaveImage, CreateVideo, FlashVSR_SM_KSampler, SaveVideo, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, GetVideoComponents, VHS_VideoCombine, DiffuEraserSampler, CreateVideo, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, ImageFromBatch+, VHS_VideoCombine, PreviewImage, MaskToImage, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, Note, ImageResizeKJv2, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 337977388}
---

# 平台全量/（随变）seedance2.0水印去除+高清化V3（9_16竖版）_2021669365162188801.json

> 来源文件 `comfyui_library/workflows/平台全量/（随变）seedance2.0水印去除+高清化V3（9_16竖版）_2021669365162188801.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatImageBatch`
- `JWInteger`
- `SaveImage`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `SaveVideo`
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
- `Note`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `337977388`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatImageBatch`、`JWInteger`、`SaveImage`、`CreateVideo`、`FlashVSR_SM_KSampler`、`SaveVideo`、`ImageConcanate`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`VHS_VideoCombine`、`DiffuEraserSampler`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`MaskToImage`、`VHS_VideoInfo`、`MathExpression|pysssss`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
