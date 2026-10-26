---
key: 数字人/数字人/小云雀seedance2.0水印去除+高清化V2（16_9横版）_2020301691408617474.json
name: 小云雀seedance2.0水印去除+高清化V2（16_9横版）_2020301691408617474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/小云雀seedance2.0水印去除+高清化V2（16_9横版）_2020301691408617474.json
hash: d00482abfd3bff45
coverage: 0.885714
learned_at: 2026-10-26 02:01:56
nodes: [DiffuEraserLoader, easy showAnything, ImageResizeKJv2, RepeatImageBatch, ImageConcanate, MaskToImage, PreviewImage, Note, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, CreateVideo, FlashVSR_SM_KSampler, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, CreateVideo, DiffuEraserSampler, VHS_VideoCombine, SaveVideo, ImageFromBatch+, JWInteger, VHS_LoadVideo, LoadImage, VHS_VideoCombine, easy showAnything, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, ImageConcanate]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1072491452}
---

# 数字人/数字人/小云雀seedance2.0水印去除+高清化V2（16_9横版）_2020301691408617474.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/小云雀seedance2.0水印去除+高清化V2（16_9横版）_2020301691408617474.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `DiffuEraserLoader`
- `easy showAnything`
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `ImageConcanate`
- `MaskToImage`
- `PreviewImage`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `DiffuEraserSampler` ★核心
- `VHS_VideoCombine`
- `SaveVideo`
- `ImageFromBatch+`
- `JWInteger`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `easy showAnything`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageConcanate`

## 关键参数

- `seed` = `1280`
- `steps` = `1072491452`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`DiffuEraserLoader`、`ImageResizeKJv2`、`RepeatImageBatch`、`ImageConcanate`、`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`CreateVideo`、`FlashVSR_SM_KSampler`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserSampler`、`SaveVideo`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`、`MathExpression|pysssss`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、FlashVSR_SM_KSampler、DiffuEraserSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
