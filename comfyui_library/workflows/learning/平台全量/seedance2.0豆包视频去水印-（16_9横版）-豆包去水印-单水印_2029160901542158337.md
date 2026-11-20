---
key: 平台全量/seedance2.0豆包视频去水印-（16_9横版）-豆包去水印-单水印_2029160901542158337.json
name: seedance2.0豆包视频去水印-（16_9横版）-豆包去水印-单水印_2029160901542158337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（16_9横版）-豆包去水印-单水印_2029160901542158337.json
hash: b6437afa1fb07e20
coverage: 0.829268
learned_at: 2026-11-14 01:17:47
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, VHS_VideoCombine, Label (rgthree), MarkdownNote, LoadImage, ImageFromBatch+, PreviewImage, MarkdownNote, VHS_VideoCombine, DiffuEraserSampler, CustomAddLabel, VHS_LoadVideo, MathExpression|pysssss, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 624647320}
---

# 平台全量/seedance2.0豆包视频去水印-（16_9横版）-豆包去水印-单水印_2029160901542158337.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（16_9横版）-豆包去水印-单水印_2029160901542158337.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
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
- `LoadImage`
- `ImageFromBatch+`
- `PreviewImage`
- `MarkdownNote`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `CustomAddLabel`
- `VHS_LoadVideo`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `624647320`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`VHS_VideoCombine`、`Label (rgthree)`、`LoadImage`、`DiffuEraserSampler`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、CustomAddLabel
