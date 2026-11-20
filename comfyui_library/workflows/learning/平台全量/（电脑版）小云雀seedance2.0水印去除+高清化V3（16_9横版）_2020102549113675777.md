---
key: 平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（16_9横版）_2020102549113675777.json
name: （电脑版）小云雀seedance2.0水印去除+高清化V3（16_9横版）_2020102549113675777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（16_9横版）_2020102549113675777.json
hash: 42dc58e47fdb5658
coverage: 0.888889
learned_at: 2026-11-14 02:54:08
nodes: [DiffuEraserLoader, easy showAnything, ImageResizeKJv2, RepeatImageBatch, ImageConcanate, MaskToImage, PreviewImage, Note, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, CreateVideo, DiffuEraserSampler, VHS_VideoCombine, ImageFromBatch+, JWInteger, VHS_LoadVideo, LoadImage, VHS_VideoCombine, easy showAnything, VHS_VideoInfo, MathExpression|pysssss, MathExpression|pysssss, SaveVideo, FlashVSR_SM_KSampler, CreateVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 913906961}
---

# 平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（16_9横版）_2020102549113675777.json

> 来源文件 `comfyui_library/workflows/平台全量/（电脑版）小云雀seedance2.0水印去除+高清化V3（16_9横版）_2020102549113675777.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `DiffuEraserLoader`
- `easy showAnything`
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `ImageConcanate`
- `MaskToImage`
- `PreviewImage`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `ImageConcanate`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `CreateVideo`
- `DiffuEraserSampler` ★核心
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `JWInteger`
- `VHS_LoadVideo`
- `LoadImage`
- `VHS_VideoCombine`
- `easy showAnything`
- `VHS_VideoInfo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `SaveVideo`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `913906961`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **89%**（32/36）

**有卡**：`DiffuEraserLoader`、`ImageResizeKJv2`、`RepeatImageBatch`、`ImageConcanate`、`MaskToImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`CreateVideo`、`DiffuEraserSampler`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`、`MathExpression|pysssss`、`SaveVideo`、`FlashVSR_SM_KSampler`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、DiffuEraserSampler、FlashVSR_SM_KSampler、ImageResizeKJv2、SaveImage、SaveVideo、CreateVideo
