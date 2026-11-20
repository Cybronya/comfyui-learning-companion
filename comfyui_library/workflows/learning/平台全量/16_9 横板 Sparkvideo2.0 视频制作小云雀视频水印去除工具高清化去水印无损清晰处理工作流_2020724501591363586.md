---
key: 平台全量/16_9 横板 Sparkvideo2.0 视频制作小云雀视频水印去除工具高清化去水印无损清晰处理工作流_2020724501591363586.json
name: 16_9 横板 Sparkvideo2.0 视频制作小云雀视频水印去除工具高清化去水印无损清晰处理工作流_2020724501591363586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/16_9 横板 Sparkvideo2.0 视频制作小云雀视频水印去除工具高清化去水印无损清晰处理工作流_2020724501591363586.json
hash: 58ed2840bcfe9cc0
coverage: 0.885714
learned_at: 2026-11-14 00:11:01
nodes: [ImageFromBatch+, ImageResizeKJv2, PreviewImage, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, easy showAnything, RepeatImageBatch, DiffuEraserSampler, DiffuEraserLoader, VHS_VideoCombine, VHS_VideoCombine, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, GetVideoComponents, ImageConcanate, Note, MaskToImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, LoadImage, JWInteger, VHS_LoadVideo, LayerUtility: PurgeVRAM V2, CreateVideo, ImageConcanate, FlashVSR_SM_Model, FlashVSR_SM_KSampler, CreateVideo, SaveVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1402111639}
---

# 平台全量/16_9 横板 Sparkvideo2.0 视频制作小云雀视频水印去除工具高清化去水印无损清晰处理工作流_2020724501591363586.json

> 来源文件 `comfyui_library/workflows/平台全量/16_9 横板 Sparkvideo2.0 视频制作小云雀视频水印去除工具高清化去水印无损清晰处理工作流_2020724501591363586.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `RepeatImageBatch`
- `DiffuEraserSampler` ★核心
- `DiffuEraserLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `GetVideoComponents`
- `ImageConcanate`
- `Note`
- `MaskToImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `LoadImage`
- `JWInteger`
- `VHS_LoadVideo`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `ImageConcanate`
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`
- `SaveVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `1402111639`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`ImageFromBatch+`、`ImageResizeKJv2`、`VHS_VideoInfo`、`MathExpression|pysssss`、`RepeatImageBatch`、`DiffuEraserSampler`、`DiffuEraserLoader`、`VHS_VideoCombine`、`GetVideoComponents`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`ImageConcanate`、`MaskToImage`、`SaveImage`、`LoadImage`、`VHS_LoadVideo`、`LayerUtility: PurgeVRAM V2`、`CreateVideo`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`SaveVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
