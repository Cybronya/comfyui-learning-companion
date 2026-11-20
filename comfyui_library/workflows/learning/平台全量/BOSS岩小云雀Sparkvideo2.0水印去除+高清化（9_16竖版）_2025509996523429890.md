---
key: 平台全量/BOSS岩小云雀Sparkvideo2.0水印去除+高清化（9_16竖版）_2025509996523429890.json
name: BOSS岩小云雀Sparkvideo2.0水印去除+高清化（9_16竖版）_2025509996523429890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/BOSS岩小云雀Sparkvideo2.0水印去除+高清化（9_16竖版）_2025509996523429890.json
hash: 7dcd7e97dca1670a
coverage: 0.885714
learned_at: 2026-11-14 00:19:36
nodes: [ImageFromBatch+, ImageResizeKJv2, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, easy showAnything, RepeatImageBatch, DiffuEraserSampler, LayerUtility: PurgeVRAM V2, ImageConcanate, DiffuEraserLoader, VHS_VideoCombine, VHS_VideoCombine, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, FlashVSR_SM_Model, FlashVSR_SM_KSampler, GetVideoComponents, CreateVideo, ImageConcanate, CreateVideo, VHS_VideoCombine, SaveImage, Note, MaskToImage, VHS_LoadVideo, JWInteger, SaveVideo, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 931330489}
---

# 平台全量/BOSS岩小云雀Sparkvideo2.0水印去除+高清化（9_16竖版）_2025509996523429890.json

> 来源文件 `comfyui_library/workflows/平台全量/BOSS岩小云雀Sparkvideo2.0水印去除+高清化（9_16竖版）_2025509996523429890.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `RepeatImageBatch`
- `DiffuEraserSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageConcanate`
- `DiffuEraserLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `GetVideoComponents`
- `CreateVideo`
- `ImageConcanate`
- `CreateVideo`
- `VHS_VideoCombine`
- `SaveImage`
- `Note`
- `MaskToImage`
- `VHS_LoadVideo`
- `JWInteger`
- `SaveVideo`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `931330489`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`ImageFromBatch+`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfo`、`MathExpression|pysssss`、`RepeatImageBatch`、`DiffuEraserSampler`、`LayerUtility: PurgeVRAM V2`、`ImageConcanate`、`DiffuEraserLoader`、`VHS_VideoCombine`、`GetVideoComponents`、`JWInteger`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`CreateVideo`、`SaveImage`、`MaskToImage`、`VHS_LoadVideo`、`SaveVideo`、`LoadImage`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
