---
key: 平台全量/seedance2.0豆包视频去水印-（1_1方形）-豆包去水印-三水印_2034990615485751297.json
name: seedance2.0豆包视频去水印-（1_1方形）-豆包去水印-三水印_2034990615485751297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（1_1方形）-豆包去水印-三水印_2034990615485751297.json
hash: df8e7cbecec0c786
coverage: 0.842105
learned_at: 2026-11-14 01:17:50
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, Label (rgthree), MarkdownNote, ImageFromBatch+, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, DiffuEraserSampler, VHS_VideoCombine, LoadImage, CustomAddLabel, VHS_LoadVideo, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 555968039}
---

# 平台全量/seedance2.0豆包视频去水印-（1_1方形）-豆包去水印-三水印_2034990615485751297.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（1_1方形）-豆包去水印-三水印_2034990615485751297.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
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
- `Label (rgthree)`
- `MarkdownNote`
- `ImageFromBatch+`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `CustomAddLabel`
- `VHS_LoadVideo`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `1280`
- `steps` = `555968039`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`Label (rgthree)`、`VHS_VideoCombine`、`DiffuEraserSampler`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、CustomAddLabel
