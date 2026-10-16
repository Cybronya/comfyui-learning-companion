---
key: 视频生成/图生视频/即梦官方版seedance2.0水印去除+高清化V2（9_16竖版）_2020315533945606146.json
name: 即梦官方版seedance2.0水印去除+高清化V2（9_16竖版）_2020315533945606146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2020315533945606146.json
hash: 19fbf49bdec79451
coverage: 0.885714
learned_at: 2026-10-15 22:35:06
nodes: [easy showAnything, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageResizeKJv2, JWInteger, SaveImage, Note, CreateVideo, FlashVSR_SM_KSampler, SaveVideo, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, GetVideoComponents, VHS_VideoCombine, DiffuEraserSampler, CreateVideo, LayerUtility: PurgeVRAM V2, DiffuEraserLoader, VHS_LoadVideo, LoadImage, ImageFromBatch+, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss, RepeatImageBatch, easy showAnything, MathExpression|pysssss, VHS_VideoInfo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1846869710}
---

# 视频生成/图生视频/即梦官方版seedance2.0水印去除+高清化V2（9_16竖版）_2020315533945606146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2020315533945606146.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `easy showAnything`
- `MaskToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageResizeKJv2`
- `JWInteger`
- `SaveImage`
- `Note`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `SaveVideo`
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

## 关键参数

- `seed` = `1280`
- `steps` = `1846869710`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`JWInteger`、`SaveImage`、`CreateVideo`、`FlashVSR_SM_KSampler`、`SaveVideo`、`ImageConcanate`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`VHS_VideoCombine`、`DiffuEraserSampler`、`LayerUtility: PurgeVRAM V2`、`DiffuEraserLoader`、`VHS_LoadVideo`、`LoadImage`、`MathExpression|pysssss`、`RepeatImageBatch`、`VHS_VideoInfo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、FlashVSR_SM_KSampler、DiffuEraserSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
