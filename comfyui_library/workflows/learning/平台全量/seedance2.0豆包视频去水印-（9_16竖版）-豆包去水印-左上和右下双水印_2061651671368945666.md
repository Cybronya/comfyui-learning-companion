---
key: 平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2061651671368945666.json
name: seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2061651671368945666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2061651671368945666.json
hash: 635cb3f9122c38ba
coverage: 0.842105
learned_at: 2026-11-14 01:17:51
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, JWInteger, ImageFromBatch+, GetVideoComponents, GetVideoComponents, CustomAddLabel, SaveVideo, VHS_VideoCombine, ImageFromBatch+, VHS_VideoCombine, DiffuEraserSampler, CustomAddLabel, VHS_LoadVideo, LoadImage, easy showAnything, PreviewImage, VHS_VideoCombine, Reroute, MathExpression|pysssss, CreateVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, FlashVSR_SM_KSampler, CreateVideo, FlashVSR_SM_Model, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 2026979301}
---

# 平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2061651671368945666.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0豆包视频去水印-（9_16竖版）-豆包去水印-左上和右下双水印_2061651671368945666.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（38 个）：
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
- `JWInteger`
- `ImageFromBatch+`
- `GetVideoComponents`
- `GetVideoComponents`
- `CustomAddLabel`
- `SaveVideo`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `CustomAddLabel`
- `VHS_LoadVideo`
- `LoadImage`
- `easy showAnything`
- `PreviewImage`
- `VHS_VideoCombine`
- `Reroute`
- `MathExpression|pysssss`
- `CreateVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`
- `FlashVSR_SM_Model`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `2026979301`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CustomAddLabel`、`SaveVideo`、`VHS_VideoCombine`、`DiffuEraserSampler`、`VHS_LoadVideo`、`LoadImage`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、CustomAddLabel
