---
key: 平台全量/（动态版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2021165391262785537.json
name: （动态版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2021165391262785537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（动态版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2021165391262785537.json
hash: 7450dabc764340bc
coverage: 0.888889
learned_at: 2026-11-14 02:53:52
nodes: [easy showAnything, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageResizeKJv2, JWInteger, SaveImage, Note, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, GetVideoComponents, VHS_VideoCombine, DiffuEraserSampler, CreateVideo, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, ImageFromBatch+, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, RepeatImageBatch, easy showAnything, MathExpression|pysssss, VHS_VideoInfo, VHS_LoadVideo, LoadImage, VHS_VideoCombine, FlashVSR_SM_KSampler, SaveVideo, CreateVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1180326321}
---

# 平台全量/（动态版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2021165391262785537.json

> 来源文件 `comfyui_library/workflows/平台全量/（动态版）即梦官方版seedance2.0水印去除+高清化V3（9_16竖版）_2021165391262785537.json`

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
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `FlashVSR_SM_KSampler` ★核心
- `SaveVideo`
- `CreateVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1180326321`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`JWInteger`、`SaveImage`、`ImageConcanate`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`VHS_VideoCombine`、`DiffuEraserSampler`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`MathExpression|pysssss`、`RepeatImageBatch`、`VHS_VideoInfo`、`VHS_LoadVideo`、`LoadImage`、`FlashVSR_SM_KSampler`、`SaveVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
