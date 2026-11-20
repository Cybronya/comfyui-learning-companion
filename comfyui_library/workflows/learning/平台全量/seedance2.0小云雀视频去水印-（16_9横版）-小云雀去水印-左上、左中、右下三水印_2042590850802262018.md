---
key: 平台全量/seedance2.0小云雀视频去水印-（16_9横版）-小云雀去水印-左上、左中、右下三水印_2042590850802262018.json
name: seedance2.0小云雀视频去水印-（16_9横版）-小云雀去水印-左上、左中、右下三水印_2042590850802262018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0小云雀视频去水印-（16_9横版）-小云雀去水印-左上、左中、右下三水印_2042590850802262018.json
hash: 880021739e9a1d1c
coverage: 0.875
learned_at: 2026-11-14 01:17:44
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, VHS_VideoCombine, Label (rgthree), MarkdownNote, DiffuEraserSampler, VHS_VideoCombine, MathExpression|pysssss, VHS_LoadVideo, ImageFromBatch+, SaveImage, LoadImage, CustomAddLabel, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1005693138}
---

# 平台全量/seedance2.0小云雀视频去水印-（16_9横版）-小云雀去水印-左上、左中、右下三水印_2042590850802262018.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0小云雀视频去水印-（16_9横版）-小云雀去水印-左上、左中、右下三水印_2042590850802262018.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `ImageResizeKJv2`
- `MaskToImage`
- `PreviewImage`
- `VHS_VideoInfo`
- `RepeatImageBatch`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `JWInteger`
- `MarkdownNote`
- `DiffuEraserLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageConcanate`
- `ImageFromBatch+`
- `GetVideoComponents`
- `CreateVideo`
- `LayerUtility: PurgeVRAM V2`
- `GetVideoComponents`
- `FlashVSR_SM_KSampler` ★核心
- `CustomAddLabel`
- `FlashVSR_SM_Model`
- `CreateVideo`
- `SaveVideo`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `MarkdownNote`
- `DiffuEraserSampler` ★核心
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `ImageFromBatch+`
- `SaveImage`
- `LoadImage`
- `CustomAddLabel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `1005693138`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`VHS_VideoCombine`、`Label (rgthree)`、`DiffuEraserSampler`、`VHS_LoadVideo`、`SaveImage`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
