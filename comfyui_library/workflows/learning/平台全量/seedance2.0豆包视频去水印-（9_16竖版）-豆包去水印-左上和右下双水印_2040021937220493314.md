---
key: 平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2040021937220493314.json
name: seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2040021937220493314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2040021937220493314.json
hash: 963fb985bdf307e7
coverage: 0.829268
learned_at: 2026-11-14 01:17:51
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, VHS_VideoCombine, Label (rgthree), MarkdownNote, ImageFromBatch+, VHS_VideoCombine, DiffuEraserSampler, CustomAddLabel, VHS_LoadVideo, LoadImage, VHS_VideoCombine, easy showAnything, PreviewImage, VHS_VideoCombine, Reroute, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1877426796}
---

# 平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2040021937220493314.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2040021937220493314.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `ImageResizeKJv2`
- `MaskToImage`
- `PreviewImage`
- `VHS_VideoInfo`
- `RepeatImageBatch`
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
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `CustomAddLabel`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `easy showAnything`
- `PreviewImage`
- `VHS_VideoCombine`
- `Reroute`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `1280`
- `steps` = `1877426796`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`VHS_VideoCombine`、`Label (rgthree)`、`DiffuEraserSampler`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、CustomAddLabel
