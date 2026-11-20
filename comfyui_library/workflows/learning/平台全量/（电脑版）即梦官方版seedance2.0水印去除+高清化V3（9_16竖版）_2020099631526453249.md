---
key: 平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2020099631526453249.json
name: （电脑版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2020099631526453249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2020099631526453249.json
hash: 72d5ddb828f4f310
coverage: 0.888889
learned_at: 2026-11-14 02:54:08
nodes: [easy showAnything, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageResizeKJv2, JWInteger, SaveImage, Note, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, GetVideoComponents, VHS_VideoCombine, DiffuEraserSampler, CreateVideo, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, VHS_LoadVideo, LoadImage, ImageFromBatch+, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, RepeatImageBatch, easy showAnything, MathExpression|pysssss, VHS_VideoInfo, FlashVSR_SM_KSampler, SaveVideo, CreateVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 525850476}
---

# 平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2020099631526453249.json

> 来源文件 `comfyui_library/workflows/平台全量/（电脑版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2020099631526453249.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `easy showAnything`
- `MaskToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageResizeKJv2`
- `JWInteger`
- `SaveImage`
- `Note`
- `ImageConcanate`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageConcanate`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `CreateVideo`
- `LayerUtility: PurgeVRAM V2`
- `DiffuEraserLoader`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `VHS_VideoInfo`
- `FlashVSR_SM_KSampler` ★核心
- `SaveVideo`
- `CreateVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `525850476`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`JWInteger`、`SaveImage`、`ImageConcanate`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`VHS_VideoCombine`、`DiffuEraserSampler`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`VHS_LoadVideo`、`LoadImage`、`MathExpression|pysssss`、`RepeatImageBatch`、`VHS_VideoInfo`、`FlashVSR_SM_KSampler`、`SaveVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
