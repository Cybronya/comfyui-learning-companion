---
key: 平台全量/Ltx2.3字幕乱码去除+高清化V3_2045147059384229889.json
name: Ltx2.3字幕乱码去除+高清化V3_2045147059384229889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Ltx2.3字幕乱码去除+高清化V3_2045147059384229889.json
hash: 1714f8eef3545212
coverage: 0.896552
learned_at: 2026-11-14 00:39:29
nodes: [ImageResizeKJv2, DiffuEraserSampler, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoInfo, easy showAnything, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, easy showAnything, RepeatImageBatch, RunningHub Deepcleaner, CreateVideo, GetVideoComponents, ImageFromBatch+, GetVideoComponents, FlashVSR_SM_Model, FlashVSR_SM_KSampler, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, MaskToImage, VHS_LoadVideo, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, JWInteger, ImageFromBatch+, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 661854944}
---

# 平台全量/Ltx2.3字幕乱码去除+高清化V3_2045147059384229889.json

> 来源文件 `comfyui_library/workflows/平台全量/Ltx2.3字幕乱码去除+高清化V3_2045147059384229889.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `ImageResizeKJv2`
- `DiffuEraserSampler` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoInfo`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `DiffuEraserLoader`
- `easy showAnything`
- `RepeatImageBatch`
- `RunningHub Deepcleaner`
- `CreateVideo`
- `GetVideoComponents`
- `ImageFromBatch+`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `JWInteger`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `MaskToImage`
- `VHS_LoadVideo`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `JWInteger`
- `ImageFromBatch+`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `661854944`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`ImageResizeKJv2`、`DiffuEraserSampler`、`MathExpression|pysssss`、`VHS_VideoInfo`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`RepeatImageBatch`、`RunningHub Deepcleaner`、`CreateVideo`、`GetVideoComponents`、`ImageFromBatch+`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`MaskToImage`、`VHS_LoadVideo`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、CreateVideo、DiffuEraserLoader
