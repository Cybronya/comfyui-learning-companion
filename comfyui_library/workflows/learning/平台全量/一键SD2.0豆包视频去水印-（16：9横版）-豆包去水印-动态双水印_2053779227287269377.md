---
key: 平台全量/一键SD2.0豆包视频去水印-（16：9横版）-豆包去水印-动态双水印_2053779227287269377.json
name: 一键SD2.0豆包视频去水印-（16：9横版）-豆包去水印-动态双水印_2053779227287269377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键SD2.0豆包视频去水印-（16：9横版）-豆包去水印-动态双水印_2053779227287269377.json
hash: e53784470a09586b
coverage: 0.846154
learned_at: 2026-11-14 01:27:18
nodes: [ImageResizeKJv2, MaskToImage, PreviewImage, VHS_VideoInfo, RepeatImageBatch, easy showAnything, easy showAnything, MathExpression|pysssss, JWInteger, MarkdownNote, DiffuEraserLoader, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, ImageFromBatch+, GetVideoComponents, CreateVideo, LayerUtility: PurgeVRAM V2, GetVideoComponents, FlashVSR_SM_KSampler, CustomAddLabel, FlashVSR_SM_Model, CreateVideo, SaveVideo, VHS_VideoCombine, MarkdownNote, ImageFromBatch+, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, DiffuEraserSampler, VHS_VideoCombine, CustomAddLabel, MathExpression|pysssss, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1837616574}
---

# 平台全量/一键SD2.0豆包视频去水印-（16：9横版）-豆包去水印-动态双水印_2053779227287269377.json

> 来源文件 `comfyui_library/workflows/平台全量/一键SD2.0豆包视频去水印-（16：9横版）-豆包去水印-动态双水印_2053779227287269377.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（39 个）：
- `ImageResizeKJv2`
- `MaskToImage`
- `PreviewImage`
- `VHS_VideoInfo`
- `RepeatImageBatch`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `JWInteger`
- `MarkdownNote`
- `DiffuEraserLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
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
- `VHS_VideoCombine`
- `MarkdownNote`
- `ImageFromBatch+`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `DiffuEraserSampler` ★核心
- `VHS_VideoCombine`
- `CustomAddLabel`
- `MathExpression|pysssss`
- `LoadImage`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1837616574`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`ImageResizeKJv2`、`MaskToImage`、`VHS_VideoInfo`、`RepeatImageBatch`、`MathExpression|pysssss`、`JWInteger`、`DiffuEraserLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`ImageFromBatch+`、`GetVideoComponents`、`CreateVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_KSampler`、`CustomAddLabel`、`FlashVSR_SM_Model`、`SaveVideo`、`VHS_VideoCombine`、`DiffuEraserSampler`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveVideo、CreateVideo、CustomAddLabel
