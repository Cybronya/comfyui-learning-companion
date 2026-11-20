---
key: 平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-单水印_2028830812015169537.json
name: seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-单水印_2028830812015169537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-单水印_2028830812015169537.json
hash: d3676c72f0ad4b51
coverage: 0.846154
learned_at: 2026-11-14 01:17:51
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, Label (rgthree), SaveImage, LoadImage, MarkdownNote, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, MarkdownNote, CustomAddLabel, VHS_LoadVideo, DiffuEraserSampler, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1284373597}
---

# 平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-单水印_2028830812015169537.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-单水印_2028830812015169537.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
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
- `ImageFromBatch+`
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
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MarkdownNote`
- `CustomAddLabel`
- `VHS_LoadVideo`
- `DiffuEraserSampler` ★核心
- `MathExpression|pysssss`

## 关键参数

- `seed` = `1280`
- `steps` = `1284373597`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`ImageConcanate`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`Label (rgthree)`、`SaveImage`、`LoadImage`、`VHS_VideoCombine`、`VHS_LoadVideo`、`DiffuEraserSampler`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
