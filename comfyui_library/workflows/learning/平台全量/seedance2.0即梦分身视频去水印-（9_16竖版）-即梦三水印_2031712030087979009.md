---
key: 平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2031712030087979009.json
name: seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2031712030087979009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2031712030087979009.json
hash: 1a4f4a30fdf127c0
coverage: 0.871795
learned_at: 2026-11-14 01:17:42
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, MathExpression|pysssss, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageFromBatch+, DiffuEraserSampler, CustomAddLabel, VHS_VideoCombine, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, Label (rgthree), VHS_VideoCombine, LoadImage, SaveImage, VHS_VideoCombine, VHS_LoadVideo, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1270499636}
---

# 平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2031712030087979009.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0即梦分身视频去水印-（9_16竖版）-即梦三水印_2031712030087979009.json`

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
- `Label (rgthree)`
- `VHS_VideoCombine`
- `LoadImage`
- `SaveImage`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `MarkdownNote`

## 关键参数

- `seed` = `1280`
- `steps` = `1270499636`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`DiffuEraserSampler`、`CustomAddLabel`、`VHS_VideoCombine`、`ImageConcanate`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`FlashVSR_SM_Model`、`SaveVideo`、`Label (rgthree)`、`LoadImage`、`SaveImage`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
