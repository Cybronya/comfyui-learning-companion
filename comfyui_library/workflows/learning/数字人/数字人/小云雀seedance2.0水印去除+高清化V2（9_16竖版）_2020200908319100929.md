---
key: 数字人/数字人/小云雀seedance2.0水印去除+高清化V2（9_16竖版）_2020200908319100929.json
name: 小云雀seedance2.0水印去除+高清化V2（9_16竖版）_2020200908319100929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/小云雀seedance2.0水印去除+高清化V2（9_16竖版）_2020200908319100929.json
hash: b560aafcfefd42a9
coverage: 0.885714
learned_at: 2026-10-26 02:01:57
nodes: [easy showAnything, easy showAnything, ImageResizeKJv2, RepeatImageBatch, JWInteger, SaveImage, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, GetVideoComponents, VHS_VideoCombine, DiffuEraserSampler, CreateVideo, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, ImageFromBatch+, VHS_VideoCombine, VHS_LoadVideo, LoadImage, PreviewImage, MaskToImage, Note, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, SaveVideo, FlashVSR_SM_KSampler, CreateVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 354410570}
---

# 数字人/数字人/小云雀seedance2.0水印去除+高清化V2（9_16竖版）_2020200908319100929.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/小云雀seedance2.0水印去除+高清化V2（9_16竖版）_2020200908319100929.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `easy showAnything`
- `easy showAnything`
- `ImageResizeKJv2`
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
- `VHS_LoadVideo`
- `LoadImage`
- `PreviewImage`
- `MaskToImage`
- `Note`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `SaveVideo`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `354410570`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`ImageResizeKJv2`、`RepeatImageBatch`、`JWInteger`、`SaveImage`、`ImageConcanate`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`DiffuEraserSampler`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`VHS_LoadVideo`、`LoadImage`、`MaskToImage`、`VHS_VideoInfo`、`MathExpression|pysssss`、`SaveVideo`、`FlashVSR_SM_KSampler`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、FlashVSR_SM_KSampler、DiffuEraserSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
