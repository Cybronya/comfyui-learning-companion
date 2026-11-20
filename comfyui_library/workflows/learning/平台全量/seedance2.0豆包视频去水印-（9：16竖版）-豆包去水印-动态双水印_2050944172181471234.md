---
key: 平台全量/seedance2.0豆包视频去水印-（9：16竖版）-豆包去水印-动态双水印_2050944172181471234.json
name: seedance2.0豆包视频去水印-（9：16竖版）-豆包去水印-动态双水印_2050944172181471234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9：16竖版）-豆包去水印-动态双水印_2050944172181471234.json
hash: 90a68b104a704e61
coverage: 0.85
learned_at: 2026-11-14 01:17:54
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, VHS_VideoCombine, Label (rgthree), MarkdownNote, ImageFromBatch+, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, DiffuEraserSampler, VHS_VideoCombine, MathExpression|pysssss, VHS_LoadVideo, LoadImage, CustomAddLabel]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 490073887}
---

# 平台全量/seedance2.0豆包视频去水印-（9：16竖版）-豆包去水印-动态双水印_2050944172181471234.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9：16竖版）-豆包去水印-动态双水印_2050944172181471234.json`

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
- `ImageFromBatch+`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `LoadImage`
- `CustomAddLabel`

## 关键参数

- `seed` = `1280`
- `steps` = `490073887`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`VHS_VideoCombine`、`Label (rgthree)`、`DiffuEraserSampler`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、CustomAddLabel
