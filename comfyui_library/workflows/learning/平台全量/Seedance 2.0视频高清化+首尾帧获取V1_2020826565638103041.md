---
key: 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2020826565638103041.json
name: Seedance 2.0视频高清化+首尾帧获取V1_2020826565638103041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2020826565638103041.json
hash: 924b60c20beabe2e
coverage: 1
learned_at: 2026-11-14 01:00:15
nodes: [CreateVideo, SaveVideo, VHS_VideoCombine, GetVideoComponents, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, LoadVideo, ImageFromBatch+, SaveImage, SaveImage, FlashVSR_SM_KSampler, GetImageSizeAndCount, ImageFromBatch+, JWInteger]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1943190128}
---

# 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2020826565638103041.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2020826565638103041.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（18 个）：
- `CreateVideo`
- `SaveVideo`
- `VHS_VideoCombine`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageConcanate`
- `LoadVideo`
- `ImageFromBatch+`
- `SaveImage`
- `SaveImage`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `JWInteger`

## 关键参数

- `seed` = `1280`
- `steps` = `1943190128`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`CreateVideo`、`SaveVideo`、`VHS_VideoCombine`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`ImageConcanate`、`LoadVideo`、`SaveImage`、`FlashVSR_SM_KSampler`、`GetImageSizeAndCount`

**用到的条目**：FlashVSR_SM_KSampler、GetImageSizeAndCount、SaveImage、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageConcanate
