---
key: 数字人/数字人/即梦官方版seedance2.0水印去除+高清化V2（16_9横版）_2020194791643947010.json
name: 即梦官方版seedance2.0水印去除+高清化V2（16_9横版）_2020194791643947010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/即梦官方版seedance2.0水印去除+高清化V2（16_9横版）_2020194791643947010.json
hash: 5b4689c74b8f4f25
coverage: 0.885714
learned_at: 2026-10-26 02:00:52
nodes: [RepeatImageBatch, ImageConcanate, PreviewImage, Note, CreateVideo, FlashVSR_SM_KSampler, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, LayerUtility: PurgeVRAM V2, CreateVideo, VHS_VideoCombine, SaveVideo, ImageFromBatch+, JWInteger, VHS_VideoCombine, LoadImage, VHS_VideoCombine, ImageResizeKJv2, MaskToImage, DiffuEraserLoader, SaveImage, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, DiffuEraserSampler, VHS_VideoInfo, MathExpression|pysssss, easy showAnything, easy showAnything, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1792618508}
---

# 数字人/数字人/即梦官方版seedance2.0水印去除+高清化V2（16_9横版）_2020194791643947010.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/即梦官方版seedance2.0水印去除+高清化V2（16_9横版）_2020194791643947010.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `RepeatImageBatch`
- `ImageConcanate`
- `PreviewImage`
- `Note`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
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
- `SaveVideo`
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

## 关键参数

- `seed` = `1280`
- `steps` = `1792618508`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`RepeatImageBatch`、`ImageConcanate`、`CreateVideo`、`FlashVSR_SM_KSampler`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`SaveVideo`、`LoadImage`、`ImageResizeKJv2`、`MaskToImage`、`DiffuEraserLoader`、`SaveImage`、`VHS_LoadVideo`、`DiffuEraserSampler`、`VHS_VideoInfo`、`MathExpression|pysssss`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、FlashVSR_SM_KSampler、DiffuEraserSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
