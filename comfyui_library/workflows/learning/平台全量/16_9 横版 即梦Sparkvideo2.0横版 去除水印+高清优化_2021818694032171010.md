---
key: 平台全量/16_9 横版 即梦Sparkvideo2.0横版 去除水印+高清优化_2021818694032171010.json
name: 16_9 横版 即梦Sparkvideo2.0横版 去除水印+高清优化_2021818694032171010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/16_9 横版 即梦Sparkvideo2.0横版 去除水印+高清优化_2021818694032171010.json
hash: 089b203c06dbab05
coverage: 0.862069
learned_at: 2026-11-14 00:11:03
nodes: [CreateVideo, PreviewImage, MaskToImage, ImageResizeKJv2, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, RepeatImageBatch, easy showAnything, DiffuEraserLoader, DiffuEraserSampler, LayerUtility: PurgeVRAM V2, GetVideoComponents, ImageFromBatch+, JWInteger, GetVideoComponents, FlashVSR_SM_Model, JWInteger, CreateVideo, FlashVSR_SM_KSampler, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, SaveVideo, VHS_LoadVideo, JWInteger, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 171845222}
---

# 平台全量/16_9 横版 即梦Sparkvideo2.0横版 去除水印+高清优化_2021818694032171010.json

> 来源文件 `comfyui_library/workflows/平台全量/16_9 横版 即梦Sparkvideo2.0横版 去除水印+高清优化_2021818694032171010.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `CreateVideo`
- `PreviewImage`
- `MaskToImage`
- `ImageResizeKJv2`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatImageBatch`
- `easy showAnything`
- `DiffuEraserLoader`
- `DiffuEraserSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `GetVideoComponents`
- `ImageFromBatch+`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `JWInteger`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `SaveVideo`
- `VHS_LoadVideo`
- `JWInteger`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `seed` = `1280`
- `steps` = `171845222`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`CreateVideo`、`MaskToImage`、`ImageResizeKJv2`、`VHS_VideoInfo`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatImageBatch`、`DiffuEraserLoader`、`DiffuEraserSampler`、`LayerUtility: PurgeVRAM V2`、`GetVideoComponents`、`ImageFromBatch+`、`JWInteger`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`VHS_VideoCombine`、`SaveVideo`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、DiffuEraserLoader
