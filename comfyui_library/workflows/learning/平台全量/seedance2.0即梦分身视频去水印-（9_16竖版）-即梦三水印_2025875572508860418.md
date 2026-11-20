---
key: 平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2025875572508860418.json
name: seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2025875572508860418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2025875572508860418.json
hash: 36b2be49829a457f
coverage: 0.875
learned_at: 2026-11-14 01:17:41
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageFromBatch+, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, VHS_VideoCombine, Label (rgthree), MarkdownNote, SaveImage, LoadImage, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, DiffuEraserSampler, CustomAddLabel, VHS_LoadVideo, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1002376109}
---

# 平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2025875572508860418.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2025875572508860418.json`

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
- `ImageFromBatch+`
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
- `SaveImage`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `CustomAddLabel`
- `VHS_LoadVideo`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `1280`
- `steps` = `1002376109`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`ImageConcanate`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`VHS_VideoCombine`、`Label (rgthree)`、`SaveImage`、`LoadImage`、`DiffuEraserSampler`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
