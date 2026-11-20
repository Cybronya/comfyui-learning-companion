---
key: 平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2028161736657870850.json
name: seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2028161736657870850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2028161736657870850.json
hash: cf8d638c0198f10d
coverage: 0.871795
learned_at: 2026-11-14 01:17:41
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, MathExpression|pysssss, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageFromBatch+, DiffuEraserSampler, CustomAddLabel, VHS_VideoCombine, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, VHS_VideoCombine, Label (rgthree), VHS_VideoCombine, MarkdownNote, SaveImage, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1843875205}
---

# 平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2028161736657870850.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2028161736657870850.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `ImageResizeKJv2`
- `MaskToImage`
- `PreviewImage`
- `VHS_VideoInfo`
- `RepeatImageBatch`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `JWInteger`
- `MarkdownNote`
- `DiffuEraserLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageFromBatch+`
- `DiffuEraserSampler` ★核心
- `CustomAddLabel`
- `VHS_VideoCombine`
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
- `VHS_VideoCombine`
- `MarkdownNote`
- `SaveImage`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `1843875205`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`DiffuEraserSampler`、`CustomAddLabel`、`VHS_VideoCombine`、`ImageConcanate`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`SaveVideo`、`Label (rgthree)`、`SaveImage`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
