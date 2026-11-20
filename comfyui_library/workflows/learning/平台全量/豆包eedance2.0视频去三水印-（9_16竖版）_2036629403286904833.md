---
key: 平台全量/豆包eedance2.0视频去三水印-（9_16竖版）_2036629403286904833.json
name: 豆包eedance2.0视频去三水印-（9_16竖版）_2036629403286904833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/豆包eedance2.0视频去三水印-（9_16竖版）_2036629403286904833.json
hash: da1ca563b418dd11
coverage: 0.864865
learned_at: 2026-11-14 02:44:49
nodes: [VHS_VideoInfo, RepeatImageBatch, easy showAnything, MathExpression|pysssss, JWInteger, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, LoadImage, ImageFromBatch+, PreviewImage, ImageResizeKJv2, MaskToImage, PreviewImage, MarkdownNote, CustomAddLabel, VHS_VideoCombine, MathExpression|pysssss, VHS_VideoCombine, VHS_LoadVideo, ImageConcanate, DiffuEraserSampler, VHS_VideoCombine, easy showAnything, JWInteger]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 855381687}
---

# 平台全量/豆包eedance2.0视频去三水印-（9_16竖版）_2036629403286904833.json

> 来源文件 `comfyui_library/workflows/平台全量/豆包eedance2.0视频去三水印-（9_16竖版）_2036629403286904833.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `VHS_VideoInfo`
- `RepeatImageBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `JWInteger`
- `DiffuEraserLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `LoadImage`
- `ImageFromBatch+`
- `PreviewImage`
- `ImageResizeKJv2`
- `MaskToImage`
- `PreviewImage`
- `MarkdownNote`
- `CustomAddLabel`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `ImageConcanate`
- `DiffuEraserSampler` ★核心
- `VHS_VideoCombine`
- `easy showAnything`
- `JWInteger`

## 关键参数

- `seed` = `1280`
- `steps` = `855381687`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`LoadImage`、`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoCombine`、`VHS_LoadVideo`、`DiffuEraserSampler`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、CustomAddLabel
