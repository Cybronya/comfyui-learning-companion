---
key: 平台全量/（新动态版）手机版即梦分身Seedance 2.0水印去除+高清化V6（9_16竖版）_2027298818005405697.json
name: （新动态版）手机版即梦分身Seedance 2.0水印去除+高清化V6（9_16竖版）_2027298818005405697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（新动态版）手机版即梦分身Seedance 2.0水印去除+高清化V6（9_16竖版）_2027298818005405697.json
hash: a30051b6798dc314
coverage: 0.875
learned_at: 2026-11-14 02:54:01
nodes: [ImageResizeKJv2, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, DiffuEraserSampler, CreateVideo, DiffuEraserLoader, MathExpression|pysssss, RepeatImageBatch, easy showAnything, MathExpression|pysssss, VHS_VideoCombine, FlashVSR_SM_KSampler, ImageFromBatch+, LoadImage, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, RunningHub Deepcleaner, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfo, easy showAnything, VHS_LoadVideo, PreviewImage, SaveImage, JWInteger, Note, MaskToImage, ImageConcanate]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 553878471}
---

# 平台全量/（新动态版）手机版即梦分身Seedance 2.0水印去除+高清化V6（9_16竖版）_2027298818005405697.json

> 来源文件 `comfyui_library/workflows/平台全量/（新动态版）手机版即梦分身Seedance 2.0水印去除+高清化V6（9_16竖版）_2027298818005405697.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（32 个）：
- `ImageResizeKJv2`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetVideoComponents`
- `DiffuEraserSampler` ★核心
- `CreateVideo`
- `DiffuEraserLoader`
- `MathExpression|pysssss`
- `RepeatImageBatch`
- `easy showAnything`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `FlashVSR_SM_KSampler` ★核心
- `ImageFromBatch+`
- `LoadImage`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `RunningHub Deepcleaner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfo`
- `easy showAnything`
- `VHS_LoadVideo`
- `PreviewImage`
- `SaveImage`
- `JWInteger`
- `Note`
- `MaskToImage`
- `ImageConcanate`

## 关键参数

- `seed` = `1280`
- `steps` = `553878471`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`ImageResizeKJv2`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`DiffuEraserSampler`、`CreateVideo`、`DiffuEraserLoader`、`MathExpression|pysssss`、`RepeatImageBatch`、`VHS_VideoCombine`、`FlashVSR_SM_KSampler`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`RunningHub Deepcleaner`、`VHS_VideoInfo`、`VHS_LoadVideo`、`SaveImage`、`MaskToImage`、`ImageConcanate`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、CreateVideo、DiffuEraserLoader
